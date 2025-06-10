# Implementing the simple authentication account-driven enrollment flow

**Framework**: Device Management

Examine the steps between the user, client, server, and Apple services in the simple authentication flow.

#### Overview

To implement account-driven enrollment, you need to support a series of interactions between the user’s device and your MDM server. The following diagrams illustrate the interactions, and the sections below detail each of the interaction steps.

![A sequence diagram showing the first five interactions between the user, client, server, and Apple servers for simple authentication.](https://docs-assets.developer.apple.com/published/0d3c28bcc45f65cb5210f9635b1a95a6/media-4091468%402x.png)

##### Sign in

In step 1, a person enters a user account identifier to start the MDM enrollment flow. The identifier needs to conform to a  format, where  is a user identifier, and  is a fully qualified domain name (FQDN) corresponding to a domain that advertises the MDM service for the person’s organization. The client splits the supplied identifier at the last occurrence of the @ character. If the resulting components are invalid (for example, empty or not an FQDN), an error occurs, and the person can reenter a valid identifier to proceed or can cancel the enrollment.

##### Send the Well Known Request

In step 2, the client sends an `HTTPS GET` request for the URL `https://<domain>/.well-known/com.apple.remotemanagement` (where `<domain>` is the domain/FQDN portion of the user identifier that the client extracts in the previous step). The client includes two query parameters in the URL path:

- `user-identifier`: The value of the user account identifier entered in step 1 above.
- `model-family`: The device’s model family.

Possible values of `model-family` are:

- `AppleTV`
- `iPad`
- `iPhone`
- `Mac`
- `RealityDevice`
- `Watch`

The server uses these values to help determine whether a user or a device enrollment needs to occur, and which MDM server the device uses for enrollment (for example, the system can assign different sets of users to different MDM servers within an organization, so the response for each user matches their assigned MDM server).

The server can send an HTTP redirect response for this request, and the client follows the redirect. However, the client doesn’t add the original query parameters to the redirect URL, so it’s the responsibility of the server to include all appropriate query parameters. This redirect behavior is useful in cases where it’s hard to set up the well-known service on the web server that the system uses for the top-level organization domain (as extracted from the user identifier). In that case, you can configure the top-level web server with a simple static redirect rule for the well-known URL that points to a different server (typically the MDM server) that actually handles the request.

###### Redirect the Well Known Request

It’s sometimes difficult for an organization to host the well-known service discovery endpoint at the web server that serves the top-level organization domain. To avoid the need for that, Apple provides a fallback discovery service that can redirect the device to a well-known resource that another server (typically the MDM server) hosts at the organization. This approach works only when the service discovery user identifier matches a Managed Apple Account associated with the organization.

If the initial well-known request from the device results in an HTTP failure status response (404, 403, and so on), the device makes a request to Apple Business/School Manager (AxM), and includes the original query parameters. AxM then redirects the device to the actual well-known endpoint for the organization’s MDM server.

The organization’s MDM server needs to instruct Apple Business/School Manager (AxM) on how to map the organization’s user identifiers to the appropriate endpoint. You do that using a new AxM endpoint where the MDM server can configure the redirect URL for its organization. Note that this URL is publicly accessible in typical deployments, so don’t assume its secrecy. For more information, see [`Assign Account-Driven Enrollment Service Discovery`](assign-account-driven-enrollment-profile.md).

Support for this is available in iOS 18.2, macOS 15.2, and visionOS 2.2, and later.

##### Process the Json Document

In step 3, the server returns a JSON document that conforms to the schema defined below. The client extracts the `BaseURL` property in the first JSON array object and uses it in subsequent requests. If the response is malformed, or is an HTTP error response, the system signals an error to the user and cancels enrollment. A successful response from the server needs to be a JSON object with the following key:

| Key | Type | Content |
| --- | --- | --- |
| `Servers` | Array | (Required) A list of servers the client can choose from. |

Each entry in `Servers` corresponds to a server that supports a different version of the protocol. The client can select the server with the most-recent version that matches its own most-recent supported version. For the current release, this array needs to contain a single item. The `Servers` array items are JSON objects with the following keys:

| Key | Type | Content |
| --- | --- | --- |
| `Version` | String | (Required) The server’s version string. |
| `BaseURL` | String | (Required) The URL where the enrollment takes place. |

The `Version` key indicates the type of enrollment the device needs to perform, and can be one of the following values:

| Value | Description |
| --- | --- |
| mdm-byod | Indicates a user enrollment. |
| mdm-adde | Indicates a device enrollment. |

##### Attempt the First Enrollment

In step 4, the client sends an `HTTP POST` request to the URL that the server specifies in the `BaseURL` property the client extracts from the well-known response JSON document. The request body is a cryptographically signed property list with the following keys:

| Key | Type | Content |
| --- | --- | --- |
| `LANGUAGE` | String | The currently selected system language, such as `en`. |
| `PRODUCT` | String | The device product type, such as `iPhone17,2`. |
| `VERSION` | String | The device operating system build version, such as `23A300`. |

The device uses its built-in identity certificate to sign the request body.

An example HTTP request:

```other
<<<<< Request
POST /enroll/byod HTTP/1.1
Host: mdmserver.example.com
Content-Type: application/xml
Content-Length: 327

<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>LANGUAGE</key>
    <string>en-US</string>
    <key>PRODUCT</key>
    <string>iPhone17,2</string>
    <key>VERSION</key>
    <string>19A240</string>
</dict>
</plist>

>>>>> Response
HTTP/1.1 401 Unauthorized
Content-Length: 0
WWW-Authenticate: Bearer method="apple-as-web", url="https://mdmserver.example.com/authenticate"
```

##### Return the 401 Response

In step 5, the server returns an HTTP 401 response status to the client and includes a `WWW-Authenticate` response header. This response header needs to use the `Bearer` scheme and include the following parameters:

| Key | Type | Content |
| --- | --- | --- |
| `method` | String | (Required) The server’s method string. Needs to be `apple-as-web`. |
| `url` | String | (Required) The URL where the authentication starts. |

The `method` parameter indicates the type of authentication protocol (`apple-as-web`), which selects an [`ASWebAuthenticationSession`](https://developer.apple.com/documentation/AuthenticationServices/ASWebAuthenticationSession) simple authentication protocol flow.

When the `method` is `apple-as-web`, the `url` parameter needs to be present, which indicates the URL of the initial [`ASWebAuthenticationSession`](https://developer.apple.com/documentation/AuthenticationServices/ASWebAuthenticationSession) HTTP request. The URL scheme needs to be either `http` or `https`, and `https` is recommended for improved security.

```other
WWW-Authenticate: Bearer method="apple-as-web",
    url="https://mdmserver.example.com/authenticate"
```

If the client’s enrollment request is invalid, the server returns a standard HTTP error response code (for example, 400 or 403) to halt the enrollment flow on the device. If the server’s response is invalid (for example, missing the `WWW-Authenticate` response header), the system cancels the enrollment.

##### Implement the Authentication Flow

In steps 6–10, the client adds a query item to the web-auth URL with the name `user-identifier`, and sets the value to the user account identifier that the person enters. The client creates an [`ASWebAuthenticationSession`](https://developer.apple.com/documentation/AuthenticationServices/ASWebAuthenticationSession) using the web-auth URL and a callback scheme that it sets to `apple-remotemanagement-user-login`, and then starts the session.

![A sequence diagram showing interactions 6-11 between the user, client, server, and Apple servers for simple authentication.](https://docs-assets.developer.apple.com/published/be55f211bba11bab44eff9ec91bf8764/media-4091469%402x.png)

The [`ASWebAuthenticationSession`](https://developer.apple.com/documentation/AuthenticationServices/ASWebAuthenticationSession) performs an `HTTPS GET` request for the web-auth URL, and presents the resulting HTML data to the user in a web view. A simple HTML sign-in page might contain a form with a user ID and password entry, OK and Cancel buttons, optional terms and conditions, optional branding, and so on.

The MDM server responding to the request can prepopulate any user ID form field by extracting the relevant items from the web-auth URL’s `user-identifier` query item. The server can also use that query item to customize the form based on the user name or domain portions of the user account identifier.

Your MDM server might use an internal identity provider (IdP), or a third-party IdP to authenticate users. If your server uses a third-party IdP, the web-auth URL request can redirect the client’s web view to the third-party IdP sign-in site to perform user authentication. [`ASWebAuthenticationSession`](https://developer.apple.com/documentation/AuthenticationServices/ASWebAuthenticationSession) supports most types of browser-based single sign-on, multifactor, or federated authentication. There can be several round trips between the client and the IdP site before completing authentication.

The user has the option of canceling out of the web view at any time, which terminates the authentication flow and the enrollment.

```swift
<<<<< Request
GET /authenticate?user-identifier=user01@example.com HTTP/1.1
Host: mdmserver.example.com

>>>>> Response
HTTP/1.1 200 OK
Content-Type: text/html; charset="utf-8"
Content-Length: 17643

<!DOCTYPE html>
<html>
…
</html>
```

##### Return the Authentication Result

In step 11, the [`ASWebAuthenticationSession`](https://developer.apple.com/documentation/AuthenticationServices/ASWebAuthenticationSession) web flow completes when the server returns an HTTP 308 permanent redirect response to the client, with a `Location` header that it sets to a URL with a scheme of `apple-remotemanagement-user-login` (the authentication session callback URL scheme). The URL needs to have a network location component of `authentication-results`. The URL needs to include an `access-token` query item with a value that is the access token. The client securely stores the access token for use when authorizing subsequent requests to the server. The server can define the format of the access token — the client treats it as an opaque token. This may be a token that the server itself generates, or one that the IdP generates.

```other
<<<<< Request
POST /authenticate-results HTTP/1.1
Content-Type: multipart/form-data; boundary=----WebKitFormBoundarySaBDj3Bd7BeKC1s2
Content-Length: 236

------WebKitFormBoundarySaBDj3Bd7BeKC1s2
Content-Disposition: form-data; name="username"

user01
------WebKitFormBoundarySaBDj3Bd7BeKC1s2
Content-Disposition: form-data; name="password"

secret
------WebKitFormBoundarySaBDj3Bd7BeKC1s2--

>>>>> Response
HTTP/1.1 308 Permanent Redirect
Content-Length: 0
Location: apple-remotemanagement-user-login://authentication-results?access-token=dXNlci1pZGVudGl0eQ
```

If authentication fails, the server returns an appropriate HTTP error response code that terminates the enrollment on the device.

##### Attempt the Second Enrollment

In step 12, the client repeats the HTTP POST request it makes in the first enrollment attempt, using the same request body. However, this time it also includes an `Authorization HTTP` request header. This header needs to use the `Bearer` scheme and include the access token that the client retrieves from the authentication session flow.

![A sequence diagram showing interactions 12-20 between the user, client, server, and Apple servers for simple authentication.](https://docs-assets.developer.apple.com/published/0d9a9bb4703ca84da712f9b77ec825d1/media-4091470%402x.png)

When the server processes the HTTP request, it authorizes the request by verifying the validity of the access token in the `Authorization HTTP` request header. If the access token is invalid, or the header isn’t present or has incorrect values, the server needs to reject the request with a suitable HTTP error response status. If the access token is valid, the server returns an `HTTP 200 OK` response with a response body containing the MDM enrollment profile that the client uses to enroll with the MDM server.

Because the server knows who the user is at this point, it can customize the enrollment profile for any per-user behavior. For example, if different sets of users are on different MDM servers within an organization, the enrollment profile for each user needs to match their assigned MDM server.

```other
<<<<< Request
POST /enroll/byod HTTP/1.1
Host: mdmserver.example.com
Content-Type: application/x-www-form-urlencoded
Content-Length: 326
Authorization: Bearer dXNlci1pZGVudGl0eQ

<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>LANGUAGE</key>
    <string>en-US</string>
    <key>PRODUCT</key>
    <string>iPhone17,2</string>
    <key>VERSION</key>
    <string>19A240</string>
</dict>
</plist>

>>>>> Response
HTTP/1.1 200 OK
Content-Type: application/x-apple-aspen-config
Content-Length: 6785

<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>PayloadType</key>
    <string>Configuration</string>
   …
    <key>PayloadContent</key>
    <array>
        <dict>
            <key>PayloadType</key>
            <string>com.apple.security.scep</string>
            …
        </dict>
        <dict>
            <key>PayloadType</key>
            <string>com.apple.mdm</string>
            …
            <key>AssignedManagedAppleID</key>
            <string>user01@appleid.example.com</string>
            <key>EnrollmentMode</key>
            <string>BYOD</string>
        </dict>
    </array>
</dict>
</plist>
```

> **Note**:  Ensure that the `AccessRights` key isn’t present in the `com.apple.mdm` payload.

##### Validate the Enrollment Profile

In step 13, the [`MDM`](mdm.md) profile that the server delivers in the second enrollment attempt needs to include the following keys:

| Key | Type | Content |
| --- | --- | --- |
| `EnrollmentMode` | String | `BYOD` for user enrollment or `ADDE` for device enrollment. |
| `AssignedManagedAppleID` | String | The user’s Managed Apple Account. |

The `EnrollmentMode` key indicates to the client the type of enrollment the server requires. If this key is missing or has an incorrect value, the client cancels the enrollment.

The `AssignedManagedAppleID` key in the MDM enrollment profile provides the Managed Apple Account of the authenticated user to the client. If this key is missing or has an invalid value, the client cancels the enrollment. The server needs to maintain the mapping between the user identifier that starts the enrollment flow and the assigned Managed Apple Account associated with that user. For federated Managed Apple Accounts, the two identifiers are the same.

If `EnrollmentMode` is `BYOD` in the MDM enrollment profile, the `AccessRights` key can’t be present. MDM servers can’t declare access rights when using the simple enrollment mode because user enrollments have a fixed set of access rights rules for MDM commands and profile payloads. If the key is present, the client cancels the enrollment.

##### Sign in to the Managed Apple Account

In steps 14–18, after a device receives a valid enrollment profile, but before MDM enrollment actually takes place, the client creates a data-separated volume to store MDM-related managed data. The device then prompts the user to sign in to their Managed Apple Account.

If the sign-in fails, the client cancels the enrollment flow. If the sign-in succeeds, the device creates the iCloud and iTunes accounts associated with the Managed Apple Account, and then the client continues with the MDM enrollment.

##### Finish the Enrollment

In step 19, when all management setup steps are complete, the device proceeds with the actual MDM enrollment. It installs the MDM enrollment profile, performing any certificate enrollment steps, and then starting the MDM protocol flow by issuing an [`Authenticate`](authenticate.md) request. All requests to the MDM server include an `Authorization` HTTP request header with the access token as described in the “Attempt the second enrollment” section above.

## See Also

- [Implementing the OAuth 2 authentication account-driven enrollment flow](implementing-the-oauth2-authentication-user-enrollment-flow.md)
  Examine the steps between the user, client, server, and Apple services in the OAuth 2 flow.
- [Implementing the Enrollment SSO flow](implementing-the-enrollment-sso-flow.md)
  Examine the steps between the user, client, and server in the Enrollment SSO flow.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/implementing-the-simple-authentication-user-enrollment-flow)*
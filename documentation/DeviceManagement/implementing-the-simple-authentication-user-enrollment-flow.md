# Implementing the simple authentication user-enrollment flow

**Framework**: Devicemanagement

Understand the steps of the authentication flow between the user, client, server, and Apple services.

#### Overview

To implement user enrollment, you need to support a series of interactions between the user’s device and your MDM server. The diagrams below illustrates the interactions and the sections below detail each of the interaction steps.

![A sequence diagram showing the first 5 interactions between the user, client, server, and Apple servers for simple authentication.](https://docs-assets.developer.apple.com/published/0d3c28bcc45f65cb5210f9635b1a95a6/media-4091468%402x.png)

##### Sign in

In step 1 above, the user enters a user account identifier to start the MDM enrollment flow. The identifier needs to conform to a  format, where  is a user identifier, and  is a fully qualified domain name (FQDN) corresponding to a domain that advertises the MDM service for the user’s organization. The client splits the supplied identifier at the last occurrence of the @ character. If the resulting components are invalid (for example, empty, or not an FQDN), then an error occurs, and the user can re-enter a valid identifier to proceed or cancel the enrollment.

##### Well Known Request

In step 2 above, the client sends an `HTTPS GET` request for the URL `https://<domain>/.well-known/com.apple.remotemanagement` (where `<domain>` is the domain/FQDN portion of the user identifier extracted in the previous step). The client includes two query parameters in the URL path:

- `user-identifier` - the value of the user account identifier entered in step 1 above.
- `model-family` - the device’s model family (for example, iPhone, iPad, Mac).

The server uses these values to help determine whether a user or device enrollment should be done, or which MDM server the device should enroll with (for example, the system can assign different sets of users to different MDM servers within the organization, so the response for each user matches their assigned MDM server).

##### Mdm Url

In step 3 above, the server returns a JSON document that conforms to the schema defined here. The client extracts the `BaseURL` property in the first JSON array object and uses it in subsequent requests. If the response is malformed, or an HTTP error response is returned, the system signals an error to the user and cancels enrollment. A successful response from the server must be a JSON object with the following keys:

| Key | Type | Content |
| --- | --- | --- |
| `Servers` | Array | Required. A list of servers the client can choose from. |

Each entry in `Servers` corresponds to a server that supports a different version of the protocol. The client can pick the server with the most recent version that matches its own most recent supported version. For the current release, this array needs to contain a single item. The `Servers` array items are JSON objects with the following keys:

| Key | Type | Content |
| --- | --- | --- |
| `Version` | String | Required. The server’s version string. Must be `mdm-byod`. |
| `BaseURL` | String | Required. The URL where the enrollment takes place. |

##### First Enrollment Attempt

In step 4 above, the client sends an `HTTP POST` request to the URL that the server specified in the `BaseURL` property the client extracts from the well-known response JSON document. The request body is a cryptographically signed property list with the following keys:

| Key | Type | Content |
| --- | --- | --- |
| `LANGUAGE` | String | The currently selected system language, such as `en` |
| `PRODUCT` | String | The device product type, such as `iPhone10,2` |
| `VERSION` | String | The device operating system build version, such as `19A240`. |

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
    <string>iPhone10,2</string>
    <key>VERSION</key>
    <string>19A240</string>
</dict>
</plist>

>>>>> Response
HTTP/1.1 401 Unauthorized
Content-Length: 0
WWW-Authenticate: Bearer method="apple-as-web", url="https://mdmserver.example.com/authenticate"
```

##### 401 Response

In step 5 above, the server returns an HTTP 401 response status to the client and includes a `WWW-Authenticate` response header. This response header must use the `Bearer` scheme and include the following parameters:

| Key | Type | Content |
| --- | --- | --- |
| `method` | String | Required. The server’s method string. Needs to be `apple-as-web`. |
| `url` | String | Required. The URL where the authentication starts. |

The `method` parameter indicates what type of authentication protocol that in this case is `apple-as-web`, which selects an [`ASWebAuthenticationSession`](https://developer.apple.com/documentation/AuthenticationServices/ASWebAuthenticationSession) simple authentication protocol flow.

The `url` parameter needs to be present when the `method` is `apple-as-web`, and this indicates the URL of the initial [`ASWebAuthenticationSession`](https://developer.apple.com/documentation/AuthenticationServices/ASWebAuthenticationSession) HTTP request. The URL scheme needs to be either `http` or `https`, and `https` is recommended improve security.

```other
WWW-Authenticate: Bearer method="apple-as-web",
    url="https://mdmserver.example.com/authenticate"
```

If the client’s enrollment request is invalid, the server returns a standard HTTP error response code (for example, 400 or 403) to halt the enrollment flow on the device. If the server’s response is invalid (for example, missing the `WWW-Authenticate` response header), then the system cancels the enrollment.

![A sequence diagram showing interactions 6-11 between the user, client, server, and Apple servers for simple authentication.](https://docs-assets.developer.apple.com/published/be55f211bba11bab44eff9ec91bf8764/media-4091469%402x.png)

##### Authentication Flow

In steps 6-10 above, the client adds a query item to the web-auth URL, with the name `user-identifier`, and value set to the user account identifier entered by the user. The client creates an [`ASWebAuthenticationSession`](https://developer.apple.com/documentation/AuthenticationServices/ASWebAuthenticationSession) using the web-auth URL and a callback scheme set to `apple-remotemanagement-user-login`, and starts the session.

The [`ASWebAuthenticationSession`](https://developer.apple.com/documentation/AuthenticationServices/ASWebAuthenticationSession) does an `HTTPS GET` request for the web-auth URL, and presents the resulting HTML data to the user in a web view. A simple HTML sign-in page might contain a form with a user id and password entry, OK and Cancel buttons, optional terms and conditions, optional branding, and so on.

The MDM server responding to the request can pre-populate any user id form field by extracting the relevant items from the web-auth URL’s `user-identifier` query item. The server can also use that query item to customize the form based on the user name or domain portions of the user account identifier.

Your MDM server might use an internal identity provider (IdP), or a 3rd party IdP to authenticate users. If your server uses a 3rd party IdP, the web-auth URL request can redirect the client’s web-view to the 3rd party IdP login site to carry out user authentication. [`ASWebAuthenticationSession`](https://developer.apple.com/documentation/AuthenticationServices/ASWebAuthenticationSession) supports most types of browser based single sign-on, multi-factor, or federated authentication. There can be several round trips between the client and the IdP site required to complete authentication.

The user has the option of canceling out of the web-view at any time, and that terminates the authentication flow and the enrollment.

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

##### Authentication Result

In step 11 above, the [`ASWebAuthenticationSession`](https://developer.apple.com/documentation/AuthenticationServices/ASWebAuthenticationSession) web flow completes when the server returns an HTTP 308 permanent redirect response to the client, with a `Location` header set to a URL whose scheme is `apple-remotemanagement-user-login` (the authentication session callback URL scheme). The URL must have a network location component set to `authentication-results`. The URL must include an `access-token` query item, whose value is the access token. The client securely stores the access token for use when authorizing subsequent requests to the server. The server is free to define the format of the access token - the client treats it as an opaque token. This may be a token that the server itself generates, or one generated by the IdP.

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

![A sequence diagram showing interactions 12-20 between the user, client, server, and Apple servers for simple authentication.](https://docs-assets.developer.apple.com/published/0d9a9bb4703ca84da712f9b77ec825d1/media-4091470%402x.png)

##### Second Enrollment Attempt

In step 12 above, the client repeats the HTTP POST request it previously made in the first enrollment attempt, using the same request body. However, this time it also includes an `Authorization HTTP` request header. This header must use the `Bearer` scheme and include the access token retrieved from the authentication session flow.

When the server processes the HTTP request, it authorizes the request by verifying the validity of the access token provided in the `Authorization HTTP` request header. If the access token is invalid, or the header isn’t present, or has incorrect values, the server must reject the request with a suitable HTTP error response status. If the access token is valid, the server returns an `HTTP 200 OK` response with a response body containing the MDM enrollment profile that the client uses to enroll with the MDM server.

Because the server knows who the user is at this point, it can customize the enrollment profile for any per-user behavior, for example, if different sets of users are on different MDM servers within the organization, the enrollment profile for each user needs to match their assigned MDM server.

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
    <string>iPhone10,2</string>
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

> **Note**:  The `AccessRights` key must not be present in the `com.apple.mdm` payload.

##### Enrollment Profile

In step 13 above, the MDM profile delivered by the server in the second enrollment attempt must include the following keys:

| Key | Type | Content |
| --- | --- | --- |
| `EnrollmentMode` | String | Set to `BYOD` for user enrollment and `ADDE` for device enrollment. |
| `AssignedManagedAppleID` | String | The user’s Managed Apple ID. |

The `EnrollmentMode` key indicates to the client the type of enrollment the server expects. If this key is missing, or has an incorrect value, the client cancels the enrollment.

The `AssignedManagedAppleID` key in the MDM enrollment profile provides the Managed AppleID of the authenticated user to the client. If this key is missing, or has an invalid value, the client cancels the enrollment. The server needs to maintain the mapping between the user identifier used to start the enrollment flow, and the assigned Managed AppleID associated with that user. For federated Managed Apple IDs, the two identifiers are the same.

If `EnrollmentMode` is `BYOD` in the MDM enrollment profile, then the `AccessRights` key must not be present. MDM servers can’t declare access rights when using the new enrollment mode, as user enrollments have a fixed set of access rights rules for MDM commands and profile payloads. If the key is present, the client cancels the enrollment.

##### Maid Sign in

In steps 14-18 above, after a device receives a valid enrollment profile, but before MDM enrollment actually takes place, the client creates a data separated volume to store MDM related managed data. The device then prompts the user to login to their Managed Apple ID.

If the AppleID login fails, the client cancels the enrollment flow. If the AppleID login succeeds, the device creates the iCloud and iTunes accounts associated with the Apple ID, and then the client continues with the MDM enrollment.

##### Enroll

In step 19 above, once all management setup steps are complete, the device proceeds with the actual MDM enrollment. It installs the MDM enrollment profile, carrying out any certificate enrollment steps, and then starting the MDM protocol flow by issuing an `Authenticate` CheckIn request. All requests to the MDM server include an `Authorization` HTTP request header with the access token as described in the second enrollment attempt section above.

## See Also

- [Implementing the OAuth2 authentication user-enrollment flow](implementing-the-oauth2-authentication-user-enrollment-flow.md)
  Understand the steps of the OAuth2 flow between the user, client, server, and Apple services.


---

*[View on Apple Developer](https://developer.apple.com/documentation/DeviceManagement/implementing-the-simple-authentication-user-enrollment-flow)*
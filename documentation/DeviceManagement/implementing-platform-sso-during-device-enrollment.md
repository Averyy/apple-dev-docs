# Implementing Platform SSO during device enrollment

**Framework**: Device Management

Streamline device enrollment by using Platform SSO.

#### Overview

A device management service can configure a macOS device to use Platform SSO during setup after the administrator registers the device with the Automated Device Enrollment program. This streamlines the enrollment process and enforces Platform SSO registration to enable single sign-on access to apps and websites.

#### Implement the Platform Sso Flow

When the Automated Device Enrollment [`Profile`](profile.md) for a device indicates that it needs to enroll during initial setup, the device posts a request to the enrollment URL and includes the [`MachineInfo`](machineinfo.md) details in the request body. If the device is capable of supporting Platform SSO during enrollment, the [`MachineInfo`](machineinfo.md) details include an `MDM_CAN_REQUEST_PSSO_CONFIG` key with a value of `true`.

When the device management service detects a device capable of using Platform SSO during enrollment, it returns an [`ErrorCodePlatformSSORequired`](errorcodeplatformssorequired.md) 403 error response to the device. That response contains the details that allow the device to configure Platform SSO and trigger an initial authentication with the organization’s identity provider.

After the initial authentication completes successfully, the device resends the enrollment URL request and includes the [`MachineInfo`](machineinfo.md) details again. However, this time, the [`MachineInfo`](machineinfo.md) details don’t contain the `MDM_CAN_REQUEST_PSSO_CONFIG` key. The device also includes an `Authorization` HTTP request header and sets its value to include a `Bearer` token key containing an identity provider authorization token for the user. When the device management service verifies the authorization token, it delivers the enrollment profile to the device to trigger enrollment.

The device then proceeds through `Setup Assistant` and automatically creates a local user account that it configures with the Platform SSO details, so that users can sign in to that account using the identity provider credentials.

The complete set of steps for the Platform SSO during enrollment flow are:

1. Post a `MACHINEINFO` request with a PSSO indicator.
2. Detect PSSO support for the device.
3. Return the required 403 PSSO error response.
4. Fetch the [`ExtensibleSingleSignOn`](extensiblesinglesignon.md) profile.
5. Return the [`ExtensibleSingleSignOn`](extensiblesinglesignon.md) profile.
6. Install the [`ExtensibleSingleSignOn`](extensiblesinglesignon.md) profile.
7. Fetch the package.
8. Return the package.
9. Install the package.
10. Create a web view for `AuthURL`.
11. Present the sign-in view to the user.
12. Return an HTTP 308 redirect response.
13. Authenticate the user.
14. Post a `MACHINEINFO` request with the bearer token.
15. Verify the bearer token.
16. Return the enrollment profile.
17. Enroll with the device management service.

The following sections describe the details of each step.

##### Send the Initial Request

In step 1, the device posts a request to the enrollment URL and includes the [`MachineInfo`](machineinfo.md) details with an `MDM_CAN_REQUEST_PSSO_CONFIG` key with a value of `true` in the request body.

A sample HTTP request:

```plist
<<<<< Request
POST /enroll HTTP/1.1
Host: mdmserver.example.com
Content-Type: application/xml
Content-Length: 500

<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>UDID</key>
    <string>0000-1111-2222</string>
    <key>SERIAL</key>
    <string>ABCD1234</string>
    <key>PRODUCT</key>
    <string>MacBookPro18,2</string>
    <key>VERSION</key>
    <string>25A300</string>
    <key>OS_VERSION</key>
    <string>16.0</string>
    <key>MDM_CAN_REQUEST_PSSO_CONFIG</key>
    <true/>
</dict>
</plist>
```

##### Process the Platform Sso Required Response

In step 2, the device management service detects that a device that supports Platform SSO during enrollment is trying to enroll.

In step 3, the device management service returns an [`ErrorCodePlatformSSORequired`](errorcodeplatformssorequired.md) 403 error response to the device. The 403 error response is a JSON object that contains a `Code` key with a value of `com.apple.psso.required`, and a `Details` object with the following keys:

| Key | Type | Content |
| --- | --- | --- |
| `ProfileURL` | String | The URL of a configuration profile containing an [`ExtensibleSingleSignOn`](extensiblesinglesignon.md) profile payload for configuring the SSO extension for Platform SSO. |
| `Package` | Object | A dictionary for the package that installs an app with the SSO app extension for Platform SSO. |
| `AuthURL` | String | The URL the device uses to trigger Platform SSO authentication after it installs the configuration profile and app. |

The `Package` key contains a JSON object with the following keys:

| Key | Type | Content |
| --- | --- | --- |
| `ManifestURL` | String | The URL of the manifest document that specifies the package to install. |
| `PinningCerts` | Array of strings | An array of DER-encoded certificates to pin to the connection when fetching the manifest document. The certificate data values are Base64-encoded strings. |
| `PinningRevocationCheckRequired` | Boolean | If `true`, certificate revocation checks require a positive response when using certificate pinning with `PinningCerts`. |

A sample HTTP response:

```plist
>>>>> Response
HTTP/1.1 403 Forbidden
Content-Type: application/xml
Content-Length: 601

<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>Code</key>
    <string>com.apple.psso.required</string>
    <key>Details</key>
    <dict>
        <key>ProfileURL</key>
        <string>https://mdmserver.example.com/psso.mobileconfig</string>
        <key>Package</key>
        <dict>
            <key>ManifestURL</key>
            <string>https://mdmserver.example.com/psso-app.plist</string>
        </dict>
        <key>AuthURL</key>
        <string>https://idp.example.com/authenticate</string>
    </dict>
</dict>
</plist>
```

##### Set Up Platform Sso

After receiving the error response, the device sets up Platform SSO as follows:

1. It downloads the configuration profile that the `ProfileURL` key specifies (steps 4 and 5). The profile needs to contain an [`ExtensibleSingleSignOn`](extensiblesinglesignon.md) profile payload with a configuration to implement Platform SSO using the SSO extension that the package delivers.
2. It installs the configuration profile (step 6).
3. It downloads the manifest document that the `Package` key specifies, and installs the package that the manifest document specifies (steps 7 and 8). The package needs to contain an app that includes the SSO extension for Platform SSO.
4. It installs the package (step 9). This installs the app and its SSO extension on the device.

If any of the above steps fail, the device displays an error alert to the user and cycles back to a state that allows the user to try signing in again.

> ❗ **Important**:  The package needs to install the app containing the SSO extension into the `/Applications` folder to ensure the device management service is managing the app.

##### Authenticate the User

The device creates an [`ASWebAuthenticationSession`](https://developer.apple.com/documentation/AuthenticationServices/ASWebAuthenticationSession) using `AuthURL` and a callback scheme that it sets to `apple-remotemanagement-user-login` (step 10). This starts an authentication flow with the organization’s identity provider.

The [`ASWebAuthenticationSession`](https://developer.apple.com/documentation/AuthenticationServices/ASWebAuthenticationSession) performs an HTTPS GET request for the web-auth URL and presents the resulting HTML data to the user in a web view for sign-in (step 11). A simple HTML sign-in page can contain a form with text entry fields for a user ID and password, OK and Cancel buttons, optional terms and conditions, optional branding, and so on.

The user can opt to cancel out of the web view at any time, which terminates the authentication flow and the enrollment.

A sample HTTP request and response:

```html
<<<<< Request
GET /authenticate HTTP/1.1
Host: idp.example.com

>>>>> Response
HTTP/1.1 200 OK
Content-Type: text/html; charset="utf-8"
Content-Length: 17643

<!DOCTYPE html>
<html>
…
</html>
```

##### Process the User Authentication Result

The [`ASWebAuthenticationSession`](https://developer.apple.com/documentation/AuthenticationServices/ASWebAuthenticationSession) web flow completes when the device management service returns an HTTP 308 permanent redirect response to the device (step 12), with a `Location` header that the service sets to a URL with a scheme of `apple-remotemanagement-user-login` (the authentication session callback URL scheme). The service sets the network location component of the URL to `authentication-results`. It includes an `access-token` query item in the URL and sets its value to the identity provider authorization token. The identity provider controls the format of the authorization token, so the device treats it as an opaque token.

A sample HTTP response:

```other
>>>>> Response
HTTP/1.1 308 Permanent Redirect
Content-Length: 0
Location: apple-remotemanagement-user-login://authentication-results?access-token=dXNlci1pZGVudGl0eQ
```

The device management service verifies the access token to determine whether authentication succeeds (step 13). If authentication fails, the service returns an appropriate HTTP error response code that terminates the enrollment on the device.

##### Enroll the Device

After authentication with the identity provider is complete, the device posts a request to the enrollment URL and includes the [`MachineInfo`](machineinfo.md) details without an `MDM_CAN_REQUEST_PSSO_CONFIG` key in the request body (step 14). The request includes an `Authorization` HTTP header with a `Bearer` key that the device sets to the authorization token that the identity provider returns.

The device management service verifies the authorization token (step 15), and if that succeeds, it responds to the request by returning the [`MDM`](mdm.md) enrollment profile (step 16), which the device uses to enroll (step 17).

A sample HTTP request and response:

```plist
<<<<< Request
POST /enroll HTTP/1.1
Host: mdmserver.example.com
Content-Type: application/xml
Content-Length: 500
Authorization: Bearer dXNlci1pZGVudGl0eQ

<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>UDID</key>
    <string>0000-1111-2222</string>
    <key>SERIAL</key>
    <string>ABCD1234</string>
    <key>PRODUCT</key>
    <string>MacBookPro18,2</string>
    <key>VERSION</key>
    <string>25A300</string>
    <key>OS_VERSION</key>
    <string>16.0</string>
</dict>
</plist>

>>>>> Response
HTTP/1.1 200 OK
Content-Type: application/x-apple-aspen-config
Content-Length: nnn

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
            <string>com.apple.mdm</string>
            …
        </dict>
    </array>
</dict>
</plist>
```

##### Manage the Device

After enrollment, the device management service manages the device, which has a configuration for Platform SSO. The SSO app and configuration profile persist on the device and remain managed.

## See Also

- [Implementing Platform SSO for unattended device enrollment](implementing-platform-sso-for-unattended-device-enrollment.md)
  Configure and enroll unattended devices by using Platform SSO.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/implementing-platform-sso-during-device-enrollment)*
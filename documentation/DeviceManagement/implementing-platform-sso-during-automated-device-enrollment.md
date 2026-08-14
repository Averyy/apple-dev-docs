# Implementing Platform SSO during Automated Device Enrollment

**Framework**: Device Management

Streamline authentication during Automated Device Enrollment with Platform SSO.

#### Overview

A device management service can configure a Mac to use Platform SSO during setup after the administrator registers the device for Automated Device Enrollment. This streamlines the enrollment process and enforces Platform SSO registration to provide single sign-on access to apps and websites.

#### Implement the Platform Sso Flow

When the Automated Device Enrollment [`Profile`](profile.md) for a device indicates that it needs to enroll during initial setup, the device posts a request to the enrollment URL and includes the [`MachineInfo`](machineinfo.md) details in the request body. If the device is capable of supporting Platform SSO during enrollment, the [`MachineInfo`](machineinfo.md) details include an `MDM_CAN_REQUEST_PSSO_CONFIG` key with a value of `true`.

When the device management service detects a device capable of using Platform SSO during enrollment, it returns an [`ErrorCodePlatformSSORequired`](errorcodeplatformssorequired.md) `403` error response to the device. That response contains the details that allow the device to configure Platform SSO and initiate an initial authentication with the organization’s identity provider.

After the initial authentication completes successfully, the device resends the enrollment URL request and includes the [`MachineInfo`](machineinfo.md) details again. However, this time, the [`MachineInfo`](machineinfo.md) details don’t contain the `MDM_CAN_REQUEST_PSSO_CONFIG` key. The device also includes an `Authorization` HTTP request header and sets its value to include a `Bearer` token key containing an identity provider authorization token for the user. When the device management service verifies the authorization token, it delivers the device management (MDM) enrollment profile to the device to start the enrollment.

The device then proceeds through Setup Assistant and automatically creates a local user account that it configures with the Platform SSO details so people can sign in to that account using the identity provider credentials.

The complete set of steps for the Platform SSO during enrollment flow are:

1. The device requests the enrollment by posting a `MACHINEINFO` request with a PSSO indicator.
2. The device management service returns a `403` error that includes the details needed to set up and configure Platform SSO.
3. The device downloads and installs the [`ExtensibleSingleSignOn`](extensiblesinglesignon.md) profile and the package specified in the response. The package needs to contain an app that includes the SSO extension for Platform SSO.
4. The device starts an authentication flow with the organization’s identity provider using the `AuthURL` specified in the `403` response and prompts the user to authenticate. If authentication is successful, the device receives an authorization token and an HTTP `308` redirect response.
5. The device posts another `MACHINEINFO` request and includes the authorization token. If authorization is successful, the device management service returns the enrollment profile.
6. The device enrolls and creates a local user account based on information from the identity provider.

![A diagram showing the 6 steps to use Platform SSO during Automated Device Enrollment](/images/com.apple.devicemanagement/implementing-platform-sso-during-automated-device-enrollment@2x.png)

The following sections describe the details of each step.

> **Note**:  The described flow enables authenticating the enrollment using tokens provided by Platform SSO. Alternatively, you can use the  `await_device_configured` flag to keep the device in Setup Assistant while installing the Platform SSO extension and required configuration.

#### Requesting the Enrollment

In step 1, the device posts an HTTP request to the enrollment URL specified in the Automated Device Enrollment [`Profile`](profile.md) and includes the [`MachineInfo`](machineinfo.md) details with an `MDM_CAN_REQUEST_PSSO_CONFIG` key with a value of `true` in the request body.

The following is a sample HTTP request:

```plist
<<<<< Request
POST /enroll HTTP/1.1
Host: devicemanagement.example.com
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
    <string>27.0</string>
    <key>MDM_CAN_REQUEST_PSSO_CONFIG</key>
    <true/>
</dict>
</plist>
```

#### Process the Platform Sso Required Response

In step 2, the device management service detects that a device that supports Platform SSO during enrollment is trying to enroll and returns an [`ErrorCodePlatformSSORequired`](errorcodeplatformssorequired.md) `403` error response to the device. The `403` error response is a JSON object that contains a `Code` key with a value of `com.apple.psso.required`, and a `Details` object with the following keys:

| Key | Type | Content |
| --- | --- | --- |
| `ProfileURL` | String | **(Required)** The URL of a configuration profile containing an [`ExtensibleSingleSignOn`](extensiblesinglesignon.md) profile payload for configuring the SSO extension for Platform SSO. |
| `Package` | Object | **(Required)** A dictionary for the signed package that installs an app with the SSO app extension for Platform SSO. |
| `AuthURL` | String | **(Required)** The URL the device uses to start Platform SSO authentication after it installs the configuration profile and app. |

The `Package` key contains a JSON object with the following keys:

| Key | Type | Content |
| --- | --- | --- |
| `ManifestURL` | String | **(Required)** The URL of the manifest document that specifies the package to install. |
| `PinningCerts` | Array of strings | **(Optional)** An array of DER-encoded certificates to pin to the connection when fetching the manifest document. The certificate data values are `Base64-encoded strings. |
| `PinningRevocationCheckRequired` | Boolean | **(Optional)** If `true`, certificate revocation checks require a positive response when using certificate pinning with `PinningCerts`. |

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
    <key>code</key>
    <string>com.apple.psso.required</string>
    <key>details</key>
    <dict>
        <key>ProfileURL</key>
        <string>https://devicemanagement.example.com/psso.mobileconfig</string>
        <key>Package</key>
        <dict>
            <key>ManifestURL</key>
            <string>https://devicemanagement.example.com/psso-app.plist</string>
        </dict>
        <key>AuthURL</key>
        <string>https://idp.example.com/authenticate</string>
    </dict>
</dict>
</plist>
```

> ❗ **Important**:  To enforce a minimum operating system version, your device management service needs to provide the [`ErrorCodeSoftwareUpdateRequired`](errorcodesoftwareupdaterequired.md) `403`  error in its first response. After the version provided in the [`MachineInfo`](machineinfo.md) shows the required operating system version, return the [`ErrorCodePlatformSSORequired`](errorcodeplatformssorequired.md) `403` error response the next time the device requests enrollment.

#### Set Up Platform Sso

To set up Platform SSO after receiving the error response, the device:

1. Downloads the configuration profile that the `ProfileURL` key specifies (see step 3 in the figure, above). The profile needs to contain an [`ExtensibleSingleSignOn`](extensiblesinglesignon.md) profile payload with a [`ExtensibleSingleSignOn.PlatformSSO`](extensiblesinglesignon/platformsso-data.dictionary.md) object to configure Platform SSO using the SSO extension that the package delivers. The payload must contain at least the `EnableRegistrationDuringSetup` key set to `true`.
2. Installs the configuration profile.
3. Downloads the manifest document that the `Package` key specifies, and installs the package that the manifest document specifies. The package needs to contain an app that includes the SSO extension for Platform SSO.
4. Installs the package. This installs the app and its SSO extension on the device.

> ❗ **Important**:  Sign the package with a certificate the device can verify at this stage. This can be a certificate, with a trust chain rooted in a Certificate Authority within the built-in trust store or provided by a [`CertificateRoot`](certificateroot.md) configuration. If you use a custom root certificate, provide any intermediate certificates required to verify the signature.

If any of the above steps fail, the device displays an error alert to the user and cycles back to a state that allows the user to try signing in again.

> ❗ **Important**:  The package needs to install the app containing the SSO extension into the `/Applications` folder to ensure the device management service is managing the app.

If the Platform SSO extension requires it, combine the following payloads in the same profile together with the [`ExtensibleSingleSignOn`](extensiblesinglesignon.md) payload:

- [`ACMECertificate`](acmecertificate.md)
- [`AssociatedDomains`](associateddomains.md)
- [`CertificatePEM`](certificatepem.md)
- [`CertificatePKCS1`](certificatepkcs1.md)
- [`CertificatePKCS12`](certificatepkcs12.md)
- [`CertificatePreference`](certificatepreference.md)
- [`CertificateRoot`](certificateroot.md)
- [`CertificateTransparency`](certificatetransparency.md)
- [`IdentityPreference`](identitypreference.md)
- [`ManagedPreferences`](managedpreferences.md)
- [`SCEP`](scep.md)

#### Authenticate the User

In step 4, the device creates an [`ASWebAuthenticationSession`](https://developer.apple.com/documentation/authenticationservices/aswebauthenticationsession) using `AuthURL` and a callback scheme that is set to `apple-remotemanagement-user-login`. This starts an authentication flow with the organization’s identity provider.

The [`ASWebAuthenticationSession`](https://developer.apple.com/documentation/authenticationservices/aswebauthenticationsession) performs an HTTPS GET request for the `AuthURL` and presents the resulting HTML data to the user in a web view for sign-in. The sign-in page can contain a form with text entry fields for a user ID and password, OK and Cancel buttons, optional terms and conditions, optional branding, and so on.

The user can opt to cancel out of the web view at any time, which terminates the authentication flow and the enrollment.

The following is a sample HTTP request and response:

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

The [`ASWebAuthenticationSession`](https://developer.apple.com/documentation/authenticationservices/aswebauthenticationsession) web flow completes when the device management service returns an HTTP `308` permanent redirect response to the device, with a `Location` header that the service sets to a URL with a scheme of `apple-remotemanagement-user-login` (the authentication session callback URL scheme). The service sets the network location component of the URL to `authentication-results`.

It includes an `access-token` query item in the URL and sets its value to the identity provider authorization token. The identity provider controls the format of the authorization token, so the device treats it as an opaque token.

A sample HTTP response:

```other
>>>>> Response
HTTP/1.1 308 Permanent Redirect
Content-Length: 0
Location: apple-remotemanagement-user-login://authentication-results?access-token=dXNlci1pZGVudGl0eQ
```

The device management service verifies the access token to determine whether authentication succeeds. If authentication fails, the service returns an appropriate HTTP error response code that terminates the enrollment on the device.

#### Enroll the Device

After completing authentication with the identity provider, the device posts a request (see step 5 in the figure, above) to the enrollment URL and includes the [`MachineInfo`](machineinfo.md) details without an `MDM_CAN_REQUEST_PSSO_CONFIG` key in the request body. The request includes an `Authorization` HTTP header with a `Bearer` key that the device sets to the authorization token that the identity provider returns.

The device management service verifies the authorization token, and if that succeeds, it responds to the request by returning the device management [`MDM`](mdm.md) enrollment profile, which the device uses to enroll.

The following is a sample HTTP request and response:

```plist
<<<<< Request
POST /enroll HTTP/1.1
Host: devicemanagement.example.com
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
    <string>27.0</string>
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

#### Create the Local User Account

The device creates a local account using the information provided by the identity provider.

When `SynchronizeProfilePicture` is set to `true`, the device uses the profile picture provided by the SSO extension for the created account.

## See Also

- [Implementing Platform SSO for unattended device enrollment](implementing-platform-sso-for-unattended-device-enrollment.md)
  Configure and enroll unattended devices with Platform SSO.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/implementing-platform-sso-during-automated-device-enrollment)*
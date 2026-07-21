# Providing information about your device management service

**Framework**: Device Management

Create a service configuration entry point to your device management service to access frequently used information.

#### Overview

Add an unauthenticated HTTPS request entry point to your device management service to make it easier to access useful information about your service. Create the entry point using the endpoint `/MDMServiceConfig`; for example, `https://devicemanagement.example.com/MDMServiceConfig`.

The service should return a UTF-8 JSON-encoded hash (`Content-Type: application/json; charset=UTF8`) with the following values in the body of its response:

- **`dep_anchor_certs_url`**: The URL a device uses to obtain the certificates required to trust the URL specified by the `dep_enrollment_url` key. This value has the same format as the `anchor_certs` value in the Automated Device Enrollment [`Profile`](profile.md), except the body needs to be UTF-8 JSON-encoded for transfer. The decoded body of the response from this URL should be usable in a Automated Device Enrollment [`Profile`](profile.md) profile under the `anchor_certs` key without any modification.

Provide this URL even if your device management service doesn’t require additional certificates because it’s using a trusted SSL certificate. However, provide either an empty body (`Content-Length: 0`) or an empty array JSON string (`'[]'`) .

- **`dep_enrollment_url`**: The URL a device uses to begin device enrollment with the device management service. This is also the URL to use for the `url` key when defining a Automated Device Enrollment [`Profile`](profile.md) using `https://mdmenrollment.apple.com/profile`.
- **`trust_profile_url`**: The URL a device uses to obtain a Trust Profile for the device management service, as a fully-formed `.mobileconfig` profile with only payloads of type `com.apple.security.root`.

Omit this key if the device management service doesn’t require a Trust Profile because it’s using a trusted SSL certificate. Don’t return a URL that would generate an empty profile.

> 💡 **Tip**:  Provide a value for `dep_anchor_certs_url` if you provide a value for `dep_enrollment_url`.

Example of an `MDMServiceConfig` request:

```None
// Format
GET https://devicemanagement.example.com/MDMServiceConfig

// Response body
{    "dep_enrollment_url": "https://devicemanagement.example.com/devicemanagement/mdm/dep_mdm_enroll",
    "dep_anchor_certs_url": "https://devicemanagement.example.com/devicemanagement/mdm/dep_anchor_certs",
    "trust_profile_url": "https://certs.example.com/mdm/trust_profile"
}
```

Example of the `dep_anchor_certs_url` key:

```None
// Format
GET https://devicemanagement.example.com/devicemanagement/mdm/dep_anchor_certs

// Response body (truncated)
["MIIEKDCCAxCgAwIBAgIEOjznoTALBgkqhkiG9w0BAQswfjEkMCIGA1UEAwwbU3ly \nYWggQ2VydGlmaWNhd...SVVTo9ll1Lv3OJGqBkxPl9TCC\nfYYnArwzlk4qm1tP\n"]
```

Example of the `trust_profile_url` key:

```None
// Format
GET https://certs.example.com/mdm/trust_profile

// Response body
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>PayloadContent</key>
    <array>
        <dict>
            <key>PayloadContent</key>
            <data>
            MIIEKDCCAxCgAwIBAgIEOjznoTALBgkqhkiG9w0BAQswfjEkMCIG
            ...
            9TCCfYYnArwzlk4qm1tP
            </data>
            <key>PayloadDescription</key>
            <string>Installs the Root certificate for Example Corp.</string>
            <key>PayloadDisplayName</key>
            <string>Root certificate for Example Corp</string>
            <key>PayloadIdentifier</key>
            <string>com.apple.ssl.certificate</string>
            <key>PayloadOrganization</key>
            <string>Example Corp</string> 
            <key>PayloadType</key>
            <string>com.apple.security.root</string>
            <key>PayloadUUID</key>
            <string>B90FA650-5A7D-496A-8C84-0D81C9EBCE6E</string>
            <key>PayloadVersion</key>
            <integer>1</integer>
        </dict>
    </array>
<key>PayloadDescription</key>
<string>Configures your device to trust the device management service.</string>
<key>PayloadDisplayName</key>
<string>Trust Profile for Example Corp</string>
<key>PayloadIdentifier</key>
<string>com.apple.config.devicemanagement.example.com.ssl</string>
<key>PayloadScope</key>
<string>System</string>
<key>PayloadType</key>
<string>Configuration</string>
<key>PayloadUUID</key>
<string>94cdf5c0-bde0-0131-1ed5-005056831d08</string>
<key>PayloadVersion</key>
<integer>1</integer> 
</dict>
</plist>
```

## See Also

- [Managing connections](managing-connections.md)
  Establish or remove a connection between a device and your device management service.
- [Managing certificates for device management services and devices](managing-certificates-for-device-management-services-and-devices.md)
  Ensure secure connectivity with your device management service using valid certificates.
- [Dealing with inactive managed devices and invalid push tokens](dealing-with-inactive-managed-devices-and-invalid-push-tokens.md)
  Handle when devices become unmanageable due to inactivity or invalid push tokens.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/providing-information-about-your-device-management-service)*
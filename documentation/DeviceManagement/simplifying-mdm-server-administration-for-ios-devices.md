# Simplifying MDM Server Administration for iOS Devices

**Framework**: Device Management

Create a service configuration entry point to your MDM server to access to frequently used information.

#### Overview

Add an unauthenticated HTTPS request entry point to your server to make it easier to access useful information about your MDM server. Create the entry point using the endpoint `/MDMServiceConfig`; for example, `https://mdm.example.com/MDMServiceConfig`. The server code should return a UTF-8 JSON-encoded hash (`Content-Type: application/json; charset=UTF8`) with the following values in the body of its response:

Provide this URL even if the MDM server doesn’t require additional certificates because it’s using a trusted SSL certificate. However, provide either an empty body (`Content-Length: 0`) or an empty array JSON string (`'[]'`) .

Omit this key if the MDM server doesn’t require a Trust Profile because it’s using a trusted SSL certificate. Don’t return a URL that would generate an empty profile.

> 💡 **Tip**:  Provide a value for `dep_anchor_certs_url` if you provide a value for `dep_enrollment_url`.

 Provide a value for `dep_anchor_certs_url` if you provide a value for `dep_enrollment_url`.

##### Example of an Mdmserviceconfig Request

```None
// Format
GET https://mdm.example.com/MDMServiceConfig

// Response body
{    "dep_enrollment_url": "https://mdm.example.com/devicemanagement/mdm/dep_mdm_enroll",
    "dep_anchor_certs_url": "https://mdm.example.com/devicemanagement/mdm/dep_anchor_certs",
    "trust_profile_url": "https://certs.example.com/mdm/trust_profile"
}
```

##### Example of the Depanchorcertsurl Key

```None
// Format
GET https://mdm.example.com/devicemanagement/mdm/dep_anchor_certs

// Response body (truncated)
["MIIEKDCCAxCgAwIBAgIEOjznoTALBgkqhkiG9w0BAQswfjEkMCIGA1UEAwwbU3ly \nYWggQ2VydGlmaWNhd...SVVTo9ll1Lv3OJGqBkxPl9TCC\nfYYnArwzlk4qm1tP\n"]
```

##### Example of the Trustprofileurl Key

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
<string>Configures your device to trust the MDM server.</string>
<key>PayloadDisplayName</key>
<string>Trust Profile for Example Corp</string>
<key>PayloadIdentifier</key>
<string>com.apple.config.mdm.example.com.ssl</string>
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

- [Managing MDM Connections](managing-mdm-connections.md)
  Establish or remove a connection between a device and an MDM server.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/simplifying-mdm-server-administration-for-ios-devices)*
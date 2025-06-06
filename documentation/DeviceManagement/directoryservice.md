# DirectoryService

**Framework**: Device Management  
**Kind**: dictionary

The payload you use to configure an Active Directory (AD) domain.

**Availability**:
- macOS 10.8+
- Device Assignment Services ?+
- VPP License Management ?+

## Declaration

```swift
object DirectoryService
```

#### Discussion

Specify `com.apple.DirectoryService.managed` as the payload type.

##### Profile Availability

|  |  |
| --- | --- |
| Device Channel | macOS |
| User Channel | - |
| Allow Manual Install | macOS |
| Requires Supervision | - |
| Requires User Approved MDM | - |
| Allowed in User Enrollment | macOS |
| Allow Multiple Payloads | macOS |

##### Profile Example

```None
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>PayloadContent</key>
    <array>
        <dict>
            <key>HostName</key>
            <string>host.example.com</string>
            <key>Password</key>
            <string>Password123</string>
            <key>UserName</key>
            <string>bind</string>
            <key>PayloadIdentifier</key>
            <string>com.example.mydspayload</string>
            <key>PayloadType</key>
            <string>com.apple.DirectoryService.managed</string>
            <key>PayloadUUID</key>
            <string>bb657e20-60b9-4c47-8730-51803ddf69e7</string>
            <key>PayloadVersion</key>
            <integer>1</integer>
        </dict>
    </array>
    <key>PayloadDisplayName</key>
    <string>Active Directory</string>
    <key>PayloadIdentifier</key>
    <string>com.example.myprofile</string>
    <key>PayloadType</key>
    <string>Configuration</string>
    <key>PayloadUUID</key>
    <string>079b6bc3-4356-4d80-89b4-a4b8a82eb739</string>
    <key>PayloadVersion</key>
    <integer>1</integer>
</dict>
</plist>
```

## See Also

- [object ExtensibleSingleSignOn](extensiblesinglesignon.md)
  The payload you use to configure an app extension that performs single sign-on (SSO).
- [object ExtensibleSingleSignOnKerberos](extensiblesinglesignonkerberos.md)
  The payload you use to configure an app extension that performs single sign-on with the Kerberos extension.
- [object Identification](identification.md)
  The payload you use to configure the names of the account user.
- [object IdentityPreference](identitypreference.md)
  The payload you use to configure the user’s identity on the device.
- [object SingleSignOn](singlesignon.md)
  The payload you use to configure single sign-on (SSO).


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/directoryservice)*
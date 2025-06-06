# SingleSignOn

**Framework**: Device Management  
**Kind**: dictionary

The payload you use to configure single sign-on (SSO).

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Device Assignment Services ?+
- VPP License Management ?+

## Declaration

```swift
object SingleSignOn
```

#### Discussion

Specify `com.apple.sso` as the payload type.

##### Profile Availability

|  |  |
| --- | --- |
| Device Channel | iOS |
| User Channel | - |
| Allow Manual Install | iOS |
| Requires Supervision | - |
| Requires User Approved MDM | - |
| Allowed in User Enrollment | iOS |
| Allow Multiple Payloads | - |

##### Profile Example

```None
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>PayloadContent</key>
    <array>
        <dict>
            <key>ExtensionData</key>
            <dict>
                <key>useSiteAutoDiscovery</key>
                <true/>
            </dict>
            <key>ExtensionIdentifier</key>
            <string>com.apple.com</string>
            <key>TeamIdentifier</key>
            <string>RandomTeamID</string>
            <key>Hosts</key>
            <array>
                <string>.com.example.com</string>
            </array>
            <key>Realm</key>
            <string>com.example.com</string>
            <key>Type</key>
            <string>Credential</string>
            <key>PayloadIdentifier</key>
            <string>com.example.myssopayload</string>
            <key>PayloadType</key>
            <string>com.apple.sso</string>
            <key>PayloadUUID</key>
            <string>02cdfc1c-3c53-434d-99db-c55ee62548bd</string>
            <key>PayloadVersion</key>
            <integer>1</integer>
        </dict>
    </array>
    <key>PayloadDisplayName</key>
    <string>SSO</string>
    <key>PayloadIdentifier</key>
    <string>com.example.myprofile</string>
    <key>PayloadType</key>
    <string>Configuration</string>
    <key>PayloadUUID</key>
    <string>00d92c73-9844-4dc6-b742-eda33efbbf23</string>
    <key>PayloadVersion</key>
    <integer>1</integer>
</dict>
</plist>
```

## Topics

### Supporting Objects
- [object SingleSignOn.Kerberos](singlesignon/kerberos-data.dictionary.md)

## See Also

- [object DirectoryService](directoryservice.md)
  The payload you use to configure an Active Directory (AD) domain.
- [object ExtensibleSingleSignOn](extensiblesinglesignon.md)
  The payload you use to configure an app extension that performs single sign-on (SSO).
- [object ExtensibleSingleSignOnKerberos](extensiblesinglesignonkerberos.md)
  The payload you use to configure an app extension that performs single sign-on with the Kerberos extension.
- [object Identification](identification.md)
  The payload you use to configure the names of the account user.
- [object IdentityPreference](identitypreference.md)
  The payload you use to configure the user’s identity on the device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/singlesignon)*
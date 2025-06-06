# ExtensibleSingleSignOn

**Framework**: Device Management  
**Kind**: dictionary

The payload you use to configure an app extension that performs single sign-on (SSO).

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- macOS 10.15+
- visionOS 1.1+
- Device Assignment Services ?+
- VPP License Management ?+

## Declaration

```swift
object ExtensibleSingleSignOn
```

#### Discussion

Specify `com.apple.extensiblesso` as the payload type.

The system supports user channel installation in macOS 11 and later.

##### Profile Availability

|  |  |
| --- | --- |
| Device Channel | macOS |
| User Channel | macOS, Shared iPad |
| Allow Manual Install | - |
| Requires Supervision | - |
| Requires User Approved MDM | macOS |
| Allowed in User Enrollment | iOS, macOS |
| Allow Multiple Payloads | iOS, macOS, Shared iPad |

##### Profile Example

```None
<?xml version="1.0" encoding="UTF-8"?><!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
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
            <string>com.example.com</string>
            <key>TeamIdentifier</key>
            <string>RandomTeamID</string>
            <key>Hosts</key>
            <array>
                <string>.com.example.com</string>
            </array>
            <key>Realm</key>
            <string>COM.URL.COM</string>
            <key>Type</key>
            <string>Credential</string>
            <key>PayloadIdentifier</key>
            <string>com.example.myessopayload</string>
            <key>PayloadType</key>
            <string>com.apple.extensiblesso</string>
            <key>PayloadUUID</key>
            <string>dbed949d-39a2-440d-a84b-e0c825cdcb2e</string>
            <key>PayloadVersion</key>
            <integer>1</integer>
        </dict>
    </array>
    <key>PayloadDisplayName</key>
    <string>Extensible SSO</string>
    <key>PayloadIdentifier</key>
    <string>com.example.myprofile</string>
    <key>PayloadType</key>
    <string>Configuration</string>
    <key>PayloadUUID</key>
    <string>da3bbbec-a753-4aa7-aeae-a74b7a65c0b5</string>
    <key>PayloadVersion</key>
    <integer>1</integer>
</dict>
</plist>
```

## Topics

### Supporting Objects
- [object ExtensibleSingleSignOn.ExtensionData](extensiblesinglesignon/extensiondata-data.dictionary.md)
  The additional data to pass to the app extension.
- [object ExtensibleSingleSignOn.PlatformSSO](extensiblesinglesignon/platformsso-data.dictionary.md)
  The dictionary to configure Platform SSO.

## See Also

- [object DirectoryService](directoryservice.md)
  The payload you use to configure an Active Directory (AD) domain.
- [object ExtensibleSingleSignOnKerberos](extensiblesinglesignonkerberos.md)
  The payload you use to configure an app extension that performs single sign-on with the Kerberos extension.
- [object Identification](identification.md)
  The payload you use to configure the names of the account user.
- [object IdentityPreference](identitypreference.md)
  The payload you use to configure the user’s identity on the device.
- [object SingleSignOn](singlesignon.md)
  The payload you use to configure single sign-on (SSO).


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/extensiblesinglesignon)*
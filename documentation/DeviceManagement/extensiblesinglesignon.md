# ExtensibleSingleSignOn

**Framework**: Device Management  
**Kind**: dictionary

The payload that configures an app extension that performs single sign-on (SSO).

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- macOS 10.15+
- visionOS 1.1+

## Declaration

```swift
object ExtensibleSingleSignOn
```

## Mentions

- [Implementing Platform SSO during device enrollment](implementing-platform-sso-during-device-enrollment.md)
- [Implementing Platform SSO for unattended device enrollment](implementing-platform-sso-for-unattended-device-enrollment.md)

#### Discussion

Specify `com.apple.extensiblesso` as the payload type.

The system supports user channel installation in macOS 11 and later.

##### Profile Availability

|  |  |
| --- | --- |
| Device channel | iOS, macOS, visionOS |
| User channel | macOS, Shared iPad |
| Allow manual install | NA |
| Requires supervision | NA |
| Requires user-approved MDM | macOS |
| Allowed in user enrollment | iOS, macOS, visionOS |
| Allow multiple payloads | iOS, macOS, Shared iPad, visionOS |

##### Profile Example

```plist
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

### Objects
- [object ExtensibleSingleSignOn.ExtensionData](extensiblesinglesignon/extensiondata-data.dictionary.md)
  The additional data to pass to the app extension.
- [object ExtensibleSingleSignOn.PlatformSSO](extensiblesinglesignon/platformsso-data.dictionary.md)
  The dictionary to configure Platform SSO. Requires `Type` to be set to `Redirect`.

## See Also

- [object DirectoryService](directoryservice.md)
  The payload that configures an Active Directory (AD) domain.
- [object ExtensibleSingleSignOnKerberos](extensiblesinglesignonkerberos.md)
  The payload that configures an app extension that performs single sign-on with the Kerberos extension.
- [object Identification](identification.md)
  The payload that configures the names of the account user.
- [object IdentityPreference](identitypreference.md)
  The payload that configures the user’s identity on the device.
- [object SingleSignOn](singlesignon.md)
  The payload that configures single sign-on (SSO).


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/extensiblesinglesignon)*
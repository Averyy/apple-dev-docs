# PrivacyPreferencesPolicyControl

**Framework**: Device Management  
**Kind**: dictionary

The payload that configures privacy preferences.

**Availability**:
- macOS 10.14+

## Declaration

```swift
object PrivacyPreferencesPolicyControl
```

#### Discussion

Specify `com.apple.TCC.configuration-profile-policy` as the payload type.

##### Profile Availability

|  |  |
| --- | --- |
| Device channel | macOS |
| User channel | NA |
| Allow manual install | NA |
| Requires supervision | NA |
| Requires user-approved MDM | macOS |
| Allowed in user enrollment | NA |
| Allow multiple payloads | macOS |

##### Profile Example

```plist
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>PayloadContent</key>
    <array>
        <dict>
            <key>Services</key>
            <dict>
                <key>PostEvent</key>
                <array>
                    <dict>
                        <key>Allowed</key>
                        <true/>
                        <key>CodeRequirement</key>
                        <string>identifier com.apple.screensharing.agent</string>
                        <key>Comment</key>
                        <string>Allow PostEvent control for ScreensharingAgent</string>
                        <key>Identifier</key>
                        <string>com.apple.screensharing.agent</string>
                        <key>IdentifierType</key>
                        <string>bundleID</string>
                    </dict>
                </array>
            </dict>
            <key>PayloadIdentifier</key>
            <string>com.example.mytccpayload</string>
            <key>PayloadType</key>
            <string>com.apple.TCC.configuration-profile-policy</string>
            <key>PayloadUUID</key>
            <string>5AAF51E3-D21F-4CE6-B0AA-074D75916F68</string>
            <key>PayloadVersion</key>
            <integer>1</integer>
        </dict>
    </array>
    <key>PayloadDisplayName</key>
    <string>Privacy Preferences Policy Control</string>
    <key>PayloadIdentifier</key>
    <string>com.example.myprofile</string>
    <key>PayloadType</key>
    <string>Configuration</string>
    <key>PayloadUUID</key>
    <string>221000F0-D07A-11E8-811E-D0817ADA38E4</string>
    <key>PayloadVersion</key>
    <integer>1</integer>
</dict>
</plist>
```

## Topics

### Objects
- [object PrivacyPreferencesPolicyControl.Services](privacypreferencespolicycontrol/services-data.dictionary.md)
  The privacy policy control services dictionary that controls access on a per app basis.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/privacypreferencespolicycontrol)*
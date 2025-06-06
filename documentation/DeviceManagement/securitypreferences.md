# SecurityPreferences

**Framework**: Device Management  
**Kind**: dictionary

The payload you use to configure security preferences.

**Availability**:
- macOS 10.10+
- Device Assignment Services ?+
- VPP License Management ?+

## Declaration

```swift
object SecurityPreferences
```

#### Discussion

Specify `com.apple.preference.security` as the payload type.

##### Profile Availability

|  |  |
| --- | --- |
| Device Channel | macOS |
| User Channel | macOS |
| Allow Manual Install | macOS |
| Requires Supervision | - |
| Requires User Approved MDM | - |
| Allowed in User Enrollment | - |
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
            <key>dontAllowFireWallUI</key>
            <true/>
            <key>PayloadIdentifier</key>
            <string>com.example.mysecuritypreferencespayload</string>
            <key>PayloadType</key>
            <string>com.apple.preference.security</string>
            <key>PayloadUUID</key>
            <string>d99bb019-a61d-447f-8fed-8f223cc56be3</string>
            <key>PayloadVersion</key>
            <integer>1</integer>
        </dict>
    </array>
    <key>PayloadDisplayName</key>
    <string>Security Preferences</string>
    <key>PayloadIdentifier</key>
    <string>com.example.myprofile</string>
    <key>PayloadType</key>
    <string>Configuration</string>
    <key>PayloadUUID</key>
    <string>b44b6a04-6527-4333-87e5-46422e8a5844</string>
    <key>PayloadVersion</key>
    <integer>1</integer>
</dict>
</plist>
```

## See Also

- [object Passcode](passcode.md)
  The payload you use to configure a passcode policy.
- [object SmartCard](smartcard.md)
  The payload you use to configure a smart card.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/securitypreferences)*
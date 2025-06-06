# SmartCard

**Framework**: Device Management  
**Kind**: dictionary

The payload you use to configure a smart card.

**Availability**:
- macOS 10.12.4+
- Device Assignment Services ?+
- VPP License Management ?+

## Declaration

```swift
object SmartCard
```

#### Discussion

Specify `com.apple.security.smartcard` as the payload type.

##### Profile Availability

|  |  |
| --- | --- |
| Device Channel | macOS |
| User Channel | - |
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
            <key>UserPairing</key>
            <false/>
            <key>allowSmartCard</key>
            <false/>
            <key>checkCertificateTrust</key>
            <false/>
            <key>oneCardPerUser</key>
            <false/>
            <key>tokenRemovalAction</key>
            <integer>1</integer>
            <key>enforceSmartCard</key>
            <true/>
            <key>PayloadIdentifier</key>
            <string>com.example.mysmartcardpayload</string>
            <key>PayloadType</key>
            <string>com.apple.security.smartcard</string>
            <key>PayloadUUID</key>
            <string>88f7336c-d9f6-44d1-b486-11e4080e2223</string>
            <key>PayloadVersion</key>
            <integer>1</integer>
        </dict>
    </array>
    <key>PayloadDisplayName</key>
    <string>SmartCard</string>
    <key>PayloadIdentifier</key>
    <string>com.example.myprofile</string>
    <key>PayloadType</key>
    <string>Configuration</string>
    <key>PayloadUUID</key>
    <string>85091214-a32f-4131-8b03-0045e5d81c42</string>
    <key>PayloadVersion</key>
    <integer>1</integer>
</dict>
</plist>
```

## See Also

- [object Passcode](passcode.md)
  The payload you use to configure a passcode policy.
- [object SecurityPreferences](securitypreferences.md)
  The payload you use to configure security preferences.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/smartcard)*
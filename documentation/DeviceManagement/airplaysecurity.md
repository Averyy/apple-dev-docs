# AirPlaySecurity

**Framework**: Device Management  
**Kind**: dictionary

The payload you use to configure Apple TV for a particular style of AirPlay security.

**Availability**:
- tvOS 11.0+

## Declaration

```swift
object AirPlaySecurity
```

#### Discussion

Specify `com.apple.airplay.security` as the payload type.

##### Profile Availability

|  |  |
| --- | --- |
| Device channel | tvOS |
| User channel | NA |
| Allow manual install | tvOS |
| Requires supervision | NA |
| Requires user-approved MDM | NA |
| Allowed in user enrollment | NA |
| Allow multiple payloads | NA |

##### Profile Example

```plist
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>PayloadContent</key>
    <array>
        <dict>
            <key>Password</key>
            <string>MyPassword</string>
            <key>PayloadIdentifier</key>
            <string>com.example.myairplaysecuritypayload</string>
            <key>PayloadType</key>
            <string>com.apple.airplay.security</string>
            <key>PayloadUUID</key>
            <string>c0b60f19-91c7-482e-9a95-6ba71220d93e</string>
            <key>PayloadVersion</key>
            <integer>1</integer>
            <key>SecurityType</key>
            <string>PASSWORD</string>
            <key>AccessType</key>
            <string>ANY</string>
        </dict>
    </array>
    <key>PayloadDisplayName</key>
    <string>AirPlay Security</string>
    <key>PayloadIdentifier</key>
    <string>com.example.myprofile</string>
    <key>PayloadType</key>
    <string>Configuration</string>
    <key>PayloadUUID</key>
    <string>40dc47ea-41c9-4c79-8b30-a027cf6eacd6</string>
    <key>PayloadVersion</key>
    <integer>1</integer>
</dict>
</plist>
```

## See Also

- [object AirPlay](airplay.md)
  The payload you use to configure AirPlay settings.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/airplaysecurity)*
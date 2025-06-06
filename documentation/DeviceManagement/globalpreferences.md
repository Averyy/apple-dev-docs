# GlobalPreferences

**Framework**: Device Management  
**Kind**: dictionary

The payload you use to configure global preferences.

**Availability**:
- macOS 10.7+
- Device Assignment Services ?+
- VPP License Management ?+

## Declaration

```swift
object GlobalPreferences
```

#### Discussion

Specify `.GlobalPreferences` as the payload type.

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
            <key>MultipleSessionEnabled</key>
            <false/>
            <key>com.example.autologout.AutoLogOutDelay</key>
            <real>1800</real>
            <key>LULookupDisabled</key>
            <true/>
            <key>PayloadIdentifier</key>
            <string>com.example.myglobalpayload</string>
            <key>PayloadType</key>
            <string>.GlobalPreferences</string>
            <key>PayloadUUID</key>
            <string>b5033127-c0ef-4055-8fc5-7db5a8216bc8</string>
            <key>PayloadVersion</key>
            <integer>1</integer>
        </dict>
    </array>
    <key>PayloadDisplayName</key>
    <string>Global Preferences</string>
    <key>PayloadIdentifier</key>
    <string>com.example.myprofile</string>
    <key>PayloadType</key>
    <string>Configuration</string>
    <key>PayloadUUID</key>
    <string>52e0e1b6-067f-407a-a36c-7e7b917b2982</string>
    <key>PayloadVersion</key>
    <integer>1</integer>
</dict>
</plist>
```

## See Also

- [object UserPreferences](userpreferences.md)
  The payload you use to configure iCloud password preferences.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/globalpreferences)*
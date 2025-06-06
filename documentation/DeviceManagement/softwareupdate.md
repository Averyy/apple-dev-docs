# SoftwareUpdate

**Framework**: Device Management  
**Kind**: dictionary

The payload you use to configure the software update policy.

**Availability**:
- macOS 10.7+
- Device Assignment Services ?+
- VPP License Management ?+

## Declaration

```swift
object SoftwareUpdate
```

#### Discussion

Specify `com.apple.SoftwareUpdate` as the payload type.

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
            <key>AutomaticallyInstallAppUpdates</key>
            <false/>
            <key>PayloadIdentifier</key>
            <string>com.example.mysoftwareupdatepayload</string>
            <key>PayloadType</key>
            <string>com.apple.SoftwareUpdate</string>
            <key>PayloadUUID</key>
            <string>af3c6efa-0dd3-4021-814b-6f2dba91428b</string>
            <key>PayloadVersion</key>
            <integer>1</integer>
        </dict>
    </array>
    <key>PayloadDisplayName</key>
    <string>Software Update</string>
    <key>PayloadIdentifier</key>
    <string>com.example.myprofile</string>
    <key>PayloadType</key>
    <string>Configuration</string>
    <key>PayloadUUID</key>
    <string>8b6061ab-31c6-4eee-ba5b-8a09ea8f5fa7</string>
    <key>PayloadVersion</key>
    <integer>1</integer>
</dict>
</plist>

```

## See Also

- [object SystemMigration](systemmigration.md)
  The payload you use to configure system migration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/softwareupdate)*
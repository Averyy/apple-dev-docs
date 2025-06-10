# MediaManagementDiscBurning

**Framework**: Device Management  
**Kind**: dictionary

The payload you use to configure disc-burning settings.

**Availability**:
- macOS 10.7+

## Declaration

```swift
object MediaManagementDiscBurning
```

#### Discussion

Specify `com.apple.DiscRecording` as the payload type.

##### Profile Availability

|  |  |
| --- | --- |
| Device channel | macOS |
| User channel | macOS |
| Allow manual install | macOS |
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
            <key>BurnSupport</key>
            <string>authenticate</string>
            <key>PayloadIdentifier</key>
            <string>com.example.mymediamanagementpayload</string>
            <key>PayloadType</key>
            <string>com.apple.DiscRecording</string>
            <key>PayloadUUID</key>
            <string>c7d88693-77a2-4f4d-a782-6569a1c2d92c</string>
            <key>PayloadVersion</key>
            <integer>1</integer>
        </dict>
    </array>
    <key>PayloadDisplayName</key>
    <string>Media Management</string>
    <key>PayloadIdentifier</key>
    <string>com.example.myprofile</string>
    <key>PayloadType</key>
    <string>Configuration</string>
    <key>PayloadUUID</key>
    <string>8996588b-f785-4720-b68f-fa9c61d74bd4</string>
    <key>PayloadVersion</key>
    <integer>1</integer>
</dict>
</plist>
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/mediamanagementdiscburning)*
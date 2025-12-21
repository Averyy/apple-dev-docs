# ConferenceRoomDisplay

**Framework**: Device Management  
**Kind**: dictionary

The payload that configures Conference Room Display mode for Apple TV.

**Availability**:
- tvOS 10.2+

## Declaration

```swift
object ConferenceRoomDisplay
```

#### Discussion

Specify `com.apple.conferenceroomdisplay` as the payload type.

Conference Room Display mode locks Apple TV into that mode, to prevent other types of usage.

##### Profile Availability

|  |  |
| --- | --- |
| Device channel | tvOS |
| User channel | NA |
| Allow manual install | tvOS |
| Requires supervision | tvOS |
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
            <key>Message</key>
            <string>Display Message</string>
            <key>PayloadIdentifier</key>
            <string>com.example.myconferenceroompayload</string>
            <key>PayloadType</key>
            <string>com.apple.conferenceroomdisplay</string>
            <key>PayloadUUID</key>
            <string>2aff0bfa-62f4-4597-9714-3750f5e3d422</string>
            <key>PayloadVersion</key>
            <integer>1</integer>
        </dict>
    </array>
    <key>PayloadDisplayName</key>
    <string>Conference Room Display</string>
    <key>PayloadIdentifier</key>
    <string>com.example.myprofile</string>
    <key>PayloadType</key>
    <string>Configuration</string>
    <key>PayloadUUID</key>
    <string>c98885c9-12fe-43d2-8476-fb98bc959dd3</string>
    <key>PayloadVersion</key>
    <integer>1</integer>
</dict>
</plist>
```

## See Also

- [object TVRemote](tvremote.md)
  The payload that configures the Apple TV remote.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/conferenceroomdisplay)*
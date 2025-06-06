# TVRemote

**Framework**: Device Management  
**Kind**: dictionary

The payload you use to configure the Apple TV remote.

**Availability**:
- iOS 11.3+
- iPadOS 11.3+
- tvOS 11.3+
- Device Assignment Services ?+
- VPP License Management ?+

## Declaration

```swift
object TVRemote
```

#### Discussion

Specify `com.apple.tvremote` as the payload type.

##### Profile Availability

|  |  |
| --- | --- |
| Device Channel | iOS, Shared iPad, tvOS |
| User Channel | Shared iPad |
| Allow Manual Install | iOS, tvOS |
| Requires Supervision | iOS, tvOS |
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
            <key>AllowedRemotes</key>
            <array>
                <dict>
                    <key>RemoteDeviceID</key>
                    <string>10:10:10:10:10:10</string>
                </dict>
            </array>
            <key>AllowedTVs</key>
            <array/>
            <key>PayloadIdentifier</key>
            <string>com.example.mytvremotepayload</string>
            <key>PayloadType</key>
            <string>com.apple.tvremote</string>
            <key>PayloadUUID</key>
            <string>696eb2c4-df9d-463f-b74a-685dae845fac</string>
            <key>PayloadVersion</key>
            <integer>1</integer>
        </dict>
    </array>
    <key>PayloadDisplayName</key>
    <string>TV Remote</string>
    <key>PayloadIdentifier</key>
    <string>com.example.myprofile</string>
    <key>PayloadType</key>
    <string>Configuration</string>
    <key>PayloadUUID</key>
    <string>3de47695-ad92-44f5-9bc9-f1b2f2c7727b</string>
    <key>PayloadVersion</key>
    <integer>1</integer>
</dict>
</plist>
```

## Topics

### Objects
- [object TVRemote.AllowedRemotesItem](tvremote/allowedremotesitem.md)
  The array of valid devices that Apple TV can connect to.
- [object TVRemote.AllowedTVsItem](tvremote/allowedtvsitem.md)
  The array of valid Apple TV identifiers that the remote can connect to.

## See Also

- [object ConferenceRoomDisplay](conferenceroomdisplay.md)
  The payload you use to configure Conference Room Display mode for Apple TV.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/tvremote)*
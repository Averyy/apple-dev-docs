# LockScreenMessage

**Framework**: Device Management  
**Kind**: dictionary

The payload you use to configure a Lock screen message.

**Availability**:
- iOS 9.3+
- iPadOS 9.3+
- Device Assignment Services ?+
- VPP License Management ?+

## Declaration

```swift
object LockScreenMessage
```

#### Discussion

Specify `com.apple.shareddeviceconfiguration` as the payload type.

This payload allows administrators to specify optional text displayed in the login window and Lock screen (for example, an “If Lost, Return To” message and asset tag information). There can only be one Lock screen payload.

##### Profile Availability

|  |  |
| --- | --- |
| Device Channel | iOS, Shared iPad |
| User Channel | - |
| Allow Manual Install | iOS |
| Requires Supervision | iOS |
| Requires User-Approved MDM | - |
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
            <key>AssetTagInformation</key>
            <string>1234</string>
            <key>IfLostReturnToMessage</key>
            <string>Example message</string>
            <key>PayloadIdentifier</key>
            <string>com.example.mylockscreenpayload</string>
            <key>PayloadType</key>
            <string>com.apple.shareddeviceconfiguration</string>
            <key>PayloadUUID</key>
            <string>b10c0436-a51b-4119-b604-bd580f396723</string>
            <key>PayloadVersion</key>
            <integer>1</integer>
        </dict>
    </array>
    <key>PayloadDisplayName</key>
    <string>Lock Screen Message</string>
    <key>PayloadIdentifier</key>
    <string>com.example.myprofile</string>
    <key>PayloadType</key>
    <string>Configuration</string>
    <key>PayloadUUID</key>
    <string>588f1406-47be-47fc-9907-4e7955fb6d4a</string>
    <key>PayloadVersion</key>
    <integer>1</integer>
</dict>
</plist>
```

## See Also

- [object Declarations](declarations.md)
  The payload to apply a set of declaration to the device through the Settings app.
- [object EnergySaver](energysaver.md)
  The payload you use to configure energy-saver settings.
- [object FileProvider](fileprovider.md)
  The payload you use to configure file provider settings.
- [object Font](font.md)
  The payload you use to configure fonts.
- [object Screensaver](screensaver.md)
  The payload you use to configure the screen saver.
- [object SystemExtensions](systemextensions.md)
  The payload you use to configure system extensions.
- [object SystemLogging](systemlogging.md)
  The payload you use to configure system logging.
- [object TimeServer](timeserver.md)
  The payload you use to configure the time server.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/lockscreenmessage)*
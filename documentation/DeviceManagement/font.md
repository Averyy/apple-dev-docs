# Font

**Framework**: Device Management  
**Kind**: dictionary

The payload you use to configure fonts.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- macOS 10.9+
- visionOS 2.0+
- Device Assignment Services ?+
- VPP License Management ?+

## Declaration

```swift
object Font
```

#### Discussion

Specify `com.apple.font` as the payload type.

In iPadOS 18 and later, the font profile is available on the user channel for shared iPads.

##### Profile Availability

|  |  |
| --- | --- |
| Device Channel | iOS, macOS |
| User Channel | macOS, Shared iPad |
| Allow Manual Install | iOS, macOS |
| Requires Supervision | - |
| Requires User Approved MDM | - |
| Allowed in User Enrollment | iOS, macOS |
| Allow Multiple Payloads | iOS, macOS |

##### Profile Example

```None
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>PayloadContent</key>
    <array>
        <dict>
            <key>Font</key>
            <data>base64encodeddata</data>
            <key>Name</key>
            <string>Font.ttf</string>
            <key>PayloadIdentifier</key>
            <string>com.example.myfontpayload</string>
            <key>PayloadType</key>
            <string>com.apple.font</string>
            <key>PayloadUUID</key>
            <string>99659c06-bbbf-45aa-9674-06b378ec2cd5</string>
            <key>PayloadVersion</key>
            <integer>1</integer>
        </dict>
    </array>
    <key>PayloadDisplayName</key>
    <string>Fonts</string>
    <key>PayloadIdentifier</key>
    <string>com.example.myprofile</string>
    <key>PayloadType</key>
    <string>Configuration</string>
    <key>PayloadUUID</key>
    <string>9800ea91-30c4-4212-8033-d21cad4fe99a</string>
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
- [object LockScreenMessage](lockscreenmessage.md)
  The payload you use to configure a Lock screen message.
- [object Screensaver](screensaver.md)
  The payload you use to configure the screen saver.
- [object SystemExtensions](systemextensions.md)
  The payload you use to configure system extensions.
- [object SystemLogging](systemlogging.md)
  The payload you use to configure system logging.
- [object TimeServer](timeserver.md)
  The payload you use to configure the time server.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/font)*
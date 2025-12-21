# Font

**Framework**: Device Management  
**Kind**: dictionary

The payload that configures fonts.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- macOS 10.9+
- visionOS 2.0+

## Declaration

```swift
object Font
```

#### Discussion

Specify `com.apple.font` as the payload type.

In iPadOS 18 and later, the font profile is available on the user channel for Shared iPads.

##### Profile Availability

|  |  |
| --- | --- |
| Device channel | iOS, macOS, visionOS |
| User channel | macOS, Shared iPad |
| Allow manual install | iOS, macOS, visionOS |
| Requires supervision | NA |
| Requires user-approved MDM | NA |
| Allowed in user enrollment | iOS, macOS, visionOS |
| Allow multiple payloads | iOS, macOS, Shared iPad, visionOS |

##### Profile Example

```plist
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
    <dict>
        <key>PayloadContent</key>
        <array>
            <dict>
                <key>Font</key>
                <data>YmFzZTY0ZW5jb2RlZGRhdGEK</data>
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
  The payload that applies a set of declarations to the device through the Settings app.
- [object EnergySaver](energysaver.md)
  The payload that configures Energy Saver settings.
- [object FileProvider](fileprovider.md)
  The payload that configures file provider settings.
- [object LockScreenMessage](lockscreenmessage.md)
  The payload that configures a Lock Screen message.
- [object Screensaver](screensaver.md)
  The payload that configures the screen saver.
- [object SystemExtensions](systemextensions.md)
  The payload that configures system extensions.
- [object SystemLogging](systemlogging.md)
  The payload that configures system logging.
- [object TimeServer](timeserver.md)
  The payload that configures the time server.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/font)*
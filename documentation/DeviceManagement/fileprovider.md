# FileProvider

**Framework**: Device Management  
**Kind**: dictionary

The payload you use to configure file provider settings.

**Availability**:
- macOS 11.0+

## Declaration

```swift
object FileProvider
```

#### Discussion

Specify `com.apple.fileproviderd` as the payload type.

##### Profile Availability

|  |  |
| --- | --- |
| Device channel | macOS |
| User channel | macOS |
| Allow manual install | NA |
| Requires supervision | NA |
| Requires user-approved MDM | macOS |
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
            <key>AllowManagedFileProvidersToRequestAttribution</key>
            <true/>
            <key>PayloadIdentifier</key>
            <string>com.example.myfileproviderpayload</string>
            <key>PayloadType</key>
            <string>com.apple.fileproviderd</string>
            <key>PayloadUUID</key>
            <string>3ffb5741-f0f1-4fc2-9566-679ca8b10db1</string>
            <key>PayloadVersion</key>
            <integer>1</integer>
        </dict>
    </array>
    <key>PayloadDisplayName</key>
    <string>FileProvider</string>
    <key>PayloadIdentifier</key>
    <string>com.example.myprofile</string>
    <key>PayloadType</key>
    <string>Configuration</string>
    <key>PayloadUUID</key>
    <string>8efec75c-f1d3-4aaa-a4ef-104dc25cfc3d</string>
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
- [object Font](font.md)
  The payload you use to configure fonts.
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

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/fileprovider)*
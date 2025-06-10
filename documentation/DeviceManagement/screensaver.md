# Screensaver

**Framework**: Device Management  
**Kind**: dictionary

The payload you use to configure the screen saver.

**Availability**:
- macOS 10.11+

## Declaration

```swift
object Screensaver
```

#### Discussion

Specify `com.apple.screensaver` as the payload type.

##### Profile Availability

|  |  |
| --- | --- |
| Device channel | macOS |
| User channel | NA |
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
            <key>idleTime</key>
            <integer>60</integer>
            <key>loginWindowIdleTime</key>
            <integer>60</integer>
            <key>loginWindowModulePath</key>
            <string>/System/Library/Screen Savers/Example-Name.saver</string>
            <key>moduleName</key>
            <string>Example Name</string>
            <key>askForPassword</key>
            <true/>
            <key>askForPasswordDelay</key>
            <integer>5</integer>
            <key>PayloadIdentifier</key>
            <string>com.example.myscreensaverpayload</string>
            <key>PayloadType</key>
            <string>com.apple.screensaver</string>
            <key>PayloadUUID</key>
            <string>ba9abec1-ee44-413d-b75f-63748644ca71</string>
            <key>PayloadVersion</key>
            <integer>1</integer>
        </dict>
    </array>
    <key>PayloadDisplayName</key>
    <string>Screem Saver Device</string>
    <key>PayloadIdentifier</key>
    <string>com.example.myprofile</string>
    <key>PayloadType</key>
    <string>Configuration</string>
    <key>PayloadUUID</key>
    <string>4ffe721a-f2e6-4191-a3fe-1d1a463fbbac</string>
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
- [object LockScreenMessage](lockscreenmessage.md)
  The payload you use to configure a Lock screen message.
- [object SystemExtensions](systemextensions.md)
  The payload you use to configure system extensions.
- [object SystemLogging](systemlogging.md)
  The payload you use to configure system logging.
- [object TimeServer](timeserver.md)
  The payload you use to configure the time server.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/screensaver)*
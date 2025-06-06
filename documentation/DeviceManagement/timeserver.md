# TimeServer

**Framework**: Device Management  
**Kind**: dictionary

The payload you use to configure the time server.

**Availability**:
- macOS 10.12.4+
- Device Assignment Services ?+
- VPP License Management ?+

## Declaration

```swift
object TimeServer
```

#### Discussion

Specify `com.apple.MCX` as the payload type.

If multiple profiles with this payload are sent, the system sets the device’s time server to the value in the last payload installed. Removing the payload won’t change the settings back to the prior settings.

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
            <key>timeServer</key>
            <string>ntp.example.com</string>
            <key>timeZone</key>
            <string>America/Denver</string>
            <key>PayloadIdentifier</key>
            <string>com.example.mytimeserverpayload</string>
            <key>PayloadType</key>
            <string>com.apple.MCX</string>
            <key>PayloadUUID</key>
            <string>7bc24f5a-5ad8-4ad0-b05e-8f5f4418ff05</string>
            <key>PayloadVersion</key>
            <integer>1</integer>
        </dict>
    </array>
    <key>PayloadDisplayName</key>
    <string>Time Server</string>
    <key>PayloadIdentifier</key>
    <string>com.example.myprofile</string>
    <key>PayloadType</key>
    <string>Configuration</string>
    <key>PayloadUUID</key>
    <string>a18b9fa3-dbdc-4e60-89e0-d785c7c6a1a0</string>
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
- [object Screensaver](screensaver.md)
  The payload you use to configure the screen saver.
- [object SystemExtensions](systemextensions.md)
  The payload you use to configure system extensions.
- [object SystemLogging](systemlogging.md)
  The payload you use to configure system logging.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/timeserver)*
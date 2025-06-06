# SystemLogging

**Framework**: Device Management  
**Kind**: dictionary

The payload you use to configure system logging.

**Availability**:
- macOS 10.12+
- Device Assignment Services ?+
- VPP License Management ?+

## Declaration

```swift
object SystemLogging
```

#### Discussion

Specify `com.apple.system.logging` as the payload type.

##### Profile Availability

|  |  |
| --- | --- |
| Device Channel | iOS, macOS, Shared iPad, tvOS, watchOS |
| User Channel | macOS |
| Allow Manual Install | iOS, macOS, tvOS, watchOS |
| Requires Supervision | - |
| Requires User Approved MDM | - |
| Allowed in User Enrollment | - |
| Allow Multiple Payloads | iOS, macOS, Shared iPad, tvOS, watchOS |

##### Profile Example

```None
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>PayloadContent</key>
    <array>
        <dict>
            <key>Processes</key>
            <dict/>
            <key>Subsystems</key>
            <dict>
                <key>com.example.app</key>
                <dict>
                    <key>DEFAULT-OPTIONS</key>
                    <dict>
                        <key>Level</key>
                        <dict>
                            <key>Enable</key>
                            <string>Info</string>
                        </dict>
                        <key>Default-Privacy-Setting</key>
                        <string>Public</string>
                    </dict>
                </dict>
            </dict>
            <key>PayloadIdentifier</key>
            <string>com.example.mysystemloggingpayload</string>
            <key>PayloadType</key>
            <string>com.apple.system.logging</string>
            <key>PayloadUUID</key>
            <string>0ff59613-35e9-495c-88c8-01963de4ac80</string>
            <key>PayloadVersion</key>
            <integer>1</integer>
        </dict>
    </array>
    <key>PayloadDisplayName</key>
    <string>System Logging</string>
    <key>PayloadIdentifier</key>
    <string>com.example.myprofile</string>
    <key>PayloadType</key>
    <string>Configuration</string>
    <key>PayloadUUID</key>
    <string>0fbfa83e-c8ec-49d0-b50c-3acc3c05749c</string>
    <key>PayloadVersion</key>
    <integer>1</integer>
</dict>
</plist>
```

## Topics

### Objects
- [object SystemLogging.Processes](systemlogging/processes-data.dictionary.md)
- [object SystemLogging.Subsystems](systemlogging/subsystems-data.dictionary.md)
- [object SystemLogging.System](systemlogging/system-data.dictionary.md)

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
- [object TimeServer](timeserver.md)
  The payload you use to configure the time server.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/systemlogging)*
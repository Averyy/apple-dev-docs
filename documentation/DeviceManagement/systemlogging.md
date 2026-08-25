# SystemLogging

**Framework**: Device Management  
**Kind**: dictionary

The payload that configures system logging.

**Availability**:
- macOS 10.12+

## Declaration

```swift
object SystemLogging
```

#### Discussion

Specify `com.apple.system.logging` as the payload type.

##### Profile Availability

|  |  |
| --- | --- |
| Device channel | macOS |
| User channel | macOS |
| Allow manual install | macOS |
| Requires supervision | N/A |
| Requires user-approved MDM | N/A |
| Allowed in user enrollment | N/A |
| Allow multiple payloads | macOS |

##### Profile Example

```plist
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>PayloadContent</key>
    <array>
        <dict>
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
- [object SystemLogging.Subsystems](systemlogging/subsystems-data.dictionary.md)
  A dictionary enabling the logging level for subsystems. See `Customizing Logging Behavior While Debugging` for more details about the format of the dictionary.
- [object SystemLogging.System](systemlogging/system-data.dictionary.md)
  This dictionary has one key, `Enable-Private-Data`. Setting that value to `true` enables private data logging for the entire system.

## Properties

- `Subsystems` (SystemLogging.Subsystems): A dictionary enabling the logging level for subsystems. See `Customizing Logging Behavior While Debugging` for more details about the format of the dictionary.
- `System` (SystemLogging.System): This dictionary has one key, `Enable-Private-Data`. Setting that value to `true` enables private data logging for the entire system.

## See Also

- [object Declarations](declarations.md)
  The payload that applies a set of declarations to the device through the Settings app.
- [object EnergySaver](energysaver.md)
  The payload that configures Energy Saver settings.
- [object FileProvider](fileprovider.md)
  The payload that configures file provider settings.
- [object Font](font.md)
  The payload that configures fonts.
- [object LockScreenMessage](lockscreenmessage.md)
  The payload that configures a Lock Screen message.
- [object Screensaver](screensaver.md)
  The payload that configures the screen saver.
- [object SystemExtensions](systemextensions.md)
  The payload that configures system extensions.
- [object TimeServer](timeserver.md)
  The payload that configures the time server.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/systemlogging)*
# Screensaver

**Framework**: Device Management  
**Kind**: dictionary

The payload that configures the screen saver.

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
| User channel | N/A |
| Allow manual install | macOS |
| Requires supervision | N/A |
| Requires user-approved MDM | N/A |
| Allowed in user enrollment | N/A |
| Allow multiple payloads | N/A |

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
    <string>Screen Saver Device</string>
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

## Properties

- `askForPassword` (boolean): If `true`, the device prompts the user for a password when the screen saver is unlocked or stopped. When you use this prompt, you must also provide `askForPasswordDelay`. Available: macOS 10.13+
- `askForPasswordDelay` (integer): The number of seconds to delay before the device requires a password to unlock or stop the screen saver (the grace period). A value of `2147483647` (hexadecimal equivalent of `0x7FFFFFFF`) disables this requirement, and a value of `0` immediately requires the password. To use this option, you must set `askForPassword` to `true`. Available: macOS 10.13+
- `idleTime` (integer): The number of seconds of inactivity before the screen saver activates (0 = Never activate).
- `loginWindowModulePath` (string): The full path to the screen-saver module to use.
- `moduleName` (string) *(required)*: The name of the screen saver module.

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
- [object SystemExtensions](systemextensions.md)
  The payload that configures system extensions.
- [object SystemLogging](systemlogging.md)
  The payload that configures system logging.
- [object TimeServer](timeserver.md)
  The payload that configures the time server.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/screensaver)*
# EnergySaver

**Framework**: Device Management  
**Kind**: dictionary

The payload that configures Energy Saver settings.

**Availability**:
- macOS 10.7+

## Declaration

```swift
object EnergySaver
```

#### Discussion

Specify `com.apple.MCX` as the payload type.

##### Profile Availability

|  |  |
| --- | --- |
| Device channel | macOS |
| User channel | NA |
| Allow manual install | macOS |
| Requires supervision | NA |
| Requires user-approved MDM | NA |
| Allowed in user enrollment | NA |
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
            <key>com.example.EnergySaver.desktop.ACPower</key>
            <dict>
                <key>Automatic Restart On Power Loss</key>
                <integer>1</integer>
                <key>Disk Sleep Timer</key>
                <integer>180</integer>
                <key>Display Sleep Timer</key>
                <integer>60</integer>
                <key>Sleep On Power Button</key>
                <integer>0</integer>
                <key>System Sleep Timer</key>
                <integer>120</integer>
                <key>Wake On LAN</key>
                <integer>1</integer>
            </dict>
            <key>com.apple.EnergySaver.desktop.ACPower-ProfileNumber</key>
            <integer>-1</integer>
            <key>com.apple.EnergySaver.desktop.Schedule</key>
            <dict>
                <key>RepeatingPowerOff</key>
                <dict>
                    <key>eventtype</key>
                    <string>sleep</string>
                    <key>time</key>
                    <integer>0</integer>
                    <key>weekdays</key>
                    <integer>31</integer>
                </dict>
                <key>RepeatingPowerOn</key>
                <dict>
                    <key>eventtype</key>
                    <string>wakepoweron</string>
                    <key>time</key>
                    <integer>0</integer>
                    <key>weekdays</key>
                    <integer>31</integer>
                </dict>
            </dict>
            <key>com.apple.EnergySaver.portable.ACPower</key>
            <dict>
                <key>Automatic Restart On Power Loss</key>
                <integer>1</integer>
                <key>Disk Sleep Timer</key>
                <integer>180</integer>
                <key>Display Sleep Timer</key>
                <integer>5</integer>
                <key>System Sleep Timer</key>
                <integer>10</integer>
                <key>Wake On LAN</key>
                <integer>1</integer>
            </dict>
            <key>com.apple.EnergySaver.portable.ACPower-ProfileNumber</key>
            <integer>-1</integer>
            <key>com.apple.EnergySaver.portable.BatteryPower</key>
            <dict>
                <key>Automatic Restart On Power Loss</key>
                <integer>1</integer>
                <key>Disk Sleep Timer</key>
                <integer>180</integer>
                <key>Display Sleep Timer</key>
                <integer>5</integer>
                <key>System Sleep Timer</key>
                <integer>10</integer>
                <key>Wake On LAN</key>
                <integer>1</integer>
            </dict>
            <key>com.apple.EnergySaver.portable.BatteryPower-ProfileNumber</key>
            <integer>-1</integer>
            <key>PayloadIdentifier</key>
            <string>com.example.myenergysaverpayload</string>
            <key>PayloadType</key>
            <string>com.apple.MCX</string>
            <key>PayloadUUID</key>
            <string>e66c94e5-f059-404e-9188-ff152cb80c64</string>
            <key>PayloadVersion</key>
            <integer>1</integer>
        </dict>
    </array>
    <key>PayloadDisplayName</key>
    <string>EnergySaver</string>
    <key>PayloadIdentifier</key>
    <string>com.example.myprofile</string>
    <key>PayloadType</key>
    <string>Configuration</string>
    <key>PayloadUUID</key>
    <string>2627f09c-a6ea-4a2d-94b3-f6df28b3c6af</string>
    <key>PayloadVersion</key>
    <integer>1</integer>
</dict>
</plist>
```

## Topics

### Objects
- [object EnergySaver.Com.apple.EnergySaver.desktop.ACPower](energysaver/com.apple.energysaver.desktop.acpower-data.dictionary.md)
  The desktop AC power Energy Saver settings.
- [object EnergySaver.Com.apple.EnergySaver.desktop.Schedule](energysaver/com.apple.energysaver.desktop.schedule-data.dictionary.md)
  The schedule for turning the device on or off.
- [object EnergySaver.Com.apple.EnergySaver.portable.ACPower](energysaver/com.apple.energysaver.portable.acpower-data.dictionary.md)
  The laptop AC power Energy Saver settings.
- [object EnergySaver.Com.apple.EnergySaver.portable.BatteryPower](energysaver/com.apple.energysaver.portable.batterypower-data.dictionary.md)
  The laptop battery power Energy Saver settings.

## See Also

- [object Declarations](declarations.md)
  The payload that applies a set of declarations to the device through the Settings app.
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
- [object SystemLogging](systemlogging.md)
  The payload that configures system logging.
- [object TimeServer](timeserver.md)
  The payload that configures the time server.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/energysaver)*
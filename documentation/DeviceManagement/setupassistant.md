# SetupAssistant

**Framework**: Device Management  
**Kind**: dictionary

The payload that configures Setup Assistant settings.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 10.12+

## Declaration

```swift
object SetupAssistant
```

#### Discussion

Specify `com.apple.SetupAssistant.managed` as the payload type.

##### Profile Availability

|  |  |
| --- | --- |
| Device channel | iOS, macOS, Shared iPad |
| User channel | macOS |
| Allow manual install | iOS, macOS |
| Requires supervision | iOS |
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
            <key>SkipCloudSetup</key>
            <true/>
            <key>SkipSiriSetup</key>
            <true/>
            <key>SkipPrivacySetup</key>
            <true/>
            <key>SkipiCloudStorageSetup</key>
            <true/>
            <key>SkipTrueTone</key>
            <true/>
            <key>SkipAppearance</key>
            <true/>
            <key>SkipTouchIDSetup</key>
            <true/>
            <key>SkipScreenTime</key>
            <true/>
            <key>SkipAccessibility</key>
            <true/>
            <key>PayloadIdentifier</key>
            <string>com.example.mysetupassistantpayload</string>
            <key>PayloadType</key>
            <string>com.apple.SetupAssistant.managed</string>
            <key>PayloadUUID</key>
            <string>0dfccedc-e28f-4df5-bca7-a0807deab543</string>
            <key>PayloadVersion</key>
            <integer>1</integer>
        </dict>
    </array>
    <key>PayloadDisplayName</key>
    <string>Setup Assistant</string>
    <key>PayloadIdentifier</key>
    <string>com.example.myprofile</string>
    <key>PayloadType</key>
    <string>Configuration</string>
    <key>PayloadUUID</key>
    <string>4a66b685-604a-4558-92c7-ae3e082cf0ae</string>
    <key>PayloadVersion</key>
    <integer>1</integer>
</dict>
</plist>
```

## Properties

- `SkipAccessibility` (boolean): If `true`, the system skips the Accessibility pane. Available: macOS 11+
Deprecated: macOS 15+
- `SkipAppearance` (boolean): If `true`, the system skips the Choose Your Look pane. Available: macOS 10.14+
Deprecated: macOS 15+
- `SkipCloudSetup` (boolean): If `true`, the system skips the Apple Account setup pane. Available: macOS 10.12+
Deprecated: macOS 15+
- `SkipiCloudStorageSetup` (boolean): If `true`, the system skips the iCloud Storage pane. Available: macOS 10.13.4+
Deprecated: macOS 15+
- `SkipPrivacySetup` (boolean): If `true`, the system skips the Privacy consent pane. Available: macOS 10.13.4+
Deprecated: macOS 15+
- `SkipScreenTime` (boolean): If `true`, the system skips the Screen Time pane. Available: macOS 10.15+
Deprecated: macOS 15+
- `SkipSetupItems` ([string]): An array of strings that describe the setup items to skip. [`SkipKeys`](skipkeys.md) provides a list of valid strings and their meanings. Available: iOS 14+ | iPadOS 14+ | macOS 15+
- `SkipSiriSetup` (boolean): If `true`, the system skips the Siri setup pane. Available: macOS 10.12+
Deprecated: macOS 15+
- `SkipTouchIDSetup` (boolean): If `true`, the system skips the Touch ID setup pane. Available: macOS 10.15+
Deprecated: macOS 15+
- `SkipTrueTone` (boolean): If `true`, the system skips the True Tone Display pane. Available: macOS 10.13.6+
Deprecated: macOS 15+
- `SkipUnlockWithWatch` (boolean): If `true`, the system skips the Unlock With Apple Watch pane. Available: macOS 12+
Deprecated: macOS 15+
- `SkipWallpaper` (boolean): If ‘true’, the system skips the Wallpaper selection window. Available: macOS 14.1+
Deprecated: macOS 15+

## See Also

- [object Accessibility](accessibility.md)
  The payload that configures the accessibility features of the device.
- [object Desktop](desktop.md)
  The payload that configures the desktop wallpaper.
- [object Dock](dock.md)
  The payload that configures the Dock.
- [object Finder](finder.md)
  The payload that configures Finder settings.
- [object HomeScreenLayout](homescreenlayout.md)
  The payload that configures the Home Screen layout.
- [object ManagedMenuExtras](managedmenuextras.md)
  The payload that configures menu extras.
- [object Notifications](notifications.md)
  The payload that configures notifications.
- [object ScreensaverUser](screensaveruser.md)
  The payload that configures a user’s screen saver settings.
- [object TimeMachine](timemachine.md)
  The payload that configures Time Machine.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/setupassistant)*
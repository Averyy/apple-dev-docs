# SetupAssistant

**Framework**: Device Management  
**Kind**: dictionary

The payload that configures Setup Assistant settings.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
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

- `SkipAccessibility` (boolean): If `true`, the system skips the Accessibility pane.
- `SkipAppearance` (boolean): If `true`, the system skips the Choose Your Look pane.
- `SkipCloudSetup` (boolean): If `true`, the system skips the Apple Account setup pane.
- `SkipiCloudStorageSetup` (boolean): If `true`, the system skips the iCloud Storage pane.
- `SkipPrivacySetup` (boolean): If `true`, the system skips the Privacy consent pane.
- `SkipScreenTime` (boolean): If `true`, the system skips the Screen Time pane.
- `SkipSetupItems` ([string]): An array of strings that describe the setup items to skip. [`SkipKeys`](skipkeys.md) provides a list of valid strings and their meanings. Available in iOS 14 and later, and macOS 15 and later.
- `SkipSiriSetup` (boolean): If `true`, the system skips the Siri setup pane.
- `SkipTouchIDSetup` (boolean): If `true`, the system skips the Touch ID setup pane.
- `SkipTrueTone` (boolean): If `true`, the system skips the True Tone Display pane.
- `SkipUnlockWithWatch` (boolean): If `true`, the system skips the Unlock With Apple Watch pane.
- `SkipWallpaper` (boolean): If ‘true’, the system skips the Wallpaper selection window.

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
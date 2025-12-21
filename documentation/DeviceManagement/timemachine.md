# TimeMachine

**Framework**: Device Management  
**Kind**: dictionary

The payload that configures Time Machine.

**Availability**:
- macOS 10.7+

## Declaration

```swift
object TimeMachine
```

#### Discussion

Specify `com.apple.MCX.TimeMachine` as the payload type.

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
            <key>AutoBackup</key>
            <true/>
            <key>BackupAllVolumes</key>
            <true/>
            <key>BackupDestURL</key>
            <string>server.example.com</string>
            <key>BackupSizeMB</key>
            <integer>1000</integer>
            <key>BackupSkipSys</key>
            <false/>
            <key>MobileBackups</key>
            <true/>
            <key>SkipPaths</key>
            <array>
                <string>/Users/Shared</string>
            </array>
            <key>PayloadIdentifier</key>
            <string>com.example.mytimemachinepayload</string>
            <key>PayloadType</key>
            <string>com.apple.MCX.TimeMachine</string>
            <key>PayloadUUID</key>
            <string>5f0be3a6-c9b8-44db-a2ae-414311772fdb</string>
            <key>PayloadVersion</key>
            <integer>1</integer>
        </dict>
    </array>
    <key>PayloadDisplayName</key>
    <string>Time Machine</string>
    <key>PayloadIdentifier</key>
    <string>com.example.myprofile</string>
    <key>PayloadType</key>
    <string>Configuration</string>
    <key>PayloadUUID</key>
    <string>68ca5f6c-13e8-43c3-b2ee-8bc405f5eed5</string>
    <key>PayloadVersion</key>
    <integer>1</integer>
</dict>
</plist>
```

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
- [object SetupAssistant](setupassistant.md)
  The payload that configures Setup Assistant settings.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/timemachine)*
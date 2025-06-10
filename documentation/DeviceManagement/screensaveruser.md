# ScreensaverUser

**Framework**: Device Management  
**Kind**: dictionary

The payload you use to configure a user’s screen-saver settings.

**Availability**:
- macOS 10.11+

## Declaration

```swift
object ScreensaverUser
```

#### Discussion

Specify `com.apple.screensaver.user` as the payload type.

##### Profile Availability

|  |  |
| --- | --- |
| Device channel | NA |
| User channel | macOS |
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
            <key>modulePath</key>
            <string>/System/Library/Screen Savers/Name.saver</string>
            <key>PayloadIdentifier</key>
            <string>com.example.myscreensaverpayload</string>
            <key>PayloadType</key>
            <string>com.apple.screensaver.user</string>
            <key>PayloadUUID</key>
            <string>c5dceece-f633-44e6-b899-9d46631fd6e5</string>
            <key>PayloadVersion</key>
            <integer>1</integer>
        </dict>
    </array>
    <key>PayloadDisplayName</key>
    <string>Screen Saver User</string>
    <key>PayloadIdentifier</key>
    <string>com.example.myprofile</string>
    <key>PayloadType</key>
    <string>Configuration</string>
    <key>PayloadUUID</key>
    <string>59332e00-d3c5-4d2a-a23a-ba36e45034e9</string>
    <key>PayloadVersion</key>
    <integer>1</integer>
</dict>
</plist>
```

## See Also

- [object Accessibility](accessibility.md)
  The payload you use to configure the accessibility features of the device.
- [object Desktop](desktop.md)
  The payload you use to configure the desktop.
- [object Dock](dock.md)
  The payload you use to configure the dock.
- [object Finder](finder.md)
  The payload you use to configure Finder settings.
- [object HomeScreenLayout](homescreenlayout.md)
  The payload you use to configure the Home screen layout.
- [object ManagedMenuExtras](managedmenuextras.md)
  The payload you use to configure menu extras.
- [object Notifications](notifications.md)
  The payload you use to configure notifications.
- [object SetupAssistant](setupassistant.md)
  The payload you use to configure setup-assistant settings.
- [object TimeMachine](timemachine.md)
  The payload you use to configure Time Machine.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/screensaveruser)*
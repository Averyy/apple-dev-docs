# Notifications

**Framework**: Device Management  
**Kind**: dictionary

The payload you use to configure notifications.

**Availability**:
- iOS 9.3+
- iPadOS 9.3+
- macOS 10.15+

## Declaration

```swift
object Notifications
```

#### Discussion

Specify `com.apple.notificationsettings` as the payload type.

##### Profile Availability

|  |  |
| --- | --- |
| Device channel | iOS, macOS, Shared iPad |
| User channel | macOS, Shared iPad |
| Allow manual install | iOS, macOS |
| Requires supervision | iOS |
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
            <key>NotificationSettings</key>
            <array>
                <dict>
                    <key>AlertType</key>
                    <integer>0</integer>
                    <key>BundleIdentifier</key>
                    <string>com.apple.mobilemail</string>
                    <key>NotificationsEnabled</key>
                    <false/>
                </dict>
            </array>
            <key>ShowInLockScreen</key>
            <true/>
            <key>PayloadIdentifier</key>
            <string>com.example.mynotificationspayload</string>
            <key>PayloadType</key>
            <string>com.apple.notificationsettings</string>
            <key>PayloadUUID</key>
            <string>d1cc23d9-f482-40c5-b7b1-332149659986</string>
            <key>PayloadVersion</key>
            <real>1</real>
        </dict>
    </array>
    <key>PayloadDisplayName</key>
    <string>Notification</string>
    <key>PayloadIdentifier</key>
    <string>com.example.myprofile</string>
    <key>PayloadType</key>
    <string>Configuration</string>
    <key>PayloadUUID</key>
    <string>2bb0ab2e-1e0a-4c03-a662-b4ee2ffe224a</string>
    <key>PayloadVersion</key>
    <integer>1</integer>
</dict>
</plist>
```

## Topics

### Objects
- [object Notifications.NotificationSettingsItem](notifications/notificationsettingsitem.md)
  The notification settings dictionary.

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
- [object ScreensaverUser](screensaveruser.md)
  The payload you use to configure a user’s screen-saver settings.
- [object SetupAssistant](setupassistant.md)
  The payload you use to configure setup-assistant settings.
- [object TimeMachine](timemachine.md)
  The payload you use to configure Time Machine.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/notifications)*
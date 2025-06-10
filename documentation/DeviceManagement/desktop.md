# Desktop

**Framework**: Device Management  
**Kind**: dictionary

The payload you use to configure the desktop.

**Availability**:
- macOS 10.10+

## Declaration

```swift
object Desktop
```

#### Discussion

Specify `com.apple.desktop` as the payload type.

##### Profile Availability

|  |  |
| --- | --- |
| Device channel | macOS |
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
            <key>locked</key>
            <true/>
            <key>override-picture-path</key>
            <string>~/Desktop/background.png</string>
            <key>PayloadIdentifier</key>
            <string>com.example.mydesktoppayload</string>
            <key>PayloadType</key>
            <string>com.apple.desktop</string>
            <key>PayloadUUID</key>
            <string>77a7ad50-9e32-4afb-8aee-79ae0c392848</string>
            <key>PayloadVersion</key>
            <integer>1</integer>
        </dict>
    </array>
    <key>PayloadDisplayName</key>
    <string>Desktop</string>
    <key>PayloadIdentifier</key>
    <string>com.example.myprofile</string>
    <key>PayloadType</key>
    <string>Configuration</string>
    <key>PayloadUUID</key>
    <string>2e00699a-8e37-417d-94b2-97b85ff722a2</string>
    <key>PayloadVersion</key>
    <integer>1</integer>
</dict>
</plist>
```

## See Also

- [object Accessibility](accessibility.md)
  The payload you use to configure the accessibility features of the device.
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
- [object ScreensaverUser](screensaveruser.md)
  The payload you use to configure a user’s screen-saver settings.
- [object SetupAssistant](setupassistant.md)
  The payload you use to configure setup-assistant settings.
- [object TimeMachine](timemachine.md)
  The payload you use to configure Time Machine.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/desktop)*
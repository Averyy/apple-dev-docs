# ManagedMenuExtras

**Framework**: Device Management  
**Kind**: dictionary

The payload you use to configure menu extras.

**Availability**:
- macOS 10.7+

## Declaration

```swift
object ManagedMenuExtras
```

#### Discussion

Specify `com.apple.mcxMenuExtras` as the payload type.

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
            <key>Battery.menu</key>
            <false/>
            <key>delaySeconds</key>
            <integer>30</integer>
            <key>maxWaitSeconds</key>
            <integer>60</integer>
            <key>PayloadIdentifier</key>
            <string>com.example.mymanagedmenuextraspayload</string>
            <key>PayloadType</key>
            <string>com.apple.mcxMenuExtras</string>
            <key>PayloadUUID</key>
            <string>93bd5b68-0141-4055-aaaf-a6cebc1cfeeb</string>
            <key>PayloadVersion</key>
            <integer>1</integer>
        </dict>
    </array>
    <key>PayloadDisplayName</key>
    <string>Menu Extras</string>
    <key>PayloadIdentifier</key>
    <string>com.example.myprofile</string>
    <key>PayloadType</key>
    <string>Configuration</string>
    <key>PayloadUUID</key>
    <string>dc2618ce-736c-4af7-b652-f9cdf3eb9ce4</string>
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
- [object Notifications](notifications.md)
  The payload you use to configure notifications.
- [object ScreensaverUser](screensaveruser.md)
  The payload you use to configure a user’s screen-saver settings.
- [object SetupAssistant](setupassistant.md)
  The payload you use to configure setup-assistant settings.
- [object TimeMachine](timemachine.md)
  The payload you use to configure Time Machine.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/managedmenuextras)*
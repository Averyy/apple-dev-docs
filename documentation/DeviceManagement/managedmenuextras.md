# ManagedMenuExtras

**Framework**: Device Management  
**Kind**: dictionary

The payload that configures menu extras.

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
  The payload that configures the accessibility features of the device.
- [object Desktop](desktop.md)
  The payload that configures the desktop wallpaper.
- [object Dock](dock.md)
  The payload that configures the Dock.
- [object Finder](finder.md)
  The payload that configures Finder settings.
- [object HomeScreenLayout](homescreenlayout.md)
  The payload that configures the Home Screen layout.
- [object Notifications](notifications.md)
  The payload that configures notifications.
- [object ScreensaverUser](screensaveruser.md)
  The payload that configures a user’s screen saver settings.
- [object SetupAssistant](setupassistant.md)
  The payload that configures Setup Assistant settings.
- [object TimeMachine](timemachine.md)
  The payload that configures Time Machine.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/managedmenuextras)*
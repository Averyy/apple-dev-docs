# Dock

**Framework**: Device Management  
**Kind**: dictionary

The payload that configures the Dock.

**Availability**:
- macOS 10.7+

## Declaration

```swift
object Dock
```

#### Discussion

Specify `com.apple.dock` as the payload type.

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
            <key>tilesize</key>
            <integer>40</integer>
            <key>size-immutable</key>
            <true/>
            <key>magnification</key>
            <true/>
            <key>magnify-immutable</key>
            <true/>
            <key>largesize</key>
            <integer>100</integer>
            <key>magsize-immutable</key>
            <true/>
            <key>orientation</key>
            <string>left</string>
            <key>position-immutable</key>
            <true/>
            <key>mineffect</key>
            <string>genie</string>
            <key>mineffect-immutable</key>
            <true/>
            <key>windowtabbing</key>
            <string>manual</string>
            <key>windowtabbing-immutable</key>
            <true/>
            <key>dblclickbehavior</key>
            <string>maximize</string>
            <key>dblclickbehavior-immutable</key>
            <true/>
            <key>minimize-to-application</key>
            <true/>
            <key>minintoapp-immutable</key>
            <true/>
            <key>launchanim</key>
            <true/>
            <key>launchanim-immutable</key>
            <true/>
            <key>autohide</key>
            <false/>
            <key>autohide-immutable</key>
            <true/>
            <key>show-process-indicators</key>
            <false/>
            <key>showindicators-immutable</key>
            <true/>
            <key>show-recents</key>
            <false/>
            <key>showrecents-immutable</key>
            <true/>
            <key>PayloadIdentifier</key>
            <string>com.example.mydockpayload</string>
            <key>PayloadType</key>
            <string>com.apple.dock</string>
            <key>PayloadUUID</key>
            <string>8d443602-52f2-48ff-aaa9-35b16c7c54c9</string>
            <key>PayloadVersion</key>
            <integer>1</integer>
        </dict>
    </array>
    <key>PayloadDisplayName</key>
    <string>Dock</string>
    <key>PayloadIdentifier</key>
    <string>com.example.myprofile</string>
    <key>PayloadType</key>
    <string>Configuration</string>
    <key>PayloadUUID</key>
    <string>c139d3e0-5468-43b0-90bf-5e05b2e8cd6f</string>
    <key>PayloadVersion</key>
    <integer>1</integer>
</dict>
</plist>
```

## Topics

### Objects
- [object Dock.StaticItem](dock/staticitem.md)
  Items that are located on the Documents side of the Dock and cannot be removed from that location.

## See Also

- [object Accessibility](accessibility.md)
  The payload that configures the accessibility features of the device.
- [object Desktop](desktop.md)
  The payload that configures the desktop wallpaper.
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
- [object TimeMachine](timemachine.md)
  The payload that configures Time Machine.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/dock)*
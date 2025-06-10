# Finder

**Framework**: Device Management  
**Kind**: dictionary

The payload you use to configure Finder settings.

**Availability**:
- macOS 10.7+

## Declaration

```swift
object Finder
```

#### Discussion

Specify `com.apple.finder` as the payload type.

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
            <key>InterfaceLevel</key>
            <string>Full</string>
            <key>ShowHardDrivesOnDesktop</key>
            <true/>
            <key>ShowExternalHardDrivesOnDesktop</key>
            <false/>
            <key>ShowRemovableMediaOnDesktop</key>
            <false/>
            <key>ShowMountedServersOnDesktop</key>
            <true/>
            <key>WarnOnEmptyTrash</key>
            <true/>
            <key>ProhibitConnectTo</key>
            <true/>
            <key>ProhibitEject</key>
            <true/>
            <key>ProhibitBurn</key>
            <true/>
            <key>ProhibitGoToFolder</key>
            <true/>
            <key>PayloadIdentifier</key>
            <string>com.example.myfinderpayload</string>
            <key>PayloadType</key>
            <string>com.apple.finder</string>
            <key>PayloadUUID</key>
            <string>feea617a-c8f2-4dce-afae-20b2fe5f9c9b</string>
            <key>PayloadVersion</key>
            <integer>1</integer>
        </dict>
    </array>
    <key>PayloadDisplayName</key>
    <string>Finder</string>
    <key>PayloadIdentifier</key>
    <string>com.example.myprofile</string>
    <key>PayloadType</key>
    <string>Configuration</string>
    <key>PayloadUUID</key>
    <string>2527bd12-fbc4-4957-a9e7-4afeb64e0246</string>
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

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/finder)*
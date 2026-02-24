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

## Properties

- `AirPort.menu` (boolean): If `true`, enables the AirPort menu extra.
- `Battery.menu` (boolean): If `true`, enables the Battery menu extra.
- `Bluetooth.menu` (boolean): If `true`, enables the Bluetooth menu extra.
- `Clock.menu` (boolean): If `true`, enables the Clock menu extra.
- `CPU.menu` (boolean): If `true`, enables the CPU menu extra.
- `delaySeconds` (number): The number of seconds to delay after login before adding or removing menu extras. If the delay is too short, the menu extras don’t appear, or disappear from the menu bar.
- `Displays.menu` (boolean): If `true`, enables the Displays menu extra.
- `Eject.menu` (boolean): If `true`, enables the Eject menu extra.
- `Fax.menu` (boolean): If `true`, enables the Fax menu extra.
- `HomeSync.menu` (boolean): If `true`, enables the HomeSync menu extra.
- `iChat.menu` (boolean): If `true`, enables the iChat menu extra.
- `Ink.menu` (boolean): If `true`, enables the Ink menu extra.
- `IrDA.menu` (boolean): If `true`, enables the IrDA menu extra.
- `maxWaitSeconds` (number): The maximum wait, in seconds, for all menu extras to be added or removed.
- `PCCard.menu` (boolean): If `true`, enables the PCCard menu extra.
- `PPP.menu` (boolean): If `true`, enables the PPP menu extra.
- `PPPoE.menu` (boolean): If `true`, enables the PPPoE menu extra.
- `RemoteDesktop.menu` (boolean): If `true`, enables the Remote Desktop menu extra.
- `Script Menu.menu` (boolean): If `true`, enables the Script menu extra.
- `Spaces.menu` (boolean): If `true`, enables the Spaces menu extra.
- `Sync.menu` (boolean): If `true`, enables the Sync menu extra.
- `TextInput.menu` (boolean): If `true`, enables the Text Input menu extra.
- `TimeMachine.menu` (boolean): If `true`, enables the TimeMachine menu extra.
- `UniversalAccess.menu` (boolean): If `true`, enables the Universal Access menu extra.
- `User.menu` (boolean): If `true`, enables the User menu extra.
- `Volume.menu` (boolean): If `true`, enables the Volume menu extra.
- `VPN.menu` (boolean): If `true`, enables the VPN menu extra.
- `WWAN.menu` (boolean): If `true`, enables the WWAN menu extra.

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
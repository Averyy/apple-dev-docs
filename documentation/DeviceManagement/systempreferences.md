# SystemPreferences

**Framework**: Device Management  
**Kind**: dictionary  
**Role**: Device Management Profile

The payload that configures the preference panes.

**Availability**:
- macOS 10.7+ - Deprecated in 13.0

## Declaration

```
object SystemPreferences
```

#### Discussion

Specify `com.apple.systempreferences` as the payload type.

##### Profile availability

|  |  |
| --- | --- |
| Device channel | macOS |
| User channel | macOS |
| Allow manual install | macOS |
| Requires supervision | N/A |
| Requires user-approved MDM | N/A |
| Allowed in user enrollment | N/A |
| Allow multiple payloads | N/A |

##### Profile example

```plist
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>PayloadContent</key>
    <array>
        <dict>
            <key>EnabledPreferencePanes</key>
            <array>
                <string>com.apple.preferences.users</string>
            </array>
            <key>DisabledPreferencePanes</key>
            <array>
                <string>com.apple.preference.dock</string>
            </array>
            <key>PayloadIdentifier</key>
            <string>com.example.mysystempayload</string>
            <key>PayloadType</key>
            <string>com.apple.systempreferences</string>
            <key>PayloadUUID</key>
            <string>6e7d6ddc-70fc-4126-a0a3-c312c4e16e06</string>
            <key>PayloadVersion</key>
            <integer>1</integer>
        </dict>
    </array>
    <key>PayloadDisplayName</key>
    <string>System Preferences</string>
    <key>PayloadIdentifier</key>
    <string>com.example.myprofile</string>
    <key>PayloadType</key>
    <string>Configuration</string>
    <key>PayloadUUID</key>
    <string>28114fac-d230-484f-8747-4f3f1077f95c</string>
    <key>PayloadVersion</key>
    <integer>1</integer>
</dict>
</plist>
```

## Properties

- `DisabledPreferencePanes` ([string]) *(deprecated)*: The list of disabled System Preferences panes.

  Deprecated: macOS 13+

  **Allowed Values**: `com.apple.ClassroomSettings`, `com.apple.Localization`, `com.apple.preference.datetime`, `com.apple.preference.desktopscreeneffect`, `com.apple.preference.digihub.discs`, `com.apple.preference.displays`, `com.apple.preference.dock`, `com.apple.preference.energysaver`, `com.apple.preference.expose`, `com.apple.preference.general`, `com.apple.preference.ink`, `com.apple.preference.keyboard`, `com.apple.preference.mouse`, `com.apple.preference.network`, `com.apple.preference.notifications`, `com.apple.preference.printfax`, `com.apple.preference.screentime`, `com.apple.preference.security`, `com.apple.preference.sidecar`, `com.apple.preference.sound`, `com.apple.preference.speech`, `com.apple.preference.spotlight`, `com.apple.preference.startupdisk`, `com.apple.preference.trackpad`, `com.apple.preference.universalaccess`, `com.apple.preferences.AppleIDPrefPane`, `com.apple.preferences.appstore`, `com.apple.preferences.Bluetooth`, `com.apple.preferences.configurationprofiles`, `com.apple.preferences.extensions`, `com.apple.preferences.FamilySharingPrefPane`, `com.apple.preferences.icloud`, `com.apple.preferences.internetaccounts`, `com.apple.preferences.parentalcontrols`, `com.apple.preferences.password`, `com.apple.preferences.sharing`, `com.apple.preferences.softwareupdate`, `com.apple.preferences.users`, `com.apple.preferences.wallet`, `com.apple.prefpanel.fibrechannel`, `com.apple.prefs.backup`, `com.apple.Xsan`
- `DisabledSystemSettings` ([string]) *(deprecated)*: The list of disabled System Settings extensions. The device enables all other items. When you specify `DisabledSystemSettings`, the device ignores `DisabledPreferencePanes` and `EnabledPreferencePanes`.

  > **Note**:  A given System Settings extension can supply more than one section in System Settings; disabling such an extension disables all sections it supplies.

  Available: macOS 13+
  Deprecated: macOS 13+

  **Allowed Values**: `com.apple.Accessibility-Settings.extension`, `com.apple.AirDrop-Handoff-Settings.extension`, `com.apple.Battery-Settings.extension`, `com.apple.BluetoothSettings`, `com.apple.CD-DVD-Settings.extension`, `com.apple.ClassKit-Settings.extension`, `com.apple.Classroom-Settings.extension`, `com.apple.ControlCenter-Settings.extension`, `com.apple.Date-Time-Settings.extension`, `com.apple.Desktop-Settings.extension`, `com.apple.Displays-Settings.extension`, `com.apple.ExtensionsPreferences`, `com.apple.Family-Settings.extension`, `com.apple.Focus-Settings.extension`, `com.apple.Game-Center-Settings.extension`, `com.apple.Game-Controller-Settings.extension`, `com.apple.HeadphoneSettings`, `com.apple.Internet-Accounts-Settings.extension`, `com.apple.Keyboard-Settings.extension`, `com.apple.Localization-Settings.extension`, `com.apple.Lock-Screen-Settings.extension`, `com.apple.LoginItems-Settings.extension`, `com.apple.Mouse-Settings.extension`, `com.apple.Network-Settings.extension`, `com.apple.NetworkExtensionSettingsUI.NESettingsUIExtension`, `com.apple.Notifications-Settings.extension`, `com.apple.Passwords-Settings.extension`, `com.apple.Print-Scan-Settings.extension`, `com.apple.Screen-Time-Settings.extension`, `com.apple.ScreenSaver-Settings.extension`, `com.apple.Sharing-Settings.extension`, `com.apple.Siri-Settings.extension`, `com.apple.Software-Update-Settings.extension`, `com.apple.Sound-Settings.extension`, `com.apple.Startup-Disk-Settings.extension`, `com.apple.Time-Machine-Settings.extension`, `com.apple.Touch-ID-Settings.extension`, `com.apple.Trackpad-Settings.extension`, `com.apple.Transfer-Reset-Settings.extension`, `com.apple.Users-Groups-Settings.extension`, `com.apple.WalletSettingsExtension`, `com.apple.Wallpaper-Settings.extension`, `com.apple.settings.Storage`, `com.apple.systempreferences.AppleIDSettings`, `com.apple.wifi-settings-extension`
- `EnabledPreferencePanes` ([string]) *(deprecated)*: The list of enabled System Preferences panes.

  Deprecated: macOS 13+

  **Allowed Values**: `com.apple.ClassroomSettings`, `com.apple.Localization`, `com.apple.preference.datetime`, `com.apple.preference.desktopscreeneffect`, `com.apple.preference.digihub.discs`, `com.apple.preference.displays`, `com.apple.preference.dock`, `com.apple.preference.energysaver`, `com.apple.preference.expose`, `com.apple.preference.general`, `com.apple.preference.ink`, `com.apple.preference.keyboard`, `com.apple.preference.mouse`, `com.apple.preference.network`, `com.apple.preference.notifications`, `com.apple.preference.printfax`, `com.apple.preference.screentime`, `com.apple.preference.security`, `com.apple.preference.sidecar`, `com.apple.preference.sound`, `com.apple.preference.speech`, `com.apple.preference.spotlight`, `com.apple.preference.startupdisk`, `com.apple.preference.trackpad`, `com.apple.preference.universalaccess`, `com.apple.preferences.AppleIDPrefPane`, `com.apple.preferences.appstore`, `com.apple.preferences.Bluetooth`, `com.apple.preferences.configurationprofiles`, `com.apple.preferences.extensions`, `com.apple.preferences.FamilySharingPrefPane`, `com.apple.preferences.icloud`, `com.apple.preferences.internetaccounts`, `com.apple.preferences.parentalcontrols`, `com.apple.preferences.password`, `com.apple.preferences.sharing`, `com.apple.preferences.softwareupdate`, `com.apple.preferences.users`, `com.apple.preferences.wallet`, `com.apple.prefpanel.fibrechannel`, `com.apple.prefs.backup`, `com.apple.Xsan`

## See Also

### Deprecated
- [object APN](./apn.md)
  The payload that configures access point names.
- [object FDERecoveryKeyRedirection](./fderecoverykeyredirection.md)
  The payload that configures FileVault recovery key redirection.
- [object MediaManagementAllowedMedia](./mediamanagementallowedmedia.md)
  The payload that configures media management.
- [object ParentalControlDictationAndProfanity](./parentalcontroldictationandprofanity.md)
  The payload that configures parental control for dictation and profanity.
- [object ShareKit](./sharekit.md)
  The payload that configures ShareKit.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/systempreferences)*
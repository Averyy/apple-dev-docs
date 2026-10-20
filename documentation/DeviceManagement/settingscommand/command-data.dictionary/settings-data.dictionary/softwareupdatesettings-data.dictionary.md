# SettingsCommand.Command.Settings.SoftwareUpdateSettings

**Framework**: Device Management  
**Kind**: dictionary  
**Role**: Device Management Command

A dictionary that contains software update settings.

**Availability**:
- iOS 14.5+ - Deprecated in 26.0
- iPadOS 14.5+ - Deprecated in 26.0
- Mac Catalyst 14.5+ - Deprecated in 26.0

## Declaration

```
object SettingsCommand.Command.Settings.SoftwareUpdateSettings
```

## Properties

- `Item` (string) *(required)* *(deprecated)*: ~~A string that represents the type of updates that should appear in the Software Update pane in Settings. Supervised only.~~

  ~~Deprecated: iOS 26+ | iPadOS 26+~~
  Removed: iOS 27+ | iPadOS 27+

  **Allowed Values**: `SoftwareUpdateSettings`
- `RecommendationCadence` (integer) *(required)* *(deprecated)*: ~~This value defines how the system presents software updates to the user. When there’s more than one available update for the user, the system behaves as follows:~~

  ~~- `0`: Presents both options to the user.~~ ~~- `1`: Presents the lower numbered (oldest) software update version.~~ ~~- `2`: Presents only the highest numbered (most recent) release available for the device.~~

  ~~This value has no effect when there’s only one available update; the system shows the single available update to the user regardless of the value of this setting.~~

  ~~Deprecated: iOS 26+ | iPadOS 26+~~
  Removed: iOS 27+ | iPadOS 27+

  **Allowed Values**: `0`, `1`, `2`

## See Also

### Objects
- [object SettingsCommand.Command.Settings.AccessibilitySettings](./accessibilitysettings-data.dictionary.md)
  A dictionary that contains settings for accessibility.
- [object SettingsCommand.Command.Settings.AppAnalytics](./appanalytics-data.dictionary.md)
  A dictionary that contains settings for sharing app analytics.
- [object SettingsCommand.Command.Settings.ApplicationAttributes](./applicationattributes-data.dictionary.md)
  A dictionary that contains the attributes to apply to the app.
- [object SettingsCommand.Command.Settings.ApplicationConfiguration](./applicationconfiguration-data.dictionary.md)
  A dictionary that contains the configurations to apply to the app.
- [object SettingsCommand.Command.Settings.Bluetooth](./bluetooth-data.dictionary.md)
  A dictionary that contains Bluetooth settings.
- [object SettingsCommand.Command.Settings.DataRoaming](./dataroaming-data.dictionary.md)
  A dictionary that contains data roaming settings.
- [object SettingsCommand.Command.Settings.DefaultApplications](./defaultapplications-data.dictionary.md)
  A dictionary that contains default application bundle identifiers for each default application type that can be set.
- [object SettingsCommand.Command.Settings.DeviceName](./devicename-data.dictionary.md)
  A dictionary that contains device name settings.
- [object SettingsCommand.Command.Settings.DiagnosticSubmission](./diagnosticsubmission-data.dictionary.md)
  A dictionary that contains diagnostic submission settings.
- [object SettingsCommand.Command.Settings.HostName](./hostname-data.dictionary.md)
  A dictionary that contains hostname settings.
- [object SettingsCommand.Command.Settings.MDMOptions](./mdmoptions-data.dictionary.md)
  A dictionary that contains settings about the organization operating the MDM server.
- [object SettingsCommand.Command.Settings.MaximumResidentUsers](./maximumresidentusers-data.dictionary.md)
  A dictionary that contains settings for maximum resident users.
- [object SettingsCommand.Command.Settings.OrganizationInfo](./organizationinfo-data.dictionary.md)
  A dictionary that contains settings about the organization operating the MDM server.
- [object SettingsCommand.Command.Settings.PasscodeLockGracePeriod](./passcodelockgraceperiod-data.dictionary.md)
  A dictionary that contains settings for the password lock grace period.
- [object SettingsCommand.Command.Settings.PersonalHotspot](./personalhotspot-data.dictionary.md)
  A dictionary that contains Personal Hotspot settings.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/settingscommand/command-data.dictionary/settings-data.dictionary/softwareupdatesettings-data.dictionary)*
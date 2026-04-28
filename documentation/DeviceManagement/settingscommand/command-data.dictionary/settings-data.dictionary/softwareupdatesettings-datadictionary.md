# SettingsCommand.Command.Settings.SoftwareUpdateSettings

**Framework**: Device Management  
**Kind**: dictionary

A dictionary that contains software update settings.

**Availability**:
- iOS 14.5+
- iPadOS 14.5+
- Mac Catalyst 14.5+
- Device Assignment Services ?+
- VPP License Management ?+

## Declaration

```swift
object SettingsCommand.Command.Settings.SoftwareUpdateSettings
```

## Properties

- `Item` (string) *(required)*: A string that represents the type of updates that should appear in the Software Update pane in Settings. Supervised only.
- `RecommendationCadence` (integer) *(required)*: This value defines how the system presents software updates to the user. When there’s more than one available update for the user, the system behaves as follows: - `0`: Presents both options to the user.
- `1`: Presents the lower numbered (oldest) software update version.
- `2`: Presents only the highest numbered (most recent) release available for the device. This value has no effect when there’s only one available update; the system shows the single available update to the user regardless of the value of this setting. Available in iOS 14.5 and later.

## See Also

- [object SettingsCommand.Command.Settings.AccessibilitySettings](settingscommand/command-data.dictionary/settings-data.dictionary/accessibilitysettings-data.dictionary.md)
  A dictionary that contains settings for accessibility.
- [object SettingsCommand.Command.Settings.AppAnalytics](settingscommand/command-data.dictionary/settings-data.dictionary/appanalytics-data.dictionary.md)
  A dictionary that contains settings for sharing app analytics.
- [object SettingsCommand.Command.Settings.ApplicationAttributes](settingscommand/command-data.dictionary/settings-data.dictionary/applicationattributes-data.dictionary.md)
  A dictionary that contains the attributes to apply to the app.
- [object SettingsCommand.Command.Settings.ApplicationConfiguration](settingscommand/command-data.dictionary/settings-data.dictionary/applicationconfiguration-data.dictionary.md)
  A dictionary that contains the configurations to apply to the app.
- [object SettingsCommand.Command.Settings.Bluetooth](settingscommand/command-data.dictionary/settings-data.dictionary/bluetooth-data.dictionary.md)
  A dictionary that contains Bluetooth settings.
- [object SettingsCommand.Command.Settings.DataRoaming](settingscommand/command-data.dictionary/settings-data.dictionary/dataroaming-data.dictionary.md)
  A dictionary that contains data roaming settings.
- [object SettingsCommand.Command.Settings.DefaultApplications](settingscommand/command-data.dictionary/settings-data.dictionary/defaultapplications-data.dictionary.md)
  A dictionary that contains default application bundle identifiers for each default application type that can be set.
- [object SettingsCommand.Command.Settings.DeviceName](settingscommand/command-data.dictionary/settings-data.dictionary/devicename-data.dictionary.md)
  A dictionary that contains device name settings.
- [object SettingsCommand.Command.Settings.DiagnosticSubmission](settingscommand/command-data.dictionary/settings-data.dictionary/diagnosticsubmission-data.dictionary.md)
  A dictionary that contains diagnostic submission settings.
- [object SettingsCommand.Command.Settings.HostName](settingscommand/command-data.dictionary/settings-data.dictionary/hostname-data.dictionary.md)
  A dictionary that contains hostname settings.
- [object SettingsCommand.Command.Settings.MDMOptions](settingscommand/command-data.dictionary/settings-data.dictionary/mdmoptions-data.dictionary.md)
  A dictionary that contains settings about the organization operating the MDM server.
- [object SettingsCommand.Command.Settings.MaximumResidentUsers](settingscommand/command-data.dictionary/settings-data.dictionary/maximumresidentusers-data.dictionary.md)
  A dictionary that contains settings for maximum resident users.
- [object SettingsCommand.Command.Settings.OrganizationInfo](settingscommand/command-data.dictionary/settings-data.dictionary/organizationinfo-data.dictionary.md)
  A dictionary that contains settings about the organization operating the MDM server.
- [object SettingsCommand.Command.Settings.PasscodeLockGracePeriod](settingscommand/command-data.dictionary/settings-data.dictionary/passcodelockgraceperiod-data.dictionary.md)
  A dictionary that contains settings for the password lock grace period.
- [object SettingsCommand.Command.Settings.PersonalHotspot](settingscommand/command-data.dictionary/settings-data.dictionary/personalhotspot-data.dictionary.md)
  A dictionary that contains Personal Hotspot settings.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/settingscommand/command-data.dictionary/settings-data.dictionary/softwareupdatesettings-data.dictionary)*
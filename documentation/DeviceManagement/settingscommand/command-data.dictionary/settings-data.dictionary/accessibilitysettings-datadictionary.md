# SettingsCommand.Command.Settings.AccessibilitySettings

**Framework**: Device Management  
**Kind**: dictionary

A dictionary that contains settings for accessibility.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- watchOS 10.0+

## Declaration

```swift
object SettingsCommand.Command.Settings.AccessibilitySettings
```

## Properties

- `BoldTextEnabled` (boolean): If `true`, the system enables bold text.
- `GrayscaleEnabled` (boolean): If `true`, the system enables grayscale display.
- `IncreaseContrastEnabled` (boolean): If `true`, the system enables increase contrast. Available: iOS 16+ | iPadOS 16+
- `Item` (string) *(required)*: Sets various accessibility settings. The system allows only keys with explicitly provided values.
- `ReduceMotionEnabled` (boolean): If `true`, the system enables reduced motion.
- `ReduceTransparencyEnabled` (boolean): If `true`, the system enables reduced transparency.
- `TextSize` (integer): The accessibility text size apps that support dynamic text use. `0` is the smallest value, and `11` is the largest available.
- `TouchAccommodationsEnabled` (boolean): If `true`, the system enables touch accommodations.
- `VoiceOverEnabled` (boolean): If `true`, the system enables voiceover.
- `ZoomEnabled` (boolean): If `true`, the system enables zoom.

## See Also

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
- [object SettingsCommand.Command.Settings.SharedDeviceConfiguration](settingscommand/command-data.dictionary/settings-data.dictionary/shareddeviceconfiguration-data.dictionary.md)
  A dictionary that contains shared device configuration settings.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/settingscommand/command-data.dictionary/settings-data.dictionary/accessibilitysettings-data.dictionary)*
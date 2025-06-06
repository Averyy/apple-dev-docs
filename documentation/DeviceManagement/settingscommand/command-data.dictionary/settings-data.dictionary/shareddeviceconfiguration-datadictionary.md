# SettingsCommand.Command.Settings.SharedDeviceConfiguration

**Framework**: Device Management  
**Kind**: dictionary

A dictionary that contains shared device configuration settings.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.1+
- watchOS 10.0+
- Device Assignment Services ?+
- VPP License Management ?+

## Declaration

```swift
object SettingsCommand.Command.Settings.SharedDeviceConfiguration
```

#### Discussion

This setting doesn’t support user enrollment, and is available in iOS 13.4 and later for Shared iPad.

Apply this setting before users log in to the device. If you upgraded the device to iOS 13.4 or later, perform an erase of all content and settings before applying this setting. Provide either the `QuotaSize` or `ResidentUsers`. If you provide both values, the MDM server uses `QuotaSize`.

## Topics

### Commands
- [object SettingsCommand.Command.Settings.SharedDeviceConfiguration.AwaitUserConfiguration](settingscommand/command-data.dictionary/settings-data.dictionary/shareddeviceconfiguration-data.dictionary/awaituserconfiguration-data.dictionary.md)
  Enables the user configuration Setup Assistant workflow.
- [object SettingsCommand.Command.Settings.SharedDeviceConfiguration.PasscodePolicy](settingscommand/command-data.dictionary/settings-data.dictionary/shareddeviceconfiguration-data.dictionary/passcodepolicy-data.dictionary.md)
  A dictionary that contains passcode policies.

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
- [object SettingsCommand.Command.Settings.DeviceName](settingscommand/command-data.dictionary/settings-data.dictionary/devicename-data.dictionary.md)
  A dictionary that contains device name settings.
- [object SettingsCommand.Command.Settings.DiagnosticSubmission](settingscommand/command-data.dictionary/settings-data.dictionary/diagnosticsubmission-data.dictionary.md)
  A dictionary that contains diagnostic submission settings.
- [object SettingsCommand.Command.Settings.HostName](settingscommand/command-data.dictionary/settings-data.dictionary/hostname-data.dictionary.md)
  A dictionary that contains hostname settings.
- [object SettingsCommand.Command.Settings.MDMOptions](settingscommand/command-data.dictionary/settings-data.dictionary/mdmoptions-data.dictionary.md)
  A dictionary that contains settings about the organization operating the MDM server.
- [object SettingsCommand.Command.Settings.OrganizationInfo](settingscommand/command-data.dictionary/settings-data.dictionary/organizationinfo-data.dictionary.md)
  A dictionary that contains settings about the organization operating the MDM server.
- [object SettingsCommand.Command.Settings.PersonalHotspot](settingscommand/command-data.dictionary/settings-data.dictionary/personalhotspot-data.dictionary.md)
  A dictionary that contains Personal Hotspot settings.
- [object SettingsCommand.Command.Settings.SoftwareUpdateSettings](settingscommand/command-data.dictionary/settings-data.dictionary/softwareupdatesettings-data.dictionary.md)
  A dictionary that contains software update settings.
- [object SettingsCommand.Command.Settings.TimeZone](settingscommand/command-data.dictionary/settings-data.dictionary/timezone-data.dictionary.md)
  A dictionary that contains time zone settings.
- [object SettingsCommand.Command.Settings.Wallpaper](settingscommand/command-data.dictionary/settings-data.dictionary/wallpaper-data.dictionary.md)
  A dictionary that contains wallpaper settings.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/settingscommand/command-data.dictionary/settings-data.dictionary/shareddeviceconfiguration-data.dictionary)*
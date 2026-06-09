# SettingsCommand.Command.Settings

**Framework**: Device Management  
**Kind**: dictionary

An array of dictionaries that contains the settings.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 5.0+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.1+
- watchOS 10.0+

## Declaration

```swift
object SettingsCommand.Command.Settings
```

## Topics

### Objects
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
- [object SettingsCommand.Command.Settings.SharedDeviceConfiguration](settingscommand/command-data.dictionary/settings-data.dictionary/shareddeviceconfiguration-data.dictionary.md)
  A dictionary that contains shared device configuration settings.
- [object SettingsCommand.Command.Settings.TimeZone](settingscommand/command-data.dictionary/settings-data.dictionary/timezone-data.dictionary.md)
  A dictionary that contains time zone settings.
- [object SettingsCommand.Command.Settings.VoiceRoaming](settingscommand/command-data.dictionary/settings-data.dictionary/voiceroaming-data.dictionary.md)
  A dictionary that contains voice roaming settings.
- [object SettingsCommand.Command.Settings.Wallpaper](settingscommand/command-data.dictionary/settings-data.dictionary/wallpaper-data.dictionary.md)
  A dictionary that contains wallpaper settings.

## Properties

- `AccessibilitySettings` (SettingsCommand.Command.Settings.AccessibilitySettings): A dictionary that contains accessibility settings. Available: iOS 16+ | iPadOS 16+ | watchOS 10+
- `AppAnalytics` (SettingsCommand.Command.Settings.AppAnalytics): A dictionary that contains settings for sharing app analytics. This setting is available only for Shared iPad in iOS 9.3.2 and later. Available: iOS 9.3.2+ | iPadOS 9.3.2+
- `ApplicationAttributes` (SettingsCommand.Command.Settings.ApplicationAttributes): A dictionary that contains the attributes to apply to the app. Omit this setting to remove existing attributes. This setting supports user enrollment. This setting fails for apps that Declarative Device Management manages. Available: iOS 7+ | iPadOS 7+ | tvOS 10.2+ | visionOS 1.1+ | watchOS 10+
- `ApplicationConfiguration` (SettingsCommand.Command.Settings.ApplicationConfiguration): A dictionary that contains the configurations to apply to the app. Omit this setting to remove existing configurations. This setting requires the App Management access right, supports user enrollment. This setting fails for apps that Declarative Device Management manages. Available: iOS 7+ | iPadOS 7+ | macOS 10.15+ | tvOS 10.2+ | visionOS 1.1+ | watchOS 10+
- `Bluetooth` (SettingsCommand.Command.Settings.Bluetooth): A dictionary that contains Bluetooth settings. This setting requires the Network Information access right, doesn’t support user enrollment, and is available only on supervised devices. Available: iOS 11.3+ | iPadOS 11.3+ | macOS 10.13.4+
- `DataRoaming` (SettingsCommand.Command.Settings.DataRoaming): A dictionary that contains data roaming settings. This setting requires the Network Information access right, and doesn’t support user enrollment. Available: iOS 5+ | iPadOS 5+
- `DefaultApplications` (SettingsCommand.Command.Settings.DefaultApplications): A dictionary that contains default application bundle identifiers for each default application type that can be set.
- `DeviceName` (SettingsCommand.Command.Settings.DeviceName): A dictionary that contains device name settings. This setting doesn’t support user enrollment, and is available only on supervised devices. Available: iOS 5+ | iPadOS 5+ | macOS 10.10+ | tvOS 9+ | visionOS 2+
- `DiagnosticSubmission` (SettingsCommand.Command.Settings.DiagnosticSubmission): A dictionary that contains diagnostic submission settings. This setting is available only for Shared iPad in iOS 9.3 and later. Available: iOS 9.3+ | iPadOS 9.3+
- `HostName` (SettingsCommand.Command.Settings.HostName): A dictionary that contains hostname settings. This setting doesn’t support user enrollment. Available: macOS 10.11+
- `MaximumResidentUsers` (SettingsCommand.Command.Settings.MaximumResidentUsers): A dictionary that contains settings for maximum resident users. Apple deprecated this setting in iOS 13.4. Use ’SharedDeviceConfiguration` instead. This setting is available only for Shared iPad. Available: iOS 9.3+ | iPadOS 9.3+
Deprecated: iOS 13.4+ | iPadOS 13.4+
- `MDMOptions` (SettingsCommand.Command.Settings.MDMOptions): A dictionary that contains settings related to the MDM protocol. This setting doesn’t support user enrollment. Available: iOS 7+ | iPadOS 7+ | macOS 10.15+ | visionOS 2+
- `OrganizationInfo` (SettingsCommand.Command.Settings.OrganizationInfo): A dictionary that contains settings about the organization operating the MDM server. This setting supports user enrollment.
- `PasscodeLockGracePeriod` (SettingsCommand.Command.Settings.PasscodeLockGracePeriod): A dictionary that contains password lock grace period settings. This setting is available only for Shared iPad in iOS 9.3.2 and later. This key is deprecated. Use ‘PasscodeLockGracePeriod’ in SettingsCommand.Command.Settings.SharedDeviceConfiguration.PasscodePolicy instead. Available: iOS 9.3.2+ | iPadOS 9.3.2+
Deprecated: iOS 17+ | iPadOS 17+
- `PersonalHotspot` (SettingsCommand.Command.Settings.PersonalHotspot): A dictionary that contains Personal Hotspot settings. This setting requires the Network Information access right, and doesn’t support user enrollment. Available: iOS 5+ | iPadOS 5+
- `SharedDeviceConfiguration` (SettingsCommand.Command.Settings.SharedDeviceConfiguration): A dictionary that contains shared device configuration settings. This setting is available only for Shared iPad in iOS 13.4 and later. Available: iOS 13.4+ | iPadOS 13.4+
- `TimeZone` (SettingsCommand.Command.Settings.TimeZone): A dictionary that contains time zone settings. This setting is available only on supervised devices and doesn’t support user enrollment. Available: iOS 14+ | iPadOS 14+ | tvOS 14+ | visionOS 2+
- `VoiceRoaming` (SettingsCommand.Command.Settings.VoiceRoaming): A dictionary that contains voice roaming settings. This setting requires the Network Information access right, and doesn’t support user enrollment. Available: iOS 5+ | iPadOS 5+
Deprecated: iOS 16+ | iPadOS 16+
- `Wallpaper` (SettingsCommand.Command.Settings.Wallpaper): A dictionary that contains wallpaper settings. This setting doesn’t support user enrollment. Starting in iOS 16 and iPadOS 17, when setting the wallpaper for the first time, both locations update. After that, you can set either location separately. Available: iOS 8+ | iPadOS 8+


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/settingscommand/command-data.dictionary/settings-data.dictionary)*
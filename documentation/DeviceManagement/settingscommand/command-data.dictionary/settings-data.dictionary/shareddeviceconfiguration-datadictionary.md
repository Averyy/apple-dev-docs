# SettingsCommand.Command.Settings.SharedDeviceConfiguration

**Framework**: Device Management  
**Kind**: dictionary

A dictionary that contains shared device configuration settings.

**Availability**:
- iOS 13.4+
- iPadOS 13.4+
- Mac Catalyst 13.4+

## Declaration

```swift
object SettingsCommand.Command.Settings.SharedDeviceConfiguration
```

## Topics

### Objects
- [object SettingsCommand.Command.Settings.SharedDeviceConfiguration.AwaitUserConfiguration](settingscommand/command-data.dictionary/settings-data.dictionary/shareddeviceconfiguration-data.dictionary/awaituserconfiguration-data.dictionary.md)
  Enables the user configuration Setup Assistant workflow.
- [object SettingsCommand.Command.Settings.SharedDeviceConfiguration.PasscodePolicy](settingscommand/command-data.dictionary/settings-data.dictionary/shareddeviceconfiguration-data.dictionary/passcodepolicy-data.dictionary.md)
  A dictionary that contains passcode policies.

## Properties

- `AwaitUserConfiguration` (SettingsCommand.Command.Settings.SharedDeviceConfiguration.AwaitUserConfiguration): If enabled, the Shared iPad device enters Setup Assistant after the user triggers a login. The MDM server has a chance to configure the device and user. After configuration, the server needs to send a [`User Configured`](user-configured-command.md) command to the user channel to unblock the login. This feature requires the device to have network access during the login process. Available: iOS 17+ | iPadOS 17+
- `Item` (string) *(required)*: A string that identifies this setting. Available: iOS 13.4+ | iPadOS 13.4+ | visionOS 26+
- `ManagedAppleIDDefaultDomains` ([string]): A list of domains that the Shared iPad login screen displays. The user can pick a domain from the list to complete their Managed Apple Account. If this list contains more than 3 domains, the system picks 3 at random for display. Available: iOS 16+ | iPadOS 16+
- `OnlineAuthenticationGracePeriod` (integer): A grace period (in days) for Shared iPad online authentication. The Shared iPad only verifies the user’s passcode locally during login for users that already exist on the device. However, the system requires an online authentication (against Apple’s identity server) after the number of days specified by this setting. Setting this value to 0 enforces online authentication every time. Available: iOS 16+ | iPadOS 16+
- `PasscodePolicy` (SettingsCommand.Command.Settings.SharedDeviceConfiguration.PasscodePolicy): A dictionary that contains passcode policies. Available: iOS 17+ | iPadOS 17+
- `QuotaSize` (integer): The quota size, in megabytes (MB), for each user on the shared device, or if the quota size is too small, the minimum quota size. Available to Temporary Sessions Only guest users on iOS 17+.
- `ResidentUsers` (integer): The expected number of users. If this value is greater than the value for the maximum possible number of users that the device supports, the MDM server uses that value instead.
- `SkipLanguageAndLocaleSetupForNewUsers` (boolean): If `true`, the system picks the system language and locale automatically for the new Shared iPad user. Available: iOS 16.2+ | iPadOS 16.2+
- `TemporarySessionOnly` (boolean): If `true`, the user only sees the Guest Welcome pane and can only log in as a guest user. If `false`, the user can sign in with a Managed Apple Account (the existing behavior). Available: iOS 14.5+ | iPadOS 14.5+
- `TemporarySessionTimeout` (integer): The timeout, in seconds, for the temporary session. The temporary session logs out automatically after the specified period of inactivity. The minimum value is 30 seconds. Setting this value to `0` removes the timeout. Available: iOS 14.5+ | iPadOS 14.5+ | visionOS 26+
- `UserSessionTimeout` (integer): The timeout, in seconds, for the user session. The user session logs out automatically after the specified period of inactivity. The minimum value is 30 seconds. Setting this value to `0` removes the timeout. Available: iOS 14.5+ | iPadOS 14.5+

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

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/settingscommand/command-data.dictionary/settings-data.dictionary/shareddeviceconfiguration-data.dictionary)*
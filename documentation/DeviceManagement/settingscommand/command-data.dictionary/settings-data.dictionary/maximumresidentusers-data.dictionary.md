# SettingsCommand.Command.Settings.MaximumResidentUsers

**Framework**: Device Management  
**Kind**: dictionary  
**Role**: Device Management Command

A dictionary that contains settings for maximum resident users.

**Availability**:
- iOS 9.3+ - Deprecated in 13.4
- iPadOS 9.3+ - Deprecated in 13.4
- Mac Catalyst 9.3+ - Deprecated in 13.4

## Declaration

```
object SettingsCommand.Command.Settings.MaximumResidentUsers
```

## Properties

- `Item` (string) *(required)* *(deprecated)*: A string that identifies this setting.

  Deprecated: iOS 13.4+ | iPadOS 13.4+

  **Allowed Values**: `MaximumResidentUsers`
- `MaximumResidentUsers` (integer) *(required)* *(deprecated)*: The maximum number of users that can use the device. If this value is greater than the value for the maximum possible number of users that the device supports, the MDM server uses that value instead.

  This setting requires that the device is in the `AwaitingConfiguration` phase before it receives the [`DeviceConfiguredCommand`](../../../deviceconfiguredcommand.md) message.

  When a device reaches the maximum number of resident users and a new user tries to sign in, the MDM server removes a synchronized user to make space for the new user. If there are no synchronized users, the new user sign-in fails. A synchronized user is a user that has completed syncing their data.

  Deprecated: iOS 13.4+ | iPadOS 13.4+

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
- [object SettingsCommand.Command.Settings.OrganizationInfo](./organizationinfo-data.dictionary.md)
  A dictionary that contains settings about the organization operating the MDM server.
- [object SettingsCommand.Command.Settings.PasscodeLockGracePeriod](./passcodelockgraceperiod-data.dictionary.md)
  A dictionary that contains settings for the password lock grace period.
- [object SettingsCommand.Command.Settings.PersonalHotspot](./personalhotspot-data.dictionary.md)
  A dictionary that contains Personal Hotspot settings.
- [object SettingsCommand.Command.Settings.SharedDeviceConfiguration](./shareddeviceconfiguration-data.dictionary.md)
  A dictionary that contains shared device configuration settings.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/settingscommand/command-data.dictionary/settings-data.dictionary/maximumresidentusers-data.dictionary)*
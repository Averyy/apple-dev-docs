# SettingsCommand.Command.Settings.ApplicationAttributes

**Framework**: Device Management  
**Kind**: dictionary  
**Role**: Device Management Command

A dictionary that contains the attributes to apply to the app.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 7.0+
- tvOS 10.2+
- visionOS 1.1+
- watchOS 10.0+

## Declaration

```
object SettingsCommand.Command.Settings.ApplicationAttributes
```

## Topics

### Objects
- [object SettingsCommand.Command.Settings.ApplicationAttributes.Attributes](./applicationattributes-data.dictionary/attributes-data.dictionary.md)
  A dictionary that contains the attributes to apply to the app.

## Properties

- `Attributes` (SettingsCommand.Command.Settings.ApplicationAttributes.Attributes): A dictionary that contains the attributes to apply to the app. Omit this setting to remove existing attributes.
- `Identifier` (string) *(required)*: The bundle identifier of the app.

  > ❗ **Important**:  For a watchOS app, the identifier needs to be the watch’s bundle identifier, which differs from the main bundle identifier for the iPhone the watch pairs with. Obtain the watch’s bundle identifier for an app with a watch bundle, in the `watchBundleId` key that’s part of the Content Metadata query. For more information on this query, see [Getting app and book information (Legacy)](../../../getting-app-and-book-information-legacy.md).
- `Item` (string) *(required)*: A string that identifies this setting.

  **Allowed Values**: `ApplicationAttributes`

## See Also

### Objects
- [object SettingsCommand.Command.Settings.AccessibilitySettings](./accessibilitysettings-data.dictionary.md)
  A dictionary that contains settings for accessibility.
- [object SettingsCommand.Command.Settings.AppAnalytics](./appanalytics-data.dictionary.md)
  A dictionary that contains settings for sharing app analytics.
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
- [object SettingsCommand.Command.Settings.SharedDeviceConfiguration](./shareddeviceconfiguration-data.dictionary.md)
  A dictionary that contains shared device configuration settings.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/settingscommand/command-data.dictionary/settings-data.dictionary/applicationattributes-data.dictionary)*
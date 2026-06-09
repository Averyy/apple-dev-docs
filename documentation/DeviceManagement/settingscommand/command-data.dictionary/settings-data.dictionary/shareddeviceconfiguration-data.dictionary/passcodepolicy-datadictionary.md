# SettingsCommand.Command.Settings.SharedDeviceConfiguration.PasscodePolicy

**Framework**: Device Management  
**Kind**: dictionary

A dictionary that contains passcode policies.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+

## Declaration

```swift
object SettingsCommand.Command.Settings.SharedDeviceConfiguration.PasscodePolicy
```

## Properties

- `AutoLockTime` (integer): The number of seconds before a device goes to sleep after being idle. The minimum value for this setting is `120` seconds.
- `PasscodeLockGracePeriod` (integer): The number of seconds before a locked screen requires the user to enter the device passcode to unlock it. The minimum value is `0` seconds and the maximum value is `14400` seconds. If a device has a passcode, a change to a larger value doesn’t take effect until the user logs out or removes the passcode. For this reason, it’s better to set this value before the user sets a passcode. If the value is less than one of the known values, the device uses the next lowest value. For example a value of 299 results in an effective setting of 60. This setting won’t take effect if `TemporarySessionOnly` is `true` because there’s no passcode for a temporary session.

## See Also

- [object SettingsCommand.Command.Settings.SharedDeviceConfiguration.AwaitUserConfiguration](settingscommand/command-data.dictionary/settings-data.dictionary/shareddeviceconfiguration-data.dictionary/awaituserconfiguration-data.dictionary.md)
  Enables the user configuration Setup Assistant workflow.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/settingscommand/command-data.dictionary/settings-data.dictionary/shareddeviceconfiguration-data.dictionary/passcodepolicy-data.dictionary)*
# SettingsCommand.Command.Settings.SharedDeviceConfiguration.AwaitUserConfiguration

**Framework**: Device Management  
**Kind**: dictionary

Enables the user configuration Setup Assistant workflow.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+

## Declaration

```swift
object SettingsCommand.Command.Settings.SharedDeviceConfiguration.AwaitUserConfiguration
```

## Properties

- `Enabled` (boolean) *(required)*: If `true`, the device stops at the Setup Assistant pane after user login. The user can’t use the device until it receives a [`User Configured`](user-configured-command.md) command.

## See Also

- [object SettingsCommand.Command.Settings.SharedDeviceConfiguration.PasscodePolicy](settingscommand/command-data.dictionary/settings-data.dictionary/shareddeviceconfiguration-data.dictionary/passcodepolicy-data.dictionary.md)
  A dictionary that contains passcode policies.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/settingscommand/command-data.dictionary/settings-data.dictionary/shareddeviceconfiguration-data.dictionary/awaituserconfiguration-data.dictionary)*
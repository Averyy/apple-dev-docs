# SettingsCommand.Command.Settings.SharedDeviceConfiguration.AwaitUserConfiguration

**Framework**: Device Management  
**Kind**: dictionary  
**Role**: Device Management Command

Enables the user configuration Setup Assistant workflow.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+

## Declaration

```
object SettingsCommand.Command.Settings.SharedDeviceConfiguration.AwaitUserConfiguration
```

## Properties

- `Enabled` (boolean) *(required)*: If `true`, the device stops at the Setup Assistant pane after user login. The user can’t use the device until it receives a [`User Configured`](../../../../user-configured-command.md) command.

## See Also

### Objects
- [object SettingsCommand.Command.Settings.SharedDeviceConfiguration.PasscodePolicy](./passcodepolicy-data.dictionary.md)
  A dictionary that contains passcode policies.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/settingscommand/command-data.dictionary/settings-data.dictionary/shareddeviceconfiguration-data.dictionary/awaituserconfiguration-data.dictionary)*
# SettingsCommand.Command.Settings.MDMOptions.MDMOptions

**Framework**: Device Management  
**Kind**: dictionary

A dictionary that contains MDM options.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 7.0+
- macOS 10.15+
- visionOS 2.0+

## Declaration

```swift
object SettingsCommand.Command.Settings.MDMOptions.MDMOptions
```

## Properties

- `ActivationLockAllowedWhileSupervised` (boolean): If `true`, a supervised device registers itself with Activation Lock when the user enables Find My. This setting is available for supervised devices in iOS 7 and later, and macOS 10.15 and later.
- `BootstrapTokenAllowed` (boolean): If `true`, the server supports the Bootstrap Token commands. Available: macOS 10.15+
Deprecated: macOS 11+
- `IdleRebootAllowed` (boolean): If `true`, the device automatically reboots while locked after several days of inactivity. The device sets this to `false` by default for a supervised enrollment. Starting in iOS 26.6 and iPadOS 26.6, changing the effective value from reboot allowed to reboot disallowed requires a reboot or a device unlock before the change takes effect. Available: iOS 18.4+ | iPadOS 18.4+
- `PromptUserToAllowBootstrapTokenForAuthentication` (boolean): If `true`, warn the user that they need to reboot into RecoveryOS and allow the MDM server to use the Bootstrap Token for authentication for certain sensitive operations; for example, enabling kernel extensions or installing certain types of software updates. Set this value to `false` if your MDM server doesn’t need to perform these operations. The value provided here overrides the value specified in MDM, and only applies when `BootstrapTokenAllowedForAuthentication` is `true` in the [`SecurityInfoResponse.SecurityInfo`](securityinforesponse/securityinfo-data.dictionary.md) response. This value is available for a Mac with Apple silicon in macOS 11 and later. Available: macOS 11+


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/settingscommand/command-data.dictionary/settings-data.dictionary/mdmoptions-data.dictionary/mdmoptions-data.dictionary)*
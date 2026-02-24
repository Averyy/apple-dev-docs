# ClearActivationLockBypassCodeCommand.Command

**Framework**: Device Management  
**Kind**: dictionary

The command to clear the Activation Lock bypass code on a device.

**Availability**:
- iOS 7.1+
- iPadOS 7.1+
- macOS 10.15+
- visionOS 2.0+

## Declaration

```swift
object ClearActivationLockBypassCodeCommand.Command
```

## Properties

- `RequestRequiresNetworkTether` (boolean): If `true`, the device needs to be network-tethered to run the command.
- `RequestType` (string) *(required)*: The request type for this command.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/clearactivationlockbypasscodecommand/command-data.dictionary)*
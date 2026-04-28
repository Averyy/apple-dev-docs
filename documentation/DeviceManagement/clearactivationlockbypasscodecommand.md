# ClearActivationLockBypassCodeCommand

**Framework**: Device Management  
**Kind**: dictionary

The command to clear the Activation Lock bypass code on a device.

**Availability**:
- iOS 7.1+
- iPadOS 7.1+
- Mac Catalyst 7.1+
- macOS 10.15+
- visionOS 2.0+
- Device Assignment Services ?+
- VPP License Management ?+

## Declaration

```swift
object ClearActivationLockBypassCodeCommand
```

## Mentions

- [Handling NotNow Status Responses](handling-notnow-status-responses.md)

## Topics

### Objects
- [object ClearActivationLockBypassCodeCommand.Command](clearactivationlockbypasscodecommand/command-data.dictionary.md)
  The command to clear the Activation Lock bypass code on a device.

## Properties

- `Command` (ClearActivationLockBypassCodeCommand.Command) *(required)*: The command dictionary.
- `CommandUUID` (string) *(required)*: The unique identifier of the command.

## See Also

- [object ClearActivationLockBypassCodeResponse](clearactivationlockbypasscoderesponse.md)
  A response from the device after it processes the command to clear the Activation Lock bypass code on a device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/clearactivationlockbypasscodecommand)*
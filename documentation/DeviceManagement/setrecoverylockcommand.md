# SetRecoveryLockCommand

**Framework**: Device Management  
**Kind**: dictionary

The command to set or clear the Recovery Lock password.

**Availability**:
- macOS 11.5+
- Device Assignment Services ?+
- VPP License Management ?+

## Declaration

```swift
object SetRecoveryLockCommand
```

## Topics

### Objects
- [object SetRecoveryLockCommand.Command](setrecoverylockcommand/command-data.dictionary.md)
  The command to set or clear the Recovery Lock password.

## Properties

- `Command` (SetRecoveryLockCommand.Command) *(required)*: The command dictionary.
- `CommandUUID` (string) *(required)*: The unique identifier of the command.

## See Also

- [object SetRecoveryLockResponse](setrecoverylockresponse.md)
  A response from the device after it processes the command to set or clear the Recovery Lock password.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/setrecoverylockcommand)*
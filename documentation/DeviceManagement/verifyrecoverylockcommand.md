# VerifyRecoveryLockCommand

**Framework**: Device Management  
**Kind**: dictionary  
**Role**: Device Management Command

The command to verify the device’s Recovery Lock password.

**Availability**:
- macOS 11.5+

## Declaration

```
object VerifyRecoveryLockCommand
```

## Topics

### Objects
- [object VerifyRecoveryLockCommand.Command](./verifyrecoverylockcommand/command-data.dictionary.md)
  The command to verify the device’s Recovery Lock password.

## Properties

- `Command` (VerifyRecoveryLockCommand.Command) *(required)*: The command dictionary.
- `CommandUUID` (string) *(required)*: The unique identifier of the command.

## See Also

### Commands and responses
- [object VerifyRecoveryLockResponse](./verifyrecoverylockresponse.md)
  A response from the device after it processes the command to verify the device’s Recovery Lock password.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/verifyrecoverylockcommand)*
# SetRecoveryLockCommand

**Framework**: Device Management  
**Kind**: dictionary  
**Role**: Device Management Command

The command to set or clear the Recovery Lock password.

**Availability**:
- macOS 11.5+

## Declaration

```
object SetRecoveryLockCommand
```

## Topics

### Objects
- [object SetRecoveryLockCommand.Command](./setrecoverylockcommand/command-data.dictionary.md)
  The command to set or clear the Recovery Lock password.

## Properties

- `Command` (SetRecoveryLockCommand.Command) *(required)*: The command dictionary.
- `CommandUUID` (string) *(required)*: The unique identifier of the command.

## See Also

### Commands and responses
- [object SetRecoveryLockResponse](./setrecoverylockresponse.md)
  A response from the device after it processes the command to set or clear the Recovery Lock password.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/setrecoverylockcommand)*
# SetAutoAdminPasswordCommand

**Framework**: Device Management  
**Kind**: dictionary  
**Role**: Device Management Command

The command to update the local administrator account password.

**Availability**:
- macOS 10.11+

## Declaration

```
object SetAutoAdminPasswordCommand
```

## Topics

### Objects
- [object SetAutoAdminPasswordCommand.Command](./setautoadminpasswordcommand/command-data.dictionary.md)
  The command to update the local administrator account password.

## Properties

- `Command` (SetAutoAdminPasswordCommand.Command) *(required)*: The command dictionary.
- `CommandUUID` (string) *(required)*: The unique identifier of the command.

## See Also

### Commands and responses
- [object SetAutoAdminPasswordResponse](./setautoadminpasswordresponse.md)
  A response from the device after it processes the command to update the local administrator account password.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/setautoadminpasswordcommand)*
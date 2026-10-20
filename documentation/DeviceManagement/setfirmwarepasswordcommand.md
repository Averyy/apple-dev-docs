# SetFirmwarePasswordCommand

**Framework**: Device Management  
**Kind**: dictionary  
**Role**: Device Management Command

The command to change or clear the firmware password on a device.

**Availability**:
- macOS 10.13+

## Declaration

```
object SetFirmwarePasswordCommand
```

## Topics

### Objects
- [object SetFirmwarePasswordCommand.Command](./setfirmwarepasswordcommand/command-data.dictionary.md)
  The command to change or clear the firmware password on a device.

## Properties

- `Command` (SetFirmwarePasswordCommand.Command) *(required)*: The command dictionary.
- `CommandUUID` (string) *(required)*: The unique identifier of the command.

## See Also

### Commands and responses
- [object SetFirmwarePasswordResponse](./setfirmwarepasswordresponse.md)
  A response from the device after it processes the command to change or clear the firmware password on a device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/setfirmwarepasswordcommand)*
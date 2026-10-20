# VerifyFirmwarePasswordCommand

**Framework**: Device Management  
**Kind**: dictionary  
**Role**: Device Management Command

The command to verify the firmware password on a device.

**Availability**:
- macOS 10.13+

## Declaration

```
object VerifyFirmwarePasswordCommand
```

## Topics

### Objects
- [object VerifyFirmwarePasswordCommand.Command](./verifyfirmwarepasswordcommand/command-data.dictionary.md)
  The command to verify the firmware password on a device.

## Properties

- `Command` (VerifyFirmwarePasswordCommand.Command) *(required)*: The command dictionary.
- `CommandUUID` (string) *(required)*: The unique identifier of the command.

## See Also

### Commands and responses
- [object VerifyFirmwarePasswordResponse](./verifyfirmwarepasswordresponse.md)
  A response from the device after it processes the command to verify the firmware password on a device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/verifyfirmwarepasswordcommand)*
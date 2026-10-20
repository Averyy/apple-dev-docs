# LOMDeviceRequestCommand

**Framework**: Device Management  
**Kind**: dictionary  
**Role**: Device Management Command

The command to send requests to a device using lights-out management (LOM).

**Availability**:
- macOS 11.0+

## Declaration

```
object LOMDeviceRequestCommand
```

## Topics

### Objects
- [object LOMDeviceRequestCommand.Command](./lomdevicerequestcommand/command-data.dictionary.md)
  The command to send requests to a device using lights-out management (LOM).

## Properties

- `Command` (LOMDeviceRequestCommand.Command) *(required)*: The command dictionary.
- `CommandUUID` (string) *(required)*: The unique identifier of the command.

## See Also

### Commands and responses
- [object LOMDeviceRequestResponse](./lomdevicerequestresponse.md)
  A response from the device after it processes the command to send requests to a device using lights-out management (LOM).


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/lomdevicerequestcommand)*
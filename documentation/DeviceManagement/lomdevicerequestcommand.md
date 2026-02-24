# LOMDeviceRequestCommand

**Framework**: Device Management  
**Kind**: dictionary

The command to send requests to a device using lights-out management (LOM).

**Availability**:
- macOS 11.0+

## Declaration

```swift
object LOMDeviceRequestCommand
```

## Topics

### Objects
- [object LOMDeviceRequestCommand.Command](lomdevicerequestcommand/command-data.dictionary.md)
  The command to send requests to a device using lights-out management (LOM).

## Properties

- `Command` (LOMDeviceRequestCommand.Command) *(required)*: The command dictionary.
- `CommandUUID` (string) *(required)*: The unique identifier of the command.

## See Also

- [object LOMDeviceRequestResponse](lomdevicerequestresponse.md)
  A response from the device after it processes the command to send requests to a device using lights-out management (LOM).


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/lomdevicerequestcommand)*
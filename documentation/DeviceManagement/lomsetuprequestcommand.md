# LOMSetupRequestCommand

**Framework**: Device Management  
**Kind**: dictionary

The command to get information from a device to set up lights-out management (LOM).

**Availability**:
- macOS 11.0+

## Declaration

```swift
object LOMSetupRequestCommand
```

## Topics

### Objects
- [object LOMSetupRequestCommand.Command](lomsetuprequestcommand/command-data.dictionary.md)
  The command to get information from a device to set up lights-out management (LOM).

## Properties

- `Command` (LOMSetupRequestCommand.Command) *(required)*: The command dictionary.
- `CommandUUID` (string) *(required)*: The unique identifier of the command.

## See Also

- [object LOMSetupRequestResponse](lomsetuprequestresponse.md)
  A response from the device after it processes the command to get information from a device to set up lights-out management (LOM).


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/lomsetuprequestcommand)*
# LOMDeviceRequestCommand.Command

**Framework**: Device Management  
**Kind**: dictionary

The command to send requests to a device using lights-out management (LOM).

**Availability**:
- macOS 11.0+

## Declaration

```swift
object LOMDeviceRequestCommand.Command
```

## Topics

### Objects
- [object LOMDeviceRequestCommand.Command.RequestListItem](lomdevicerequestcommand/command-data.dictionary/requestlistitem.md)
  A dictionary that contains a requested action to perform on a device using lights-out management (LOM).

## Properties

- `RequestList` ([LOMDeviceRequestCommand.Command.RequestListItem]) *(required)*: An array of requests to perform.
- `RequestRequiresNetworkTether` (boolean): If `true`, the device needs to be network-tethered to run the command.
- `RequestType` (string) *(required)*: The request type for this command.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/lomdevicerequestcommand/command-data.dictionary)*
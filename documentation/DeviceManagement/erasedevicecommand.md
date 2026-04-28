# EraseDeviceCommand

**Framework**: Device Management  
**Kind**: dictionary

The command to remotely and immediately erase a device.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 4.0+
- macOS 10.7+
- tvOS 10.2+
- visionOS 1.1+
- watchOS 10.0+
- Device Assignment Services ?+
- VPP License Management ?+

## Declaration

```swift
object EraseDeviceCommand
```

## Mentions

- [Handling NotNow Status Responses](handling-notnow-status-responses.md)

## Topics

### Objects
- [object EraseDeviceCommand.Command](erasedevicecommand/command-data.dictionary.md)
  The command to remotely and immediately erase a device.

## Properties

- `Command` (EraseDeviceCommand.Command) *(required)*: The command dictionary.
- `CommandUUID` (string) *(required)*: The unique identifier of the command.

## See Also

- [object EraseDeviceResponse](erasedeviceresponse.md)
  A response from the device after it processes the command to remotely and immediately erase a device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/erasedevicecommand)*
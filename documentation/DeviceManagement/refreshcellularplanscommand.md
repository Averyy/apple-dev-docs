# RefreshCellularPlansCommand

**Framework**: Device Management  
**Kind**: dictionary

The command to query a carrier URL for active eSIM cellular-plan profiles on a device.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- Device Assignment Services ?+
- VPP License Management ?+

## Declaration

```swift
object RefreshCellularPlansCommand
```

## Topics

### Objects
- [object RefreshCellularPlansCommand.Command](refreshcellularplanscommand/command-data.dictionary.md)
  The command to query a carrier URL for active eSIM cellular-plan profiles on a device.

## Properties

- `Command` (RefreshCellularPlansCommand.Command) *(required)*: The command dictionary.
- `CommandUUID` (string) *(required)*: The unique identifier of the command.

## See Also

- [object RefreshCellularPlansResponse](refreshcellularplansresponse.md)
  A response from the device after it processes the command to query a carrier URL for active eSIM cellular-plan profiles on a device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/refreshcellularplanscommand)*
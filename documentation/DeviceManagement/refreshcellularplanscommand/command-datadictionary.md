# RefreshCellularPlansCommand.Command

**Framework**: Device Management  
**Kind**: dictionary

The command to query a carrier URL for active eSIM cellular-plan profiles on a device.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+

## Declaration

```swift
object RefreshCellularPlansCommand.Command
```

## Properties

- `eSIMServerURL` (string) *(required)*: The carrier’s eSIM server URL to query. Obtain this URL from each carrier separately.
- `RequestRequiresNetworkTether` (boolean): If `true`, the device needs to be network-tethered to run the command.
- `RequestType` (string) *(required)*: The request type for this command.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/refreshcellularplanscommand/command-data.dictionary)*
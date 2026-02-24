# OSUpdateStatusCommand.Command

**Framework**: Device Management  
**Kind**: dictionary

The command to get the status of operating-system updates on a device.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- macOS 10.11.5+
- tvOS 12.0+

## Declaration

```swift
object OSUpdateStatusCommand.Command
```

## Properties

- `RequestRequiresNetworkTether` (boolean): If `true`, the device needs to be network-tethered to run the command.
- `RequestType` (string) *(required)*: The request type for this command.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/osupdatestatuscommand/command-data.dictionary)*
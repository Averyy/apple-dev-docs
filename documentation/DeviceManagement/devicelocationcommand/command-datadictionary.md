# DeviceLocationCommand.Command

**Framework**: Device Management  
**Kind**: dictionary

The command to request the location of a device when in Lost Mode.

**Availability**:
- iOS 9.3+
- iPadOS 9.3+
- Mac Catalyst 9.3+

## Declaration

```swift
object DeviceLocationCommand.Command
```

## Properties

- `RequestRequiresNetworkTether` (boolean): If `true`, the device needs to be network-tethered to run the command.
- `RequestType` (string) *(required)*: The request type for this command.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/devicelocationcommand/command-data.dictionary)*
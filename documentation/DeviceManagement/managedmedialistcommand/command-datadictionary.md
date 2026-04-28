# ManagedMediaListCommand.Command

**Framework**: Device Management  
**Kind**: dictionary

The command to get a list of the managed books on a device.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 8.0+
- Device Assignment Services ?+
- VPP License Management ?+

## Declaration

```swift
object ManagedMediaListCommand.Command
```

## Properties

- `RequestRequiresNetworkTether` (boolean): If `true`, the device needs to be network-tethered to run the command.
- `RequestType` (string) *(required)*: The request type for this command.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/managedmedialistcommand/command-data.dictionary)*
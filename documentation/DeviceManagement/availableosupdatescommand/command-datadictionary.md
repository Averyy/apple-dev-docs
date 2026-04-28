# AvailableOSUpdatesCommand.Command

**Framework**: Device Management  
**Kind**: dictionary

The command to get a list of available operating-system updates for a device.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 9.0+
- macOS 10.11+
- tvOS 12.0+
- Device Assignment Services ?+
- VPP License Management ?+

## Declaration

```swift
object AvailableOSUpdatesCommand.Command
```

## Properties

- `RequestRequiresNetworkTether` (boolean): If `true`, the device needs to be network-tethered to run the command.
- `RequestType` (string) *(required)*: The request type for this command.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/availableosupdatescommand/command-data.dictionary)*
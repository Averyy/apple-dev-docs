# DeviceConfiguredCommand.Command

**Framework**: Device Management  
**Kind**: dictionary

The command to inform the device that it can allow the user to continue in Setup Assistant.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 9.0+
- macOS 10.11+
- tvOS 10.2+
- visionOS 2.0+
- Device Assignment Services ?+
- VPP License Management ?+

## Declaration

```swift
object DeviceConfiguredCommand.Command
```

## Properties

- `RequestRequiresNetworkTether` (boolean): If `true`, the device needs to be network-tethered to run the command.
- `RequestType` (string) *(required)*: The request type for this command.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/deviceconfiguredcommand/command-data.dictionary)*
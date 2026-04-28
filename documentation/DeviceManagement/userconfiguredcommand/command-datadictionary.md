# UserConfiguredCommand.Command

**Framework**: Device Management  
**Kind**: dictionary

The command to inform the device that it can continue past Setup Assistant and finish login.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- Device Assignment Services ?+
- VPP License Management ?+

## Declaration

```swift
object UserConfiguredCommand.Command
```

## Properties

- `RequestRequiresNetworkTether` (boolean): If `true`, the device needs to be network-tethered to run the command.
- `RequestType` (string) *(required)*: The request type for this command.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/userconfiguredcommand/command-data.dictionary)*
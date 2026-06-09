# DeviceLockCommand.Command

**Framework**: Device Management  
**Kind**: dictionary

The command to remotely and immediately lock a device.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 4.0+
- macOS 10.7+
- visionOS 2.0+
- watchOS 10.0+

## Declaration

```swift
object DeviceLockCommand.Command
```

## Properties

- `Message` (string): The message to display on the Lock Screen of the device. This value doesn’t apply to a Shared iPad device. Available: iOS 7+ | iPadOS 7+ | macOS 10.14+ | watchOS 10+
- `PhoneNumber` (string): The phone number to display on the Lock Screen. This value doesn’t apply to a Shared iPad device. This value is available for a Mac with Apple silicon only. Available: iOS 7+ | iPadOS 7+ | macOS 11.5+ | watchOS 10+
- `PIN` (string): The six-character PIN for Find My. Available: macOS 10.8+
- `RequestRequiresNetworkTether` (boolean): If `true`, the device needs to be network-tethered to run the command.
- `RequestType` (string) *(required)*: The request type for this command.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/devicelockcommand/command-data.dictionary)*
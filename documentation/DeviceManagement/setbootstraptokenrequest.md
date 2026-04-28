# SetBootstrapTokenRequest

**Framework**: Device Management  
**Kind**: dictionary

The set bootstrap token request details.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 10.15+
- visionOS 26.0+
- Device Assignment Services ?+
- VPP License Management ?+

## Declaration

```swift
object SetBootstrapTokenRequest
```

## Properties

- `AwaitingConfiguration` (boolean): If `true`, the device is awaiting a [`Device Configured`](device-configured-command.md) command before proceeding through Setup Assistant.
- `BootstrapToken` (data): The device’s bootstrap token data. If this field is missing or zero length, the server needs to remove the bootstrap token for this device.
- `MessageType` (string) *(required)*: The message type, which requires a value of `SetBootstrapToken`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/setbootstraptokenrequest)*
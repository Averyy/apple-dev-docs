# TokenUpdateRequest

**Framework**: Device Management  
**Kind**: dictionary

The token update request details.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 4.0+
- macOS 10.7+
- tvOS 10.2+
- visionOS 1.1+
- watchOS 10.0+

## Declaration

```swift
object TokenUpdateRequest
```

## Mentions

- [Managing passcodes](managing-passcodes.md)

## Properties

- `AwaitingConfiguration` (boolean): If `true` from the device channel, the device is awaiting a [`Device Configured`](device-configured-command.md) command before proceeding through Setup Assistant. If `true` from the user channel (Shared iPad only), the device is awaiting a [`User Configured`](user-configured-command.md) command before proceeding through Setup Assistant. Available: iOS 9+ | iPadOS 9+ | macOS 10.11+ | tvOS 10.2+ | visionOS 1.1+
- `EnrollmentID` (string) *(required)*: The per-enrollment identifier for the device. The system requires this value if the enrollment type is a user enrollment. Available: iOS 13+ | iPadOS 13+ | macOS 10.15+ | visionOS 1.1+
- `EnrollmentUserID` (string) *(required)*: The per-enrollment identifier for the user. The system requires this value if the enrollment type is a user enrollment on the user channel. Available: macOS 10.15+
- `MessageType` (string) *(required)*: The message type, which requires a value of `TokenUpdate`.
- `NotOnConsole` (boolean) *(required)*: If `true`, the device isn’t on-console. Available: macOS 10.11+ | tvOS 10.2+
- `PushMagic` (string) *(required)*: The magic string to include in the push notification message.
- `Token` (data) *(required)*: The push token for the device.
- `Topic` (string) *(required)*: The topic the device subscribes to.
- `UDID` (string) *(required)*: The device’s UDID (unique device identifier). The system requires this value if the enrollment type is a device enrollment.
- `UnlockToken` (data): The data to use to unlock the device. If provided, the server needs to retain this data and send it when trying to implement [`Clear Passcode`](clear-passcode-command.md). Available: iOS 4+ | iPadOS 4+ | tvOS 10.2+ | visionOS 1.1+ | watchOS 10+
- `UserID` (string): For macOS, this value is the ID of the user. For Shared iPad, this value is `FFFFFFFF-FFFF-FFFF-FFFF-FFFFFFFFFFFF` to indicate that authentication doesn’t occur. Available: iOS 9.3+ | iPadOS 9.3+ | macOS 10.7+
- `UserLongName` (string) *(required)*: The full name of the user. Available: macOS 10.7+
- `UserShortName` (string): For macOS, this value is the short name of the user. For Shared iPad, this value is the Managed Apple Account identifier of the user on Shared iPad. It indicates that the token is for the user channel. Available: iOS 9.3+ | iPadOS 9.3+ | macOS 10.7+


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/tokenupdaterequest)*
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
- Device Assignment Services ?+
- VPP License Management ?+

## Declaration

```swift
object TokenUpdateRequest
```

## Mentions

- [Managing Passcodes](managing-passcodes.md)

## Properties

- `AwaitingConfiguration` (boolean): If `true` from the device channel, the device is awaiting a [`Device Configured`](device-configured-command.md) command before proceeding through Setup Assistant. If `true` from the user channel (Shared iPad only), the device is awaiting a [`User Configured`](user-configured-command.md) command before proceeding through Setup Assistant.
- `EnrollmentID` (string) *(required)*: The per-enrollment identifier for the device. The system requires this value if the enrollment type is a user enrollment. Available in iOS 13 and later, macOS 10.15 and later, and visionOS 2 and later.
- `EnrollmentUserID` (string) *(required)*: The per-enrollment identifier for the user. The system requires this value if the enrollment type is a user enrollment on the user channel. Available in macOS 10.15 and later.
- `MessageType` (string) *(required)*: The message type, which requires a value of `TokenUpdate`.
- `NotOnConsole` (boolean) *(required)*: If `true`, the device isn’t on-console.
- `PushMagic` (string) *(required)*: The magic string to include in the push notification message.
- `Token` (data) *(required)*: The push token for the device.
- `Topic` (string) *(required)*: The topic the device subscribes to.
- `UDID` (string) *(required)*: The device’s UDID (unique device identifier). The system requires this value if the enrollment type is a device enrollment.
- `UnlockToken` (data): The data to use to unlock the device. If provided, the server needs to retain this data and send it when trying to implement [`Clear Passcode`](clear-passcode-command.md).
- `UserID` (string): For macOS, this value is the ID of the user. For Shared iPad, this value is `FFFFFFFF-FFFF-FFFF-FFFF-FFFFFFFFFFFF` to indicate that authentication doesn’t occur.
- `UserLongName` (string) *(required)*: The full name of the user.
- `UserShortName` (string): For macOS, this value is the short name of the user. For Shared iPad, this value is the Managed Apple Account identifier of the user on Shared iPad. It indicates that the token is for the user channel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/tokenupdaterequest)*
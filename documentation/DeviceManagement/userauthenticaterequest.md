# UserAuthenticateRequest

**Framework**: Device Management  
**Kind**: dictionary

The user authenticate request details.

**Availability**:
- macOS 10.7+

## Declaration

```swift
object UserAuthenticateRequest
```

## Properties

- `DigestResponse` (string) *(required)*: A string that the client provides in the second [`User Authenticate`](user-authenticate.md) request after receiving `DigestChallenge` from the server on the first [`User Authenticate`](user-authenticate.md) request.
- `MessageType` (string) *(required)*: The message type, which requires a value of `UserAuthenticate`.
- `UDID` (string) *(required)*: The device’s UDID (unique device identifier). The system requires this value if the enrollment type is a device enrollment.
- `UserID` (string) *(required)*: The local mobile user’s GUID or the network user’s GUID from an Open Directory record.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/userauthenticaterequest)*
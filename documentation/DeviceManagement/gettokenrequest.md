# GetTokenRequest

**Framework**: Device Management  
**Kind**: dictionary

The get token request details.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- macOS 14.0+
- visionOS 1.1+

## Declaration

```swift
object GetTokenRequest
```

## Topics

### Objects
- [object GetTokenRequest.TokenParameters](gettokenrequest/tokenparameters-data.dictionary.md)
  Parameters that the system uses to generate the token.

## Properties

- `EnrollmentID` (string) *(required)*: The per-enrollment identifier for the device. The system requires this value if the enrollment type is a user enrollment.
- `EnrollmentUserID` (string) *(required)*: The per-enrollment identifier for the user. The system requires this value if the enrollment type is a user enrollment on the user channel.
- `MessageType` (string) *(required)*: The message type, which requires a value of `GetToken`.
- `TokenParameters` (GetTokenRequest.TokenParameters): Parameters that the system uses to generate the token.
- `TokenServiceType` (string) *(required)*: A string that specifies the service for the requested token.
- `UDID` (string) *(required)*: The device’s UDID (unique device identifier). The system requires this value if the enrollment type is a device enrollment.
- `UserID` (string): For macOS, this value is the ID of the user. For Shared iPad, this value is `FFFFFFFF-FFFF-FFFF-FFFF-FFFFFFFFFFFF` to indicate that authentication doesn’t occur.
- `UserLongName` (string) *(required)*: The full name of the user.
- `UserShortName` (string): For macOS, this value is the short name of the user. For Shared iPad, this value is the Managed Apple Account identifier of the user. When present, it indicates that the token is for the user channel.

## See Also

- [object GetTokenResponse](gettokenresponse.md)
  The get token response details.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/gettokenrequest)*
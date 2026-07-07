# InstallApplicationResponse

**Framework**: Device Management  
**Kind**: dictionary

A response from the device after it processes the command to install a third-party app on a device.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 5.0+
- macOS 10.9+
- tvOS 10.2+
- visionOS 1.1+
- watchOS 10.0+

## Declaration

```swift
object InstallApplicationResponse
```

## Topics

### Objects
- [object InstallApplicationResponse.ErrorChainItem](installapplicationresponse/errorchainitem.md)
  A dictionary that describes an error chain item.

## Properties

- `CommandUUID` (string): The unique identifier of the command for this response.
- `EnrollmentID` (string) *(required)*: The per-enrollment identifier for the device. The system requires this value if the enrollment type is a user enrollment. Available: iOS 13+ | iPadOS 13+ | macOS 10.15+ | visionOS 1.1+
- `EnrollmentUserID` (string) *(required)*: The per-enrollment identifier for the user. The system requires this value if the enrollment type is a user enrollment on the user channel. Available: macOS 10.15+
- `ErrorChain` ([InstallApplicationResponse.ErrorChainItem]): An array of dictionaries that describes any errors that occur.
- `Identifier` (string): The app’s bundle identifier, if the user accepted the request. > **Note**:  For a watchOS app, the identifier is the watch’s bundle identifier, which differs from the main bundle identifier for the iPhone the watch pairs with.
- `NotOnConsole` (boolean) *(required)*: If `true`, the device isn’t on-console.
- `RejectionReason` (string): The reason, if installation fails. macOS always returns “Other”.
- `State` (string): The app’s installation state, if the user accepted the request. If this value is `NeedsRedemption`, the server needs to send a redemption code to complete the app installation.
- `Status` (string) *(required)*: The status of the response, which is one of the following values: - `Acknowledged`: The device processed the command successfully.
- `Error`: An error occurred. See the `ErrorChain` for more details.
- `CommandFormatError`: A protocol error occurred, which can result from a malformed command.
- `Idle`: The device is idle; there’s no status.
- `NotNow`: The device received the command, but can’t run it.
- `UDID` (string) *(required)*: The device’s UDID (unique device identifier). The system requires this value if the enrollment type is a device enrollment.
- `UserID` (string): For macOS, this value is the ID of the user. For Shared iPad, this value is `FFFFFFFF-FFFF-FFFF-FFFF-FFFFFFFFFFFF` to indicate that authentication doesn’t occur. Available: iOS 9.3+ | iPadOS 9.3+ | macOS 10.9+
- `UserLongName` (string) *(required)*: The full name of the user. Available: macOS 10.9+
- `UserShortName` (string): For macOS, this value is the short name of the user. For Shared iPad, this value is the Managed Apple Account identifier of the user on Shared iPad. It indicates that the token is for the user channel. Available: iOS 9.3+ | iPadOS 9.3+ | macOS 10.9+

## See Also

- [object InstallApplicationCommand](installapplicationcommand.md)
  The command to install a third-party app on a device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/installapplicationresponse)*
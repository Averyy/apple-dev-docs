# ApplyRedemptionCodeResponse

**Framework**: Device Management  
**Kind**: dictionary

A response from the device after it processes the command to complete the installation of an app using a redemption code.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 5.0+
- Device Assignment Services ?+
- VPP License Management ?+

## Declaration

```swift
object ApplyRedemptionCodeResponse
```

## Topics

### Objects
- [object ApplyRedemptionCodeResponse.ErrorChainItem](applyredemptioncoderesponse/errorchainitem.md)
  A dictionary that describes an error chain item.

## Properties

- `CommandUUID` (string): The unique identifier of the command for this response.
- `EnrollmentID` (string) *(required)*: The per-enrollment identifier for the device. The system requires this value if the enrollment type is a user enrollment. Available in iOS 13 and later, macOS 10.15 and later, and visionOS 2 and later.
- `EnrollmentUserID` (string) *(required)*: The per-enrollment identifier for the user. The system requires this value if the enrollment type is a user enrollment on the user channel. Available in macOS 10.15 and later.
- `ErrorChain` ([ApplyRedemptionCodeResponse.ErrorChainItem]): An array of dictionaries that describes any errors that occur.
- `NotOnConsole` (boolean) *(required)*: If `true`, the device isn’t on-console.
- `Status` (string) *(required)*: The status of the response, which is one of the following values: - `Acknowledged`: The device processed the command successfully.
- `Error`: An error occurred. See the `ErrorChain` for more details.
- `CommandFormatError`: A protocol error occurred, which can result from a malformed command.
- `Idle`: The device is idle; there’s no status.
- `NotNow`: The device received the command, but can’t run it.
- `UDID` (string) *(required)*: The device’s UDID (unique device identifier). The system requires this value if the enrollment type is a device enrollment.
- `UserID` (string): For macOS, this value is the ID of the user. For Shared iPad, this value is `FFFFFFFF-FFFF-FFFF-FFFF-FFFFFFFFFFFF` to indicate that authentication doesn’t occur.
- `UserLongName` (string) *(required)*: The full name of the user.
- `UserShortName` (string): For macOS, this value is the short name of the user. For Shared iPad, this value is the Managed Apple Account identifier of the user on Shared iPad. It indicates that the token is for the user channel.

## See Also

- [object ApplyRedemptionCodeCommand](applyredemptioncodecommand.md)
  The command to complete the installation of an app using a redemption code.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/applyredemptioncoderesponse)*
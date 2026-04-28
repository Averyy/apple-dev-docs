# RestrictionsResponse

**Framework**: Device Management  
**Kind**: dictionary

A response from the device after it processes the command to get a list of restrictions on the device.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 4.0+
- tvOS 9.0+
- visionOS 1.1+
- watchOS 10.0+
- Device Assignment Services ?+
- VPP License Management ?+

## Declaration

```swift
object RestrictionsResponse
```

## Topics

### Objects
- [object RestrictionsResponse.ErrorChainItem](restrictionsresponse/errorchainitem.md)
  A dictionary that describes an error chain item.
- [object RestrictionsResponse.GlobalRestrictions](restrictionsresponse/globalrestrictions-data.dictionary.md)
  A dictionary that contains the global restrictions in effect.
- [object RestrictionsResponse.ProfileRestrictions](restrictionsresponse/profilerestrictions-data.dictionary.md)
  A dictionary that contains restrictions from each profile.

## Properties

- `CommandUUID` (string): The unique identifier of the command for this response.
- `EnrollmentID` (string) *(required)*: The per-enrollment identifier for the device. The system requires this value if the enrollment type is a user enrollment. Available in iOS 13 and later, macOS 10.15 and later, and visionOS 2 and later.
- `EnrollmentUserID` (string) *(required)*: The per-enrollment identifier for the user. The system requires this value if the enrollment type is a user enrollment on the user channel. Available in macOS 10.15 and later.
- `ErrorChain` ([RestrictionsResponse.ErrorChainItem]): An array of dictionaries that describes any errors that occur.
- `GlobalRestrictions` (RestrictionsResponse.GlobalRestrictions) *(required)*: A dictionary that contains the global restrictions in effect. This value is available in iOS 4 and later, and tvOS 6.1 and later.
- `NotOnConsole` (boolean) *(required)*: If `true`, the device isn’t on-console.
- `ProfileRestrictions` (RestrictionsResponse.ProfileRestrictions) *(required)*: A dictionary that contains dictionaries of restrictions from each profile. This value is only available when `ProfileRestrictions` is `true` in the command. The keys are the identifiers of the profiles. This value is available in iOS 4 and later, and tvOS 6.1 and later.
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

- [object RestrictionsCommand](restrictionscommand.md)
  The command to get a list of restrictions on the device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/restrictionsresponse)*
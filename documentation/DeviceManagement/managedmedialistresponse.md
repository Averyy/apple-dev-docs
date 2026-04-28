# ManagedMediaListResponse

**Framework**: Device Management  
**Kind**: dictionary

A response from the device after it processes the command to get a list of the managed books on a device.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 8.0+
- Device Assignment Services ?+
- VPP License Management ?+

## Declaration

```swift
object ManagedMediaListResponse
```

## Topics

### Objects
- [object ManagedMediaListResponse.BooksItem](managedmedialistresponse/booksitem.md)
  A dictionary that describes a managed book.
- [object ManagedMediaListResponse.ErrorChainItem](managedmedialistresponse/errorchainitem.md)
  A dictionary that describes an error chain item.

## Properties

- `Books` ([ManagedMediaListResponse.BooksItem]) *(required)*: An array of dictionaries that describes managed books.
- `CommandUUID` (string): The unique identifier of the command for this response.
- `EnrollmentID` (string) *(required)*: The per-enrollment identifier for the device. The system requires this value if the enrollment type is a user enrollment. Available in iOS 13 and later, macOS 10.15 and later, and visionOS 2 and later.
- `EnrollmentUserID` (string) *(required)*: The per-enrollment identifier for the user. The system requires this value if the enrollment type is a user enrollment on the user channel. Available in macOS 10.15 and later.
- `ErrorChain` ([ManagedMediaListResponse.ErrorChainItem]): An array of dictionaries that describes any errors that occur.
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

- [object ManagedMediaListCommand](managedmedialistcommand.md)
  The command to get a list of the managed books on a device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/managedmedialistresponse)*
# InstallMediaResponse

**Framework**: Device Management  
**Kind**: dictionary

A response from the device after it processes the command to install a book on a device.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 8.0+
- macOS 10.9+

## Declaration

```swift
object InstallMediaResponse
```

## Topics

### Objects
- [object InstallMediaResponse.ErrorChainItem](installmediaresponse/errorchainitem.md)
  A dictionary that describes an error chain item.

## Properties

- `CommandUUID` (string): The unique identifier of the command for this response.
- `EnrollmentID` (string) *(required)*: The per-enrollment identifier for the device. The system requires this value if the enrollment type is a user enrollment. Available: iOS 13+ | iPadOS 13+ | macOS 10.15+
Deprecated: macOS 11+
Removed: macOS 11+
- `EnrollmentUserID` (string) *(required)*: Removed: macOS 11+
- `ErrorChain` ([InstallMediaResponse.ErrorChainItem]): An array of dictionaries that describes any errors that occur.
- `iTunesStoreID` (integer): The book’s iTunes Store identifier, if present in the command. Deprecated: macOS 11+
Removed: macOS 11+
- `MediaType` (string): The media type, which can only be `Book`. Deprecated: macOS 11+
Removed: macOS 11+
- `MediaURL` (string): The URL to retrieve the book, if present in the command. Available: iOS 8+ | iPadOS 8+
Deprecated: macOS 11+
Removed: macOS 11+
- `NotOnConsole` (boolean) *(required)*: If `true`, the device isn’t on-console.
- `PersistentID` (string): The book’s persistent identifier, if present in the command. Available: iOS 8+ | iPadOS 8+
Deprecated: macOS 11+
Removed: macOS 11+
- `RejectionReason` (string): The reason, if installation fails, which is one of the following values: - `CouldNotVerifyITunesStoreID`: The `iTunesStoreID` is invalid.
- `PurchaseNotFound`: The Volume Purchase Program (VPP) license isn’t in the user’s history.
- `AppStoreDisabled`: App Store isn’t available on the device.
- `WrongMediaType`: The media type is invalid. The only valid type is `Book`.
- `DownloadInvalid`: The URL doesn’t lead to a valid book.
- `EnterpriseBooksNotSupportedInMultiUser`: Multiuser mode doesn’t support enterprise books. Deprecated: macOS 11+
Removed: macOS 11+
- `State` (string): The installation state of this book. The `Failed` and `Unknown` states are transient and the device only reports them once. Books from the Book Store report their state as `Installed` instead of `Managed`. Deprecated: macOS 11+
Removed: macOS 11+
- `Status` (string) *(required)*: The status of the response, which is one of the following values: - `Acknowledged`: The device processed the command successfully.
- `Error`: An error occurred. See the `ErrorChain` for more details.
- `CommandFormatError`: A protocol error occurred, which can result from a malformed command.
- `Idle`: The device is idle; there’s no status.
- `NotNow`: The device received the command, but can’t run it.
- `UDID` (string) *(required)*: The device’s UDID (unique device identifier). The system requires this value if the enrollment type is a device enrollment. Deprecated: macOS 11+
Removed: macOS 11+
- `UserID` (string): For macOS, this value is the ID of the user. For Shared iPad, this value is `FFFFFFFF-FFFF-FFFF-FFFF-FFFFFFFFFFFF` to indicate that authentication doesn’t occur. Available: iOS 9.3+ | iPadOS 9.3+ | macOS 10.9+
Deprecated: macOS 11+
Removed: macOS 11+
- `UserLongName` (string) *(required)*: Removed: macOS 11+
- `UserShortName` (string): For macOS, this value is the short name of the user. For Shared iPad, this value is the Managed Apple Account identifier of the user on Shared iPad. It indicates that the token is for the user channel. Available: iOS 9.3+ | iPadOS 9.3+ | macOS 10.9+
Deprecated: macOS 11+
Removed: macOS 11+

## See Also

- [object InstallMediaCommand](installmediacommand.md)
  The command to install a book on a device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/installmediaresponse)*
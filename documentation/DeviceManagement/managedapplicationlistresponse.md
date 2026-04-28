# ManagedApplicationListResponse

**Framework**: Device Management  
**Kind**: dictionary

A response from the device after it processes the command to get the status of all managed apps on a device.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 5.0+
- macOS 11.0+
- tvOS 10.2+
- visionOS 1.1+
- watchOS 10.0+
- Device Assignment Services ?+
- VPP License Management ?+

## Declaration

```swift
object ManagedApplicationListResponse
```

## Topics

### Objects
- [object ManagedApplicationListResponse.ErrorChainItem](managedapplicationlistresponse/errorchainitem.md)
  A dictionary that describes an error chain item.
- [object ManagedApplicationListResponse.ManagedApplicationList](managedapplicationlistresponse/managedapplicationlist-data.dictionary.md)
  A dictionary that contains status information about managed apps.

## Properties

- `CommandUUID` (string): The unique identifier of the command for this response.
- `EnrollmentID` (string) *(required)*: The per-enrollment identifier for the device. The system requires this value if the enrollment type is a user enrollment. Available in iOS 13 and later, macOS 10.15 and later, and visionOS 2 and later.
- `EnrollmentUserID` (string) *(required)*: The per-enrollment identifier for the user. The system requires this value if the enrollment type is a user enrollment on the user channel. Available in macOS 10.15 and later.
- `ErrorChain` ([ManagedApplicationListResponse.ErrorChainItem]): An array of dictionaries that describes any errors that occur.
- `ManagedApplicationList` (ManagedApplicationListResponse.ManagedApplicationList) *(required)*: A dictionary that contains status information about each managed app. The response doesn’t include apps that Declarative Device Management manages.
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

- [object ManagedApplicationListCommand](managedapplicationlistcommand.md)
  The command to get the status of all managed apps on a device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/managedapplicationlistresponse)*
# OSUpdateStatusResponse

**Framework**: Device Management  
**Kind**: dictionary

A response from the device after it processes the command to get the status of operating-system updates on a device.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 9.0+
- macOS 10.11.5+
- tvOS 12.0+
- Device Assignment Services ?+
- VPP License Management ?+

## Declaration

```swift
object OSUpdateStatusResponse
```

## Topics

### Objects
- [object OSUpdateStatusResponse.ErrorChainItem](osupdatestatusresponse/errorchainitem.md)
  A dictionary that describes an error chain item.
- [object OSUpdateStatusResponse.OSUpdateStatusItem](osupdatestatusresponse/osupdatestatusitem.md)
  A dictionary that describes the status of a software update.

## Properties

- `CommandUUID` (string): The unique identifier of the command for this response.
- `EnrollmentID` (string) *(required)*: The per-enrollment identifier for the device. The system requires this value if the enrollment type is a user enrollment. Available in iOS 13 and later, macOS 10.15 and later, and visionOS 2 and later.
- `EnrollmentUserID` (string) *(required)*: The per-enrollment identifier for the user. The system requires this value if the enrollment type is a user enrollment on the user channel. Available in macOS 10.15 and later.
- `ErrorChain` ([OSUpdateStatusResponse.ErrorChainItem]): An array of dictionaries that describes any errors that occur.
- `NotOnConsole` (boolean) *(required)*: If `true`, the device isn’t on-console.
- `OSUpdateStatus` ([OSUpdateStatusResponse.OSUpdateStatusItem]) *(required)*: An array of dictionaries that describes the statuses of software updates. The array is empty if there are no software updates currently in progress. This command only returns the status for System Applications and Configuration Data updates when a software update is managed by a Declarative Device Management [`SoftwareUpdateEnforcementSpecific`](softwareupdateenforcementspecific.md) configuration.
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

- [object OSUpdateStatusCommand](osupdatestatuscommand.md)
  The command to get the status of operating-system updates on a device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/osupdatestatusresponse)*
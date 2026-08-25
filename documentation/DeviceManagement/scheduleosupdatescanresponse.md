# ScheduleOSUpdateScanResponse

**Framework**: Device Management  
**Kind**: dictionary

A response from the device after it processes the command to schedule a background scan for operating-system updates on a device. Removed: use the declarative management `com.apple.configuration.softwareupdate.enforcement.specific` configuration.

**Availability**:
- macOS 10.11+

## Declaration

```swift
object ScheduleOSUpdateScanResponse
```

## Topics

### Objects
- [object ScheduleOSUpdateScanResponse.ErrorChainItem](scheduleosupdatescanresponse/errorchainitem.md)
  A dictionary that describes an error chain item.

## Properties

- `CommandUUID` (string): The unique identifier of the command for this response.
- `EnrollmentID` (string) *(required)*: Removed: macOS 27+
- `EnrollmentUserID` (string) *(required)*: Removed: macOS 27+
- `ErrorChain` ([ScheduleOSUpdateScanResponse.ErrorChainItem]): An array of dictionaries that describes any errors that occur.
- `NotOnConsole` (boolean) *(required)*: If `true`, the device isn’t on-console.
- `ScanInitiated` (boolean) *(required)*: Removed: macOS 27+
- `Status` (string) *(required)*: The status of the response, which is one of the following values: - `Acknowledged`: The device processed the command successfully.
- `Error`: An error occurred. See the `ErrorChain` for more details.
- `CommandFormatError`: A protocol error occurred, which can result from a malformed command.
- `Idle`: The device is idle; there’s no status.
- `NotNow`: The device received the command, but can’t run it.
- `UDID` (string) *(required)*: Removed: macOS 27+
- `UserID` (string): Removed: macOS 27+
- `UserLongName` (string) *(required)*: Removed: macOS 27+
- `UserShortName` (string): Removed: macOS 27+

## See Also

- [object ScheduleOSUpdateScanCommand](scheduleosupdatescancommand.md)
  The command to schedule a background scan for operating-system updates on a device. Removed: use the declarative management `com.apple.configuration.softwareupdate.enforcement.specific` configuration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/scheduleosupdatescanresponse)*
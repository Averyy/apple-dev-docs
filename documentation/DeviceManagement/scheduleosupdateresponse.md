# ScheduleOSUpdateResponse

**Framework**: Device Management  
**Kind**: dictionary

A response from the device after it processes the command to schedule an update of the operating system on a device. Removed: use the declarative management `com.apple.configuration.softwareupdate.enforcement.specific` configuration.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 9.0+
- macOS 10.11+
- tvOS 12.0+

## Declaration

```swift
object ScheduleOSUpdateResponse
```

## Topics

### Objects
- [object ScheduleOSUpdateResponse.ErrorChainItem](scheduleosupdateresponse/errorchainitem.md)
  A dictionary that describes an error chain item.
- [object ScheduleOSUpdateResponse.UpdateResultsItem](scheduleosupdateresponse/updateresultsitem.md)
  The response dictionary that describes the result of processing an operating-system update.

## Properties

- `CommandUUID` (string): The unique identifier of the command for this response.
- `EnrollmentID` (string) *(required)*: Removed: iOS 27+ | iPadOS 27+ | macOS 27+ | tvOS 27+
- `EnrollmentUserID` (string) *(required)*: Removed: iOS 27+ | iPadOS 27+ | macOS 27+ | tvOS 27+
- `ErrorChain` ([ScheduleOSUpdateResponse.ErrorChainItem]): An array of dictionaries that describes any errors that occur.
- `NotOnConsole` (boolean) *(required)*: If `true`, the device isn’t on-console.
- `Status` (string) *(required)*: The status of the response, which is one of the following values: - `Acknowledged`: The device processed the command successfully.
- `Error`: An error occurred. See the `ErrorChain` for more details.
- `CommandFormatError`: A protocol error occurred, which can result from a malformed command.
- `Idle`: The device is idle; there’s no status.
- `NotNow`: The device received the command, but can’t run it.
- `UDID` (string) *(required)*: Removed: iOS 27+ | iPadOS 27+ | macOS 27+ | tvOS 27+
- `UpdateResults` ([ScheduleOSUpdateResponse.UpdateResultsItem]) *(required)*: Removed: iOS 27+ | iPadOS 27+ | macOS 27+ | tvOS 27+
- `UserID` (string): Removed: iOS 27+ | iPadOS 27+ | macOS 27+ | tvOS 27+
- `UserLongName` (string) *(required)*: Removed: iOS 27+ | iPadOS 27+ | macOS 27+ | tvOS 27+
- `UserShortName` (string): Removed: iOS 27+ | iPadOS 27+ | macOS 27+ | tvOS 27+

## See Also

- [object ScheduleOSUpdateCommand](scheduleosupdatecommand.md)
  The command to schedule an update of the operating system on a device. Removed: use the declarative management `com.apple.configuration.softwareupdate.enforcement.specific` configuration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/scheduleosupdateresponse)*
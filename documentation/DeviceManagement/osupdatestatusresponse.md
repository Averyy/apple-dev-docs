# OSUpdateStatusResponse

**Framework**: Device Management  
**Kind**: dictionary

A response from the device after it processes the command to get the status of operating-system updates on a device. Removed: subscribe to the declarative management `softwareupdate.install-state` status item.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 9.0+
- macOS 10.11.5+
- tvOS 12.0+

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
- `EnrollmentID` (string) *(required)*: Removed: iOS 27+ | iPadOS 27+ | macOS 27+ | tvOS 27+
- `EnrollmentUserID` (string) *(required)*: Removed: iOS 27+ | iPadOS 27+ | macOS 27+ | tvOS 27+
- `ErrorChain` ([OSUpdateStatusResponse.ErrorChainItem]): An array of dictionaries that describes any errors that occur.
- `NotOnConsole` (boolean) *(required)*: If `true`, the device isn’t on-console.
- `OSUpdateStatus` ([OSUpdateStatusResponse.OSUpdateStatusItem]) *(required)*: Removed: iOS 27+ | iPadOS 27+ | macOS 27+ | tvOS 27+
- `Status` (string) *(required)*: The status of the response, which is one of the following values: - `Acknowledged`: The device processed the command successfully.
- `Error`: An error occurred. See the `ErrorChain` for more details.
- `CommandFormatError`: A protocol error occurred, which can result from a malformed command.
- `Idle`: The device is idle; there’s no status.
- `NotNow`: The device received the command, but can’t run it.
- `UDID` (string) *(required)*: Removed: iOS 27+ | iPadOS 27+ | macOS 27+ | tvOS 27+
- `UserID` (string): Removed: iOS 27+ | iPadOS 27+ | macOS 27+ | tvOS 27+
- `UserLongName` (string) *(required)*: Removed: iOS 27+ | iPadOS 27+ | macOS 27+ | tvOS 27+
- `UserShortName` (string): Removed: iOS 27+ | iPadOS 27+ | macOS 27+ | tvOS 27+

## See Also

- [object OSUpdateStatusCommand](osupdatestatuscommand.md)
  The command to get the status of operating-system updates on a device. Removed: subscribe to the declarative management `softwareupdate.install-state` status item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/osupdatestatusresponse)*
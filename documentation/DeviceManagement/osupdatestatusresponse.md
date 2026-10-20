# OSUpdateStatusResponse

**Framework**: Device Management  
**Kind**: dictionary  
**Role**: Device Management Command

A response from the device after it processes the command to get the status of operating-system updates on a device. Removed: subscribe to the declarative management `softwareupdate.install-state` status item.

**Availability**:
- iOS 9.0+ - Deprecated in 26.0
- iPadOS 9.0+ - Deprecated in 26.0
- Mac Catalyst 9.0+ - Deprecated in 26.0
- macOS 10.11.5+ - Deprecated in 26.0
- tvOS 12.0+ - Deprecated in 26.0

> **Deprecated**: **Removed** Use the declarative management software update features instead.

## Declaration

```
object OSUpdateStatusResponse
```

## Topics

### Objects
- [object OSUpdateStatusResponse.ErrorChainItem](./osupdatestatusresponse/errorchainitem.md)
  A dictionary that describes an error chain item.
- [object OSUpdateStatusResponse.OSUpdateStatusItem](./osupdatestatusresponse/osupdatestatusitem.md)
  A dictionary that describes the status of a software update.

## Properties

- `CommandUUID` (string) *(deprecated)*: The unique identifier of the command for this response.
- `EnrollmentID` (string) *(required)* *(deprecated)*: ~~The per-enrollment identifier for the device. The system requires this value if the enrollment type is a user enrollment.~~

  ~~Available: iOS 13+ | iPadOS 13+ | macOS 10.15+~~
  ~~Deprecated: iOS 26+ | iPadOS 26+ | macOS 26+ | tvOS 26+~~
  Removed: iOS 27+ | iPadOS 27+ | macOS 27+ | tvOS 27+
- `EnrollmentUserID` (string) *(required)* *(deprecated)*: ~~The per-enrollment identifier for the user. The system requires this value if the enrollment type is a user enrollment on the user channel.~~

  ~~Available: macOS 10.15+~~
  ~~Deprecated: iOS 26+ | iPadOS 26+ | macOS 26+ | tvOS 26+~~
  Removed: iOS 27+ | iPadOS 27+ | macOS 27+ | tvOS 27+
- `ErrorChain` ([OSUpdateStatusResponse.ErrorChainItem]) *(deprecated)*: An array of dictionaries that describes any errors that occur.
- `NotOnConsole` (boolean) *(required)* *(deprecated)*: If `true`, the device isn’t on-console.
- `OSUpdateStatus` ([OSUpdateStatusResponse.OSUpdateStatusItem]) *(required)* *(deprecated)*: ~~An array of dictionaries that describes the statuses of software updates. The array is empty if there are no software updates currently in progress.~~ ~~This command only returns the status for System Applications and Configuration Data updates when a Declarative Device Management [`SoftwareUpdateEnforcementSpecific`](./softwareupdateenforcementspecific.md) configuration manages a software update.~~

  ~~Deprecated: iOS 26+ | iPadOS 26+ | macOS 26+ | tvOS 26+~~
  Removed: iOS 27+ | iPadOS 27+ | macOS 27+ | tvOS 27+
- `Status` (string) *(required)* *(deprecated)*: The status of the response, which is one of the following values:

  - `Acknowledged`: The device processed the command successfully.
  - `Error`: An error occurred. See the `ErrorChain` for more details.
  - `CommandFormatError`: A protocol error occurred, which can result from a malformed command.
  - `Idle`: The device is idle; there’s no status.
  - `NotNow`: The device received the command, but can’t run it.

  **Allowed Values**: `Acknowledged`, `Error`, `CommandFormatError`, `Idle`, `NotNow`
- `UDID` (string) *(required)* *(deprecated)*: ~~The device’s UDID (unique device identifier). The system requires this value if the enrollment type is a device enrollment.~~

  ~~Deprecated: iOS 26+ | iPadOS 26+ | macOS 26+ | tvOS 26+~~
  Removed: iOS 27+ | iPadOS 27+ | macOS 27+ | tvOS 27+
- `UserID` (string) *(deprecated)*: ~~For macOS, this value is the ID of the user.~~

  ~~For Shared iPad, this value is `FFFFFFFF-FFFF-FFFF-FFFF-FFFFFFFFFFFF` to indicate that authentication doesn’t occur.~~

  ~~Available: iOS 9.3+ | iPadOS 9.3+ | macOS 10.11.5+~~
  ~~Deprecated: iOS 26+ | iPadOS 26+ | macOS 26+ | tvOS 26+~~
  Removed: iOS 27+ | iPadOS 27+ | macOS 27+ | tvOS 27+
- `UserLongName` (string) *(required)* *(deprecated)*: ~~The full name of the user.~~

  ~~Available: macOS 10.11.5+~~
  ~~Deprecated: iOS 26+ | iPadOS 26+ | macOS 26+ | tvOS 26+~~
  Removed: iOS 27+ | iPadOS 27+ | macOS 27+ | tvOS 27+
- `UserShortName` (string) *(deprecated)*: ~~For macOS, this value is the short name of the user.~~

  ~~For Shared iPad, this value is the Managed Apple Account identifier of the user on Shared iPad. It indicates that the token is for the user channel.~~

  ~~Available: iOS 9.3+ | iPadOS 9.3+ | macOS 10.11.5+~~
  ~~Deprecated: iOS 26+ | iPadOS 26+ | macOS 26+ | tvOS 26+~~
  Removed: iOS 27+ | iPadOS 27+ | macOS 27+ | tvOS 27+

## See Also

### Commands and responses
- [object OSUpdateStatusCommand](./osupdatestatuscommand.md)
  The command to get the status of operating-system updates on a device. Removed: subscribe to the declarative management `softwareupdate.install-state` status item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/osupdatestatusresponse)*
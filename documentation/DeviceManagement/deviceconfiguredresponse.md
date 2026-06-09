# DeviceConfiguredResponse

**Framework**: Device Management  
**Kind**: dictionary

A response from the device after it processes the command to inform the device that it can allow the user to continue in Setup Assistant.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 9.0+
- macOS 10.11+
- tvOS 10.2+
- visionOS 2.0+

## Declaration

```swift
object DeviceConfiguredResponse
```

## Topics

### Objects
- [object DeviceConfiguredResponse.ErrorChainItem](deviceconfiguredresponse/errorchainitem.md)
  A dictionary that describes an error chain item.

## Properties

- `CommandUUID` (string): The unique identifier of the command for this response.
- `EnrollmentID` (string) *(required)*: The per-enrollment identifier for the device. The system requires this value if the enrollment type is a user enrollment. Available: iOS 13+ | iPadOS 13+ | macOS 10.15+ | visionOS 2+
- `EnrollmentUserID` (string) *(required)*: The per-enrollment identifier for the user. The system requires this value if the enrollment type is a user enrollment on the user channel. Available: macOS 10.15+
- `ErrorChain` ([DeviceConfiguredResponse.ErrorChainItem]): An array of dictionaries that describes any errors that occur.
- `NotOnConsole` (boolean) *(required)*: If `true`, the device isn’t on-console.
- `Status` (string) *(required)*: The status of the response, which is one of the following values: - `Acknowledged`: The device processed the command successfully.
- `Error`: An error occurred. See the `ErrorChain` for more details.
- `CommandFormatError`: A protocol error occurred, which can result from a malformed command.
- `Idle`: The device is idle; there’s no status.
- `NotNow`: The device received the command, but can’t run it.
- `UDID` (string) *(required)*: The device’s UDID (unique device identifier). The system requires this value if the enrollment type is a device enrollment.
- `UserID` (string): For macOS, this value is the ID of the user. For Shared iPad, this value is `FFFFFFFF-FFFF-FFFF-FFFF-FFFFFFFFFFFF` to indicate that authentication doesn’t occur. Available: iOS 9.3+ | iPadOS 9.3+ | macOS 10.11+
- `UserLongName` (string) *(required)*: The full name of the user. Available: macOS 10.11+
- `UserShortName` (string): For macOS, this value is the short name of the user. For Shared iPad, this value is the Managed Apple Account identifier of the user on Shared iPad. It indicates that the token is for the user channel. Available: iOS 9.3+ | iPadOS 9.3+ | macOS 10.11+

## See Also

- [object DeviceConfiguredCommand](deviceconfiguredcommand.md)
  The command to inform the device that it can allow the user to continue in Setup Assistant.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/deviceconfiguredresponse)*
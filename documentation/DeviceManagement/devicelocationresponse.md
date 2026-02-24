# DeviceLocationResponse

**Framework**: Device Management  
**Kind**: dictionary

A response from the device after it processes the command to request the location of a device when in Lost Mode.

**Availability**:
- iOS 9.3+
- iPadOS 9.3+

## Declaration

```swift
object DeviceLocationResponse
```

## Topics

### Objects
- [object DeviceLocationResponse.ErrorChainItem](devicelocationresponse/errorchainitem.md)
  A dictionary that describes an error chain item.

## Properties

- `Altitude` (number) *(required)*: The altitude of the device’s location, which is a negative value if the altitude is unknown.
- `CommandUUID` (string): The unique identifier of the command for this response.
- `Course` (number) *(required)*: The direction the device is traveling, which is a negative value if the course is unknown.
- `EnrollmentID` (string) *(required)*: The per-enrollment identifier for the device. The system requires this value if the enrollment type is a user enrollment. Available in iOS 13 and later, macOS 10.15 and later, and visionOS 2 and later.
- `EnrollmentUserID` (string) *(required)*: The per-enrollment identifier for the user. The system requires this value if the enrollment type is a user enrollment on the user channel. Available in macOS 10.15 and later.
- `ErrorChain` ([DeviceLocationResponse.ErrorChainItem]): An array of dictionaries that describes any errors that occur.
- `HorizontalAccuracy` (number) *(required)*: The radius of uncertainty for the location in meters, which is a negative value if the horizontal accuracy is unknown.
- `Latitude` (number) *(required)*: The latitude of the device’s location.
- `Longitude` (number) *(required)*: The longitude of the device’s location.
- `NotOnConsole` (boolean) *(required)*: If `true`, the device isn’t on-console.
- `Speed` (number) *(required)*: The speed of the device in meters per second, which is a negative value if the speed is unknown.
- `Status` (string) *(required)*: The status of the response, which is one of the following values: - `Acknowledged`: The device processed the command successfully.
- `Error`: An error occurred. See the `ErrorChain` for more details.
- `CommandFormatError`: A protocol error occurred, which can result from a malformed command.
- `Idle`: The device is idle; there’s no status.
- `NotNow`: The device received the command, but can’t run it.
- `Timestamp` (string) *(required)*: The RFC 3339 timestamp of when the server determines the location of the device.
- `UDID` (string) *(required)*: The device’s UDID (unique device identifier). The system requires this value if the enrollment type is a device enrollment.
- `UserID` (string): For macOS, this value is the ID of the user. For Shared iPad, this value is `FFFFFFFF-FFFF-FFFF-FFFF-FFFFFFFFFFFF` to indicate that authentication doesn’t occur.
- `UserLongName` (string) *(required)*: The full name of the user.
- `UserShortName` (string): For macOS, this value is the short name of the user. For Shared iPad, this value is the Managed Apple Account identifier of the user on Shared iPad. It indicates that the token is for the user channel.
- `VerticalAccuracy` (number) *(required)*: The accuracy of the altitude value in meters, which is a negative value if the vertical accuracy is unknown.

## See Also

- [object DeviceLocationCommand](devicelocationcommand.md)
  The command to request the location of a device when in Lost Mode.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/devicelocationresponse)*
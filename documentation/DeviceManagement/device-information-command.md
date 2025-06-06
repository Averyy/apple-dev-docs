# Get Device Information

**Framework**: Device Management  
**Kind**: httpRequest

Get detailed information about a device.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.1+
- watchOS 10.0+
- Device Assignment Services ?+
- VPP License Management ?+

#### Discussion

Refer to the following sections to determine supported channels and requirements, and to see an example request and response.

##### Query Availability

|  |  |
| --- | --- |
| Device Channel | iOS, macOS, Shared iPad, tvOS, watchOS |
| User Channel | macOS, Shared iPad |
| Requires Supervision | - |
| Allowed in User Enrollment | iOS, macOS |
| Required Access Right | Special case (see subkeys) |

##### Example Request and Response

## Topics

### Command and Response
- [object DeviceInformationCommand](deviceinformationcommand.md)
  The command to query a device for specific information.
- [object DeviceInformationResponse](deviceinformationresponse.md)
  A response from the device after it processes the command to get detailed information.

## Request Body

The command to query a device for specific information.

## See Also

- [List the Installed Apps](installed-application-list-command.md)
  Get a list of the installed apps on a device.
- [Release Device from Await Configuration](device-configured-command.md)
  Inform the device that it can allow the user to continue in Setup Assistant.
- [User Configured Command](user-configured-command.md)
  Informs the device that it can continue past Setup Assistant and finish login.
- [List the Installed Restrictions](restrictions-command.md)
  Get a list of restrictions on the device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/device-information-command)*
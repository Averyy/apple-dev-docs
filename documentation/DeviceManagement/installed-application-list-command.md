# List the Installed Apps

**Framework**: Device Management  
**Kind**: httpRequest

Get a list of the installed apps on a device.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- macOS 10.7+
- tvOS 10.2+
- visionOS 1.1+
- watchOS 10.0+
- Device Assignment Services ?+
- VPP License Management ?+

#### Discussion

The response includes system apps on macOS devices, however, it doesn’t include them on iOS devices.

Refer to the following sections to determine supported channels and requirements, and to see request and response examples for iOS and macOS.

##### Query Availability

|  |  |
| --- | --- |
| Device Channel | iOS, macOS, Shared iPad, tvOS, watchOS |
| User Channel | macOS |
| Requires Supervision | - |
| Allowed in User Enrollment | iOS |
| Required Access Right | AllowQueryApplications |

##### Example Request and Response in Ios

##### Example Request and Response in Macos

## Topics

### Command and Response
- [object InstalledApplicationListCommand](installedapplicationlistcommand.md)
  The command to get a list of installed apps on a device.
- [object InstalledApplicationListResponse](installedapplicationlistresponse.md)
  A response from the device after it processes the command to get a list of installed apps.

## Request Body

The command to get a list of installed apps on a device.

## See Also

- [Get Device Information](device-information-command.md)
  Get detailed information about a device.
- [Release Device from Await Configuration](device-configured-command.md)
  Inform the device that it can allow the user to continue in Setup Assistant.
- [User Configured Command](user-configured-command.md)
  Informs the device that it can continue past Setup Assistant and finish login.
- [List the Installed Restrictions](restrictions-command.md)
  Get a list of restrictions on the device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/installed-application-list-command)*
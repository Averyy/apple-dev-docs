# Installed Application List

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

#### Discussion

The response includes system apps on macOS devices, however, it doesn’t include them on iOS devices.

Refer to the following sections to determine supported channels and requirements, and to see request and response examples for iOS and macOS.

##### Command Availability

|  |  |
| --- | --- |
| Device channel | iOS, macOS, Shared iPad, tvOS, visionOS, watchOS |
| User channel | macOS |
| Requires supervision | macOS |
| Allowed in user enrollment | iOS, visionOS |
| Required access right | AllowQueryApplications |

##### Example Request and Response in Ios

##### Example Request and Response in Macos

##### Example Request and Response in Macos

## Topics

### Commands and responses
- [object InstalledApplicationListCommand](installedapplicationlistcommand.md)
  The command to get a list of the installed apps on a device.
- [object InstalledApplicationListResponse](installedapplicationlistresponse.md)
  A response from the device after it processes the command to get a list of the installed apps on a device.

## Request Body

The request object the server returns for the Installed Application List Command.

## See Also

- [Device Information](device-information-command.md)
  Get detailed information about a device.
- [Device Configured](device-configured-command.md)
  Inform the device that it can allow the user to continue in Setup Assistant.
- [User Configured](user-configured-command.md)
  Inform the device that it can continue past Setup Assistant and finish login.
- [Restrictions](restrictions-command.md)
  Get a list of restrictions on the device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/installed-application-list-command)*
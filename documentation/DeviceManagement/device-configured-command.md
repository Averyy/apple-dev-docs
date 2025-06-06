# Release Device from Await Configuration

**Framework**: Device Management  
**Kind**: httpRequest

Inform the device that it can allow the user to continue in Setup Assistant.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- macOS 10.11+
- tvOS 10.2+
- visionOS 2.0+
- Device Assignment Services ?+
- VPP License Management ?+

#### Discussion

This command only works on Device Enrollment Program (DEP) devices that have their cloud configuration set to await configuration.

Refer to the following sections to determine supported channels and requirements, and to see an example request and response.

##### Command Availability

|  |  |
| --- | --- |
| Device Channel | iOS, macOS, Shared iPad, tvOS |
| User Channel | macOS, Shared iPad |
| Requires Supervision | - |
| Allowed in User Enrollment | - |
| Required Access Right | - |

##### Example Request and Response

## Topics

### Command and Response
- [object DeviceConfiguredCommand](deviceconfiguredcommand.md)
  The command to inform a device that it can allow the user to continue in Setup Assistant.
- [object DeviceConfiguredResponse](deviceconfiguredresponse.md)
  A response from the device after it processes the command to allow the user to continue in Setup Assistant.

## Request Body

The command to inform a device that it can allow the user to continue in Setup Assistant.

## See Also

- [List the Installed Apps](installed-application-list-command.md)
  Get a list of the installed apps on a device.
- [Get Device Information](device-information-command.md)
  Get detailed information about a device.
- [User Configured Command](user-configured-command.md)
  Informs the device that it can continue past Setup Assistant and finish login.
- [List the Installed Restrictions](restrictions-command.md)
  Get a list of restrictions on the device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/device-configured-command)*
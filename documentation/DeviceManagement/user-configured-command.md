# User Configured Command

**Framework**: Device Management  
**Kind**: httpRequest

Informs the device that it can continue past Setup Assistant and finish login.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Device Assignment Services ?+
- VPP License Management ?+

#### Discussion

Refer to the following sections to determine supported channels and requirements.

##### Command Availability

|  |  |
| --- | --- |
| Device Channel | - |
| User Channel | Shared iPad |
| Requires Supervision | Shared iPad |
| Allowed in User Enrollment | - |
| Required Access Right | - |

## Topics

### Command and Response
- [object UserConfiguredCommand](userconfiguredcommand.md)
  The command to inform a Shared iPad that the system has configured the user and can allow the user to continue in Setup Assistant.
- [object UserConfiguredResponse](userconfiguredresponse.md)
  A response from the Shared iPad after it processes the command to configure the user and continue in Setup Assistant.

## Request Body

missing

## See Also

- [List the Installed Apps](installed-application-list-command.md)
  Get a list of the installed apps on a device.
- [Get Device Information](device-information-command.md)
  Get detailed information about a device.
- [Release Device from Await Configuration](device-configured-command.md)
  Inform the device that it can allow the user to continue in Setup Assistant.
- [List the Installed Restrictions](restrictions-command.md)
  Get a list of restrictions on the device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/user-configured-command)*
# User Configured

**Framework**: Device Management  
**Kind**: httpRequest

Inform the device that it can continue past Setup Assistant and finish login.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+

#### Discussion

Refer to the following sections to determine supported channels and requirements.

##### Command Availability

|  |  |
| --- | --- |
| Device channel | iOS |
| User channel | NA |
| Requires supervision | iOS |
| Allowed in user enrollment | NA |
| Required access right | NA |

## Topics

### Commands and responses
- [object UserConfiguredCommand](userconfiguredcommand.md)
  The command to inform the device that it can continue past Setup Assistant and finish login.
- [object UserConfiguredResponse](userconfiguredresponse.md)
  A response from the device after it processes the command to inform the device that it can continue past Setup Assistant and finish login.

## Request Body

The request object the server returns for the User Configured Command.

## See Also

- [Device Information](device-information-command.md)
  Get detailed information about a device.
- [Device Configured](device-configured-command.md)
  Inform the device that it can allow the user to continue in Setup Assistant.
- [Restrictions](restrictions-command.md)
  Get a list of restrictions on the device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/user-configured-command)*
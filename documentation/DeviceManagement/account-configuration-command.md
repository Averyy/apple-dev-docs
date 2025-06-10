# Account Configuration

**Framework**: Device Management  
**Kind**: httpRequest

Create and configure a local administrator account on a device.

**Availability**:
- macOS 10.11+

## Mentions

- [Implementing Platform SSO for unattended device enrollment](implementing-platform-sso-for-unattended-device-enrollment.md)

#### Discussion

Refer to the following sections to determine supported channels and requirements, and to see an example request and response.

##### Command Availability

|  |  |
| --- | --- |
| Device channel | macOS |
| User channel | NA |
| Requires supervision | macOS |
| Allowed in user enrollment | NA |
| Required access right | NA |

##### Example Request and Response

## Topics

### Commands and responses
- [object AccountConfigurationCommand](accountconfigurationcommand.md)
  The command to create and configure a local administrator account on a device.
- [object AccountConfigurationResponse](accountconfigurationresponse.md)
  A response from the device after it processes the command to create and configure a local administrator account on a device.

## Request Body

The request object the server returns for the Account Configuration Command.

## See Also

- [Invite To Program](invite-to-program-command.md)
  Invite a user to join the Volume Purchase Program (VPP).


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/account-configuration-command)*
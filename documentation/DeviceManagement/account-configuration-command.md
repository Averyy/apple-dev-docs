# Account Configuration

**Framework**: Device Management  
**Kind**: httpRequest

Create and configure a local administrator account on a device.

**Availability**:
- macOS 10.11+
- Device Assignment Services ?+
- VPP License Management ?+

#### Discussion

Refer to the following sections to determine supported channels and requirements, and to see an example request and response.

##### Command Availability

|  |  |
| --- | --- |
| Device Channel | macOS |
| User Channel | - |
| Requires Supervision | macOS |
| Allowed in User Enrollment | - |
| Required Access Right | - |

##### Example Request and Response

## Topics

### Command and Response
- [object AccountConfigurationCommand](accountconfigurationcommand.md)
  The command to create a local administrator account on a device.
- [object AccountConfigurationResponse](accountconfigurationresponse.md)
  A response from the device after it processes the command to create and configure a local administrator account.

## Request Body

The command to create a local administrator account on a device.

## See Also

- [Invite to the Program](invite-to-program-command.md)
  Invite a user to join the Volume Purchase Program (VPP).


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/account-configuration-command)*
# Set Auto Admin Password

**Framework**: Device Management  
**Kind**: httpRequest

Update the local administrator account password.

**Availability**:
- macOS 10.11+

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
- [object SetAutoAdminPasswordCommand](setautoadminpasswordcommand.md)
  The command to update the local administrator account password.
- [object SetAutoAdminPasswordResponse](setautoadminpasswordresponse.md)
  A response from the device after it processes the command to update the local administrator account password.

## Request Body

The request object the server returns for the Set Auto Admin Password Command.

## See Also

- [Clear Passcode](clear-passcode-command.md)
  Remove the passcode from a device.
- [Clear Restrictions Password](clear-restrictions-password-command.md)
  Clear the Screen Time password and the restrictions on a device.
- [Unlock User Account](unlock-user-account-command.md)
  Unlock a user account that the system locked because of too many failed password attempts.
- [Set Firmware Password](set-firmware-password-command.md)
  Change or clear the firmware password on a device.
- [Verify Firmware Password](verify-firmware-password-command.md)
  Verify the firmware password on a device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/set-auto-admin-password-command)*
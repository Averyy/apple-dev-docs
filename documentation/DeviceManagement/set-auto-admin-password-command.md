# Set the Local Administrator Password

**Framework**: Device Management  
**Kind**: httpRequest

Update the local administrator account password.

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
- [object SetAutoAdminPasswordCommand](setautoadminpasswordcommand.md)
  The command to change the password of a local administrator account that Setup Assistant creates on a device.
- [object SetAutoAdminPasswordResponse](setautoadminpasswordresponse.md)
  A response from the device after it processes the command to update the local administrator account password.

## Request Body

The command to change the password of a local administrator account that Setup Assistant creates on a device.

## See Also

- [Clear the Passcode](clear-passcode-command.md)
  Remove the passcode from a device.
- [Clear the Restrictions Password](clear-restrictions-password-command.md)
  Clear the restrictions password and the restrictions on a device.
- [Unlock a User Account](unlock-user-account-command.md)
  Unlock a user account that the system locked because of too many failed password attempts.
- [Set the Firmware Password](set-firmware-password-command.md)
  Change or clear the firmware password on a device.
- [Verify the Firmware Password](verify-firmware-password-command.md)
  Verify the firmware password on a device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/set-auto-admin-password-command)*
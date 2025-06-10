# Verify Firmware Password

**Framework**: Device Management  
**Kind**: httpRequest

Verify the firmware password on a device.

**Availability**:
- macOS 10.13+

#### Discussion

This command has a throttle interval to prevent executing it more frequently than every 30 seconds. Requests that occur within the throttle interval return an error.

Refer to the following sections to determine supported channels and requirements, and to see an example request and response.

This command isn’t supported on Mac computers with Apple silicon.

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
- [object VerifyFirmwarePasswordCommand](verifyfirmwarepasswordcommand.md)
  The command to verify the firmware password on a device.
- [object VerifyFirmwarePasswordResponse](verifyfirmwarepasswordresponse.md)
  A response from the device after it processes the command to verify the firmware password on a device.

## Request Body

The request object the server returns for the Verify Firmware Password Command.

## See Also

- [Clear Passcode](clear-passcode-command.md)
  Remove the passcode from a device.
- [Clear Restrictions Password](clear-restrictions-password-command.md)
  Clear the restrictions password and the restrictions on a device.
- [Unlock User Account](unlock-user-account-command.md)
  Unlock a user account that the system locked because of too many failed password attempts.
- [Set Auto Admin Password](set-auto-admin-password-command.md)
  Update the local administrator account password.
- [Set Firmware Password](set-firmware-password-command.md)
  Change or clear the firmware password on a device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/verify-firmware-password-command)*
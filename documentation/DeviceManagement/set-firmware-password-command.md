# Set Firmware Password

**Framework**: Device Management  
**Kind**: httpRequest

Change or clear the firmware password on a device.

**Availability**:
- macOS 10.13+

#### Discussion

This command has a throttle interval to prevent executing it more frequently than every 30 seconds. Requests that occur within the throttle interval return an error.

> ❗ **Important**:  There’s no way to set or clear a firmware password in MDM without knowing the current password, unless the server provides a way to prompt the administrator for the current password. Contact AppleCare service and support if the current password is unknown.

After processing the command, the device restarts so that the new firmware password takes effect. This command returns an error and fails if a firmware password is already pending.

Refer to the following sections to determine supported channels and requirements, and to see an example request and response.

This command isn’t supported on a Mac with Apple silicon.

##### Command Availability

|  |  |
| --- | --- |
| Device channel | macOS |
| User channel | NA |
| Requires supervision | macOS |
| Allowed in user enrollment | NA |
| Required access right | DeviceLockAndRemovePasscode |

##### Example Request and Response

## Topics

### Commands and responses
- [object SetFirmwarePasswordCommand](setfirmwarepasswordcommand.md)
  The command to change or clear the firmware password on a device.
- [object SetFirmwarePasswordResponse](setfirmwarepasswordresponse.md)
  A response from the device after it processes the command to change or clear the firmware password on a device.

## Request Body

The request object the server returns for the Set Firmware Password Command.

## See Also

- [Clear Passcode](clear-passcode-command.md)
  Remove the passcode from a device.
- [Clear Restrictions Password](clear-restrictions-password-command.md)
  Clear the Screen Time password and the restrictions on a device.
- [Unlock User Account](unlock-user-account-command.md)
  Unlock a user account that the system locked because of too many failed password attempts.
- [Set Auto Admin Password](set-auto-admin-password-command.md)
  Update the local administrator account password.
- [Verify Firmware Password](verify-firmware-password-command.md)
  Verify the firmware password on a device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/set-firmware-password-command)*
# Unlock User Account

**Framework**: Device Management  
**Kind**: httpRequest

Unlock a user account that the system locked because of too many failed password attempts.

**Availability**:
- macOS 10.13+

#### Discussion

Refer to the following sections to determine supported channels and requirements, and to see an example request and response.

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
- [object UnlockUserAccountCommand](unlockuseraccountcommand.md)
  The command to unlock a user account that the system locked because of too many failed password attempts.
- [object UnlockUserAccountResponse](unlockuseraccountresponse.md)
  A response from the device after it processes the command to unlock a user account that the system locked because of too many failed password attempts.

## Request Body

The request object the server returns for the Unlock User Account Command.

## See Also

- [Clear Passcode](clear-passcode-command.md)
  Remove the passcode from a device.
- [Clear Restrictions Password](clear-restrictions-password-command.md)
  Clear the restrictions password and the restrictions on a device.
- [Set Auto Admin Password](set-auto-admin-password-command.md)
  Update the local administrator account password.
- [Set Firmware Password](set-firmware-password-command.md)
  Change or clear the firmware password on a device.
- [Verify Firmware Password](verify-firmware-password-command.md)
  Verify the firmware password on a device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/unlock-user-account-command)*
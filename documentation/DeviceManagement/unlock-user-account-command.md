# Unlock a User Account

**Framework**: Device Management  
**Kind**: httpRequest

Unlock a user account that the system locked because of too many failed password attempts.

**Availability**:
- macOS 10.13+
- Device Assignment Services ?+
- VPP License Management ?+

#### Discussion

Refer to the following sections to determine supported channels and requirements, and to see an example request and response.

##### Command Availability

|  |  |
| --- | --- |
| Device Channel | macOS |
| User Channel | - |
| Requires Supervision | - |
| Allowed in User Enrollment | - |
| Required Access Right | DeviceLockAndRemovePasscode |

##### Example Request and Response

## Topics

### Command and Response
- [object UnlockUserAccountCommand](unlockuseraccountcommand.md)
  The command to unlock a local user account on a device.
- [object UnlockUserAccountResponse](unlockuseraccountresponse.md)
  A response from the device after it processes the command to unlock a user account.

## Request Body

The command to unlock a local user account on a device.

## See Also

- [Clear the Passcode](clear-passcode-command.md)
  Remove the passcode from a device.
- [Clear the Restrictions Password](clear-restrictions-password-command.md)
  Clear the restrictions password and the restrictions on a device.
- [Set the Local Administrator Password](set-auto-admin-password-command.md)
  Update the local administrator account password.
- [Set the Firmware Password](set-firmware-password-command.md)
  Change or clear the firmware password on a device.
- [Verify the Firmware Password](verify-firmware-password-command.md)
  Verify the firmware password on a device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/unlock-user-account-command)*
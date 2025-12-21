# Clear Restrictions Password

**Framework**: Device Management  
**Kind**: httpRequest

Clear the Screen Time password and the restrictions on a device.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+

#### Discussion

In iOS 11 and earlier, this command clears the restrictions password and all restrictions that the password protects.

In iOS 12.2 and later, if Screen Time uses iCloud to share its settings (Share Across Devices), this command disables Screen Time entirely and clears its restrictions. If the user is a child in an iCloud family, the command fails. Otherwise, if Screen Time isn’t using iCloud, this command clears the passcode, but not the restrictions, and it leaves Screen Time enabled.

Refer to the following sections to determine supported channels and requirements, and to see an example request and response.

##### Command Availability

|  |  |
| --- | --- |
| Device channel | iOS |
| User channel | NA |
| Requires supervision | iOS |
| Allowed in user enrollment | NA |
| Required access right | NA |

##### Example Request and Response

## Topics

### Commands and responses
- [object ClearRestrictionsPasswordCommand](clearrestrictionspasswordcommand.md)
  The command to clear the Screen Time password and the restrictions on a device.
- [object ClearRestrictionsPasswordResponse](clearrestrictionspasswordresponse.md)
  A response from the device after it processes the command to clear the Screen Time password and the restrictions on a device.

## Request Body

The request object the server returns for the Clear Restrictions Password Command.

## See Also

- [Clear Passcode](clear-passcode-command.md)
  Remove the passcode from a device.
- [Unlock User Account](unlock-user-account-command.md)
  Unlock a user account that the system locked because of too many failed password attempts.
- [Set Auto Admin Password](set-auto-admin-password-command.md)
  Update the local administrator account password.
- [Set Firmware Password](set-firmware-password-command.md)
  Change or clear the firmware password on a device.
- [Verify Firmware Password](verify-firmware-password-command.md)
  Verify the firmware password on a device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/clear-restrictions-password-command)*
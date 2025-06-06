# Clear the Restrictions Password

**Framework**: Device Management  
**Kind**: httpRequest

Clear the restrictions password and the restrictions on a device.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Device Assignment Services ?+
- VPP License Management ?+

#### Discussion

In iOS 11 and earlier, this command clears the restrictions password and all restrictions that the password protects.

In iOS 12.2 and later, if Screen Time uses iCloud to share its settings (Share Across Devices), this command disables Screen Time entirely and clears its restrictions. If the user is a child in an iCloud family, the command fails. Otherwise, if Screen Time isn’t using iCloud, this command clears the passcode, but not the restrictions, and it leaves Screen Time enabled.

Refer to the following sections to determine supported channels and requirements, and to see an example request and response.

##### Command Availability

|  |  |
| --- | --- |
| Device Channel | iOS |
| User Channel | - |
| Requires Supervision | iOS |
| Allowed in User Enrollment | - |
| Required Access Right | - |

##### Example Request and Response

## Topics

### Command and Response
- [object ClearRestrictionsPasswordCommand](clearrestrictionspasswordcommand.md)
  The command to clear the restrictions passcode on a device to disable or edit parental controls.
- [object ClearRestrictionsPasswordResponse](clearrestrictionspasswordresponse.md)
  A response from the device after it processes the command to clear the restrictions password and the restrictions on a device.

## Request Body

The command to clear the restrictions passcode on a device to disable or edit parental controls.

## See Also

- [Clear the Passcode](clear-passcode-command.md)
  Remove the passcode from a device.
- [Unlock a User Account](unlock-user-account-command.md)
  Unlock a user account that the system locked because of too many failed password attempts.
- [Set the Local Administrator Password](set-auto-admin-password-command.md)
  Update the local administrator account password.
- [Set the Firmware Password](set-firmware-password-command.md)
  Change or clear the firmware password on a device.
- [Verify the Firmware Password](verify-firmware-password-command.md)
  Verify the firmware password on a device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/clear-restrictions-password-command)*
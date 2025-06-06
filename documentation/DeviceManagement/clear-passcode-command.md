# Clear the Passcode

**Framework**: Device Management  
**Kind**: httpRequest

Remove the passcode from a device.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- visionOS 1.1+
- watchOS 10.0+
- Device Assignment Services ?+
- VPP License Management ?+

#### Discussion

Clearing the passcode in iOS 16 no longer adds the passcode to the history of passcodes. Therefore, the user can reuse the cleared passcode even when the `Passcode` payload has the `pinHistory` key set.

Refer to the following sections to determine supported channels and requirements, and to see an example request and response.

##### Command Availability

|  |  |
| --- | --- |
| Device Channel | iOS, watchOS |
| User Channel | - |
| Requires Supervision | - |
| Allowed in User Enrollment | - |
| Required Access Right | AllowPasscodeRemovalAndLock |

##### Example Request and Response

## Topics

### Command and Response
- [object ClearPasscodeCommand](clearpasscodecommand.md)
  The command to clear the passcode on a device.
- [object ClearPasscodeResponse](clearpasscoderesponse.md)
  A response from the device after it processes the command to remove the passcode from a device.

## Request Body

The command to clear the passcode on a device.

## See Also

- [Clear the Restrictions Password](clear-restrictions-password-command.md)
  Clear the restrictions password and the restrictions on a device.
- [Unlock a User Account](unlock-user-account-command.md)
  Unlock a user account that the system locked because of too many failed password attempts.
- [Set the Local Administrator Password](set-auto-admin-password-command.md)
  Update the local administrator account password.
- [Set the Firmware Password](set-firmware-password-command.md)
  Change or clear the firmware password on a device.
- [Verify the Firmware Password](verify-firmware-password-command.md)
  Verify the firmware password on a device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/clear-passcode-command)*
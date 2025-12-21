# Clear Passcode

**Framework**: Device Management  
**Kind**: httpRequest

Remove the passcode from a device.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- visionOS 1.1+
- watchOS 10.0+

#### Discussion

Clearing the passcode in iOS 16 no longer adds the passcode to the history of passcodes. Therefore, the user can reuse the cleared passcode even when the `Passcode` payload has the `pinHistory` key set.

Refer to the following sections to determine supported channels and requirements, and to see an example request and response.

##### Command Availability

|  |  |
| --- | --- |
| Device channel | iOS, visionOS, watchOS |
| User channel | NA |
| Requires supervision | NA |
| Allowed in user enrollment | NA |
| Required access right | AllowPasscodeRemovalAndLock |

##### Example Request and Response

## Topics

### Commands and responses
- [object ClearPasscodeCommand](clearpasscodecommand.md)
  The command to remove the passcode from a device.
- [object ClearPasscodeResponse](clearpasscoderesponse.md)
  A response from the device after it processes the command to remove the passcode from a device.

## Request Body

The request object the server returns for the Clear Passcode Command.

## See Also

- [Clear Restrictions Password](clear-restrictions-password-command.md)
  Clear the Screen Time password and the restrictions on a device.
- [Unlock User Account](unlock-user-account-command.md)
  Unlock a user account that the system locked because of too many failed password attempts.
- [Set Auto Admin Password](set-auto-admin-password-command.md)
  Update the local administrator account password.
- [Set Firmware Password](set-firmware-password-command.md)
  Change or clear the firmware password on a device.
- [Verify Firmware Password](verify-firmware-password-command.md)
  Verify the firmware password on a device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/clear-passcode-command)*
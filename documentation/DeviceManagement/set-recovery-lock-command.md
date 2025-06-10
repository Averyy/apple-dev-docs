# Set Recovery Lock

**Framework**: Device Management  
**Kind**: httpRequest

Set or clear the Recovery Lock password.

**Availability**:
- macOS 11.5+

#### Discussion

This command sets, or clears, a password on booting to recoveryOS. When the device unenrolls MDM the system removes the recovery password.

This command is only available with Apple silicon.

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
- [object SetRecoveryLockCommand](setrecoverylockcommand.md)
  The command to set or clear the Recovery Lock password.
- [object SetRecoveryLockResponse](setrecoverylockresponse.md)
  A response from the device after it processes the command to set or clear the Recovery Lock password.

## Request Body

The request object the server returns for the Set Recovery Lock Command.

## See Also

- [Verify Recovery Lock](verify-recovery-lock-command.md)
  Verify the device’s Recovery Lock password.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/set-recovery-lock-command)*
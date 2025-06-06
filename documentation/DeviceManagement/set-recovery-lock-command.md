# Set Recovery Lock Command

**Framework**: Device Management  
**Kind**: httpRequest

Set or clear the Recovery Lock password.

**Availability**:
- macOS 11.5+
- Device Assignment Services ?+
- VPP License Management ?+

#### Discussion

This command sets, or clears, a password on booting to recoveryOS. When the device unenrolls MDM the system removes the recovery password.

This command is only available with Apple silicon.

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
- [object SetRecoveryLockCommand](setrecoverylockcommand.md)
  The command to set the password for Recovery Lock.
- [object SetRecoveryLockResponse](setrecoverylockresponse.md)
  A response from the device after it sets the password for Recovery Lock.

## Request Body

The command to set the password for Recovery Lock.

## See Also

- [Verify Recovery Lock Command](verify-recovery-lock-command.md)
  Verify the device’s Recovery Lock password.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/set-recovery-lock-command)*
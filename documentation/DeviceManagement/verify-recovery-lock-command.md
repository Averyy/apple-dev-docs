# Verify Recovery Lock Command

**Framework**: Device Management  
**Kind**: httpRequest

Verify the device’s Recovery Lock password.

**Availability**:
- macOS 11.5+
- Device Assignment Services ?+
- VPP License Management ?+

#### Discussion

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
- [object VerifyRecoveryLockCommand](verifyrecoverylockcommand.md)
  The command to verify the password for Recovery Lock.
- [object VerifyRecoveryLockResponse](verifyrecoverylockresponse.md)
  A response from the device after it verifies the password for Recovery Lock.

## Request Body

The command to verify the password for Recovery Lock.

## See Also

- [Set Recovery Lock Command](set-recovery-lock-command.md)
  Set or clear the Recovery Lock password.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/verify-recovery-lock-command)*
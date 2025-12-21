# Verify Recovery Lock

**Framework**: Device Management  
**Kind**: httpRequest

Verify the device’s Recovery Lock password.

**Availability**:
- macOS 11.5+

#### Discussion

This command is only available on a Mac with Apple silicon.

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
- [object VerifyRecoveryLockCommand](verifyrecoverylockcommand.md)
  The command to verify the device’s Recovery Lock password.
- [object VerifyRecoveryLockResponse](verifyrecoverylockresponse.md)
  A response from the device after it processes the command to verify the device’s Recovery Lock password.

## Request Body

The request object the server returns for the Verify Recovery Lock Command.

## See Also

- [Set Recovery Lock](set-recovery-lock-command.md)
  Set or clear the Recovery Lock password.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/verify-recovery-lock-command)*
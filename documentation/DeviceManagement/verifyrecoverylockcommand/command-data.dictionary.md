# VerifyRecoveryLockCommand.Command

**Framework**: Device Management  
**Kind**: dictionary  
**Role**: Device Management Command

The command to verify the device’s Recovery Lock password.

**Availability**:
- macOS 11.5+

## Declaration

```
object VerifyRecoveryLockCommand.Command
```

## Properties

- `Password` (string) *(required)*: The password to verify.
- `RequestRequiresNetworkTether` (boolean): If `true`, the device needs to be network-tethered to run the command.

  **Default**: `false`
- `RequestType` (string) *(required)*: The request type for this command.

  **Allowed Values**: `VerifyRecoveryLock`


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/verifyrecoverylockcommand/command-data.dictionary)*
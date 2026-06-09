# SetRecoveryLockCommand.Command

**Framework**: Device Management  
**Kind**: dictionary

The command to set or clear the Recovery Lock password.

**Availability**:
- macOS 11.5+

## Declaration

```swift
object SetRecoveryLockCommand.Command
```

## Properties

- `CurrentPassword` (string): If the device has a Recovery Lock password set, the system requires the current password.
- `NewPassword` (string) *(required)*: The new password for Recovery Lock. Set as an empty string to clear the Recovery Lock password.
- `RequestRequiresNetworkTether` (boolean): If `true`, the device needs to be network-tethered to run the command.
- `RequestType` (string) *(required)*: The request type for this command.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/setrecoverylockcommand/command-data.dictionary)*
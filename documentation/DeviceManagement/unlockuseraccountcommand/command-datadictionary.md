# UnlockUserAccountCommand.Command

**Framework**: Device Management  
**Kind**: dictionary

The command to unlock a user account that the system locked because of too many failed password attempts.

**Availability**:
- macOS 10.13+
- Device Assignment Services ?+
- VPP License Management ?+

## Declaration

```swift
object UnlockUserAccountCommand.Command
```

## Properties

- `RequestRequiresNetworkTether` (boolean): If `true`, the device needs to be network-tethered to run the command.
- `RequestType` (string) *(required)*: The request type for this command.
- `UserName` (string) *(required)*: The user name of the local account, which can be any local account on the system, not just a managed user account.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/unlockuseraccountcommand/command-data.dictionary)*
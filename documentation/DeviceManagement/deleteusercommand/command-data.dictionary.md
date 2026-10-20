# DeleteUserCommand.Command

**Framework**: Device Management  
**Kind**: dictionary

The command to delete a user’s account from a device.

**Availability**:
- iOS 9.3+
- iPadOS 9.3+
- Mac Catalyst 9.3+
- macOS 10.13+

## Declaration

```swift
object DeleteUserCommand.Command
```

## Properties

- `DeleteAllUsers` (boolean): If `true`, the system attempts to delete all users from the device. If `ForceDeletion` is `false`, the system generates an error instead and doesn’t delete users who have data that’s pending sync. Available: iOS 14+ | iPadOS 14+
- `ForceDeletion` (boolean): If `true`, the system deletes the account even if the user has data that’s pending sync to the cloud. Available: iOS 9.3+ | iPadOS 9.3+
- `RequestRequiresNetworkTether` (boolean): If `true`, the device needs to be network-tethered to run the command.
- `RequestType` (string) *(required)*: The request type for this command.
- `UserName` (string): The user name of the account to delete. The device requires this key when the value for `DeleteAllUsers` is absent or `false`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/deleteusercommand/command-data.dictionary)*
# LogOutUserCommand.Command

**Framework**: Device Management  
**Kind**: dictionary

The command to force the current user to log out of a device.

**Availability**:
- iOS 9.3+
- iPadOS 9.3+
- Mac Catalyst 9.3+

## Declaration

```swift
object LogOutUserCommand.Command
```

## Properties

- `RequestRequiresNetworkTether` (boolean): If `true`, the device needs to be network-tethered to run the command.
- `RequestType` (string) *(required)*: The request type for this command.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/logoutusercommand/command-data.dictionary)*
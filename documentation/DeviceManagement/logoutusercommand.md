# LogOutUserCommand

**Framework**: Device Management  
**Kind**: dictionary

The command to force the current user to log out of a device.

**Availability**:
- iOS 9.3+
- iPadOS 9.3+
- Mac Catalyst 9.3+

## Declaration

```swift
object LogOutUserCommand
```

## Topics

### Objects
- [object LogOutUserCommand.Command](logoutusercommand/command-data.dictionary.md)
  The command to force the current user to log out of a device.

## Properties

- `Command` (LogOutUserCommand.Command) *(required)*: The command dictionary.
- `CommandUUID` (string) *(required)*: The unique identifier of the command.

## See Also

- [object LogOutUserResponse](logoutuserresponse.md)
  A response from the device after it processes the command to force the current user to log out of a device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/logoutusercommand)*
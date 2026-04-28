# EnableLostModeCommand

**Framework**: Device Management  
**Kind**: dictionary

The command to enable Lost Mode on a device, which provides a message and phone number on the Lock Screen.

**Availability**:
- iOS 9.3+
- iPadOS 9.3+
- Mac Catalyst 9.3+
- Device Assignment Services ?+
- VPP License Management ?+

## Declaration

```swift
object EnableLostModeCommand
```

## Topics

### Objects
- [object EnableLostModeCommand.Command](enablelostmodecommand/command-data.dictionary.md)
  The command to enable Lost Mode on a device, which provides a message and phone number on the Lock Screen.

## Properties

- `Command` (EnableLostModeCommand.Command) *(required)*: The command dictionary.
- `CommandUUID` (string) *(required)*: The unique identifier of the command.

## See Also

- [object EnableLostModeResponse](enablelostmoderesponse.md)
  A response from the device after it processes the command to enable Lost Mode on a device, which provides a message and phone number on the Lock Screen.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/enablelostmodecommand)*
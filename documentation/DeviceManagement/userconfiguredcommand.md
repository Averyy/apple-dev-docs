# UserConfiguredCommand

**Framework**: Device Management  
**Kind**: dictionary

The command to inform the device that it can continue past Setup Assistant and finish login.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+

## Declaration

```swift
object UserConfiguredCommand
```

## Topics

### Objects
- [object UserConfiguredCommand.Command](userconfiguredcommand/command-data.dictionary.md)
  The command to inform the device that it can continue past Setup Assistant and finish login.

## Properties

- `Command` (UserConfiguredCommand.Command) *(required)*: The command dictionary.
- `CommandUUID` (string) *(required)*: The unique identifier of the command.

## See Also

- [object UserConfiguredResponse](userconfiguredresponse.md)
  A response from the device after it processes the command to inform the device that it can continue past Setup Assistant and finish login.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/userconfiguredcommand)*
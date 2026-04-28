# ClearPasscodeCommand

**Framework**: Device Management  
**Kind**: dictionary

The command to remove the passcode from a device.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 4.0+
- visionOS 1.1+
- watchOS 10.0+
- Device Assignment Services ?+
- VPP License Management ?+

## Declaration

```swift
object ClearPasscodeCommand
```

## Mentions

- [Managing Passcodes](managing-passcodes.md)
- [Handling NotNow Status Responses](handling-notnow-status-responses.md)

## Topics

### Objects
- [object ClearPasscodeCommand.Command](clearpasscodecommand/command-data.dictionary.md)
  The command to remove the passcode from a device.

## Properties

- `Command` (ClearPasscodeCommand.Command) *(required)*: The command dictionary.
- `CommandUUID` (string) *(required)*: The unique identifier of the command.

## See Also

- [object ClearPasscodeResponse](clearpasscoderesponse.md)
  A response from the device after it processes the command to remove the passcode from a device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/clearpasscodecommand)*
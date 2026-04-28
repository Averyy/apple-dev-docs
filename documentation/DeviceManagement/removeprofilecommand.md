# RemoveProfileCommand

**Framework**: Device Management  
**Kind**: dictionary

The command to remove a previously installed profile from the device.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 4.0+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.1+
- watchOS 10.0+
- Device Assignment Services ?+
- VPP License Management ?+

## Declaration

```swift
object RemoveProfileCommand
```

## Topics

### Objects
- [object RemoveProfileCommand.Command](removeprofilecommand/command-data.dictionary.md)
  The command to remove a previously installed profile from the device.

## Properties

- `Command` (RemoveProfileCommand.Command) *(required)*: The command dictionary.
- `CommandUUID` (string) *(required)*: The unique identifier of the command.

## See Also

- [object RemoveProfileResponse](removeprofileresponse.md)
  A response from the device after it processes the command to remove a previously installed profile from the device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/removeprofilecommand)*
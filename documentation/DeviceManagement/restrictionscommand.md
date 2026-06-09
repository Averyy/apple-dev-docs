# RestrictionsCommand

**Framework**: Device Management  
**Kind**: dictionary

The command to get a list of restrictions on the device.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 4.0+
- tvOS 9.0+
- visionOS 1.1+
- watchOS 10.0+

## Declaration

```swift
object RestrictionsCommand
```

## Mentions

- [Handling NotNow status responses](handling-notnow-status-responses.md)

## Topics

### Objects
- [object RestrictionsCommand.Command](restrictionscommand/command-data.dictionary.md)
  The command to get a list of restrictions on the device.

## Properties

- `Command` (RestrictionsCommand.Command) *(required)*: The command dictionary.
- `CommandUUID` (string) *(required)*: The unique identifier of the command.

## See Also

- [object RestrictionsResponse](restrictionsresponse.md)
  A response from the device after it processes the command to get a list of restrictions on the device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/restrictionscommand)*
# SecurityInfoCommand

**Framework**: Device Management  
**Kind**: dictionary

The command to get security-related information about a device.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 4.0+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.1+
- watchOS 10.0+

## Declaration

```swift
object SecurityInfoCommand
```

## Mentions

- [Deploy software updates using declarative management](deploy-software-updates-using-declarative-management.md)
- [Managing passcodes](managing-passcodes.md)

## Topics

### Objects
- [object SecurityInfoCommand.Command](securityinfocommand/command-data.dictionary.md)
  The command to get security-related information about a device.

## Properties

- `Command` (SecurityInfoCommand.Command) *(required)*: The command dictionary.
- `CommandUUID` (string) *(required)*: The unique identifier of the command.

## See Also

- [object SecurityInfoResponse](securityinforesponse.md)
  A response from the device after it processes the command to get security-related information about a device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/securityinfocommand)*
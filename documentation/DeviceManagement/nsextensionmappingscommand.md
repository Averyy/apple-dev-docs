# NSExtensionMappingsCommand

**Framework**: Device Management  
**Kind**: dictionary

The command to get a list of the installed extensions for a user on a device.

**Availability**:
- macOS 10.13+
- Device Assignment Services ?+
- VPP License Management ?+

## Declaration

```swift
object NSExtensionMappingsCommand
```

## Topics

### Objects
- [object NSExtensionMappingsCommand.Command](nsextensionmappingscommand/command-data.dictionary.md)
  The command to get a list of the installed extensions for a user on a device.

## Properties

- `Command` (NSExtensionMappingsCommand.Command) *(required)*: The command dictionary.
- `CommandUUID` (string) *(required)*: The unique identifier of the command.

## See Also

- [object NSExtensionMappingsResponse](nsextensionmappingsresponse.md)
  A response from the device after it processes the command to get a list of the installed extensions for a user on a device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/nsextensionmappingscommand)*
# AccountConfigurationCommand

**Framework**: Device Management  
**Kind**: dictionary

The command to create and configure a local administrator account on a device.

**Availability**:
- macOS 10.11+
- Device Assignment Services ?+
- VPP License Management ?+

## Declaration

```swift
object AccountConfigurationCommand
```

## Topics

### Objects
- [object AccountConfigurationCommand.Command](accountconfigurationcommand/command-data.dictionary.md)
  The command to create and configure a local administrator account on a device.

## Properties

- `Command` (AccountConfigurationCommand.Command) *(required)*: The command dictionary.
- `CommandUUID` (string) *(required)*: The unique identifier of the command.

## See Also

- [object AccountConfigurationResponse](accountconfigurationresponse.md)
  A response from the device after it processes the command to create and configure a local administrator account on a device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/accountconfigurationcommand)*
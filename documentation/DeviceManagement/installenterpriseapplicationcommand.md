# InstallEnterpriseApplicationCommand

**Framework**: Device Management  
**Kind**: dictionary  
**Role**: Device Management Command

The command to install an enterprise app on a device.

**Availability**:
- macOS 10.13.6+

## Declaration

```
object InstallEnterpriseApplicationCommand
```

## Topics

### Objects
- [object InstallEnterpriseApplicationCommand.Command](./installenterpriseapplicationcommand/command-data.dictionary.md)
  The command to install an enterprise app on a device.

## Properties

- `Command` (InstallEnterpriseApplicationCommand.Command) *(required)*: The command dictionary.
- `CommandUUID` (string) *(required)*: The unique identifier of the command.

## See Also

### Commands and responses
- [object InstallEnterpriseApplicationResponse](./installenterpriseapplicationresponse.md)
  A response from the device after it processes the command to install an enterprise app on a device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/installenterpriseapplicationcommand)*
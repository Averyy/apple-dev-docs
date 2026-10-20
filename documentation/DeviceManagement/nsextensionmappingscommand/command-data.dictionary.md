# NSExtensionMappingsCommand.Command

**Framework**: Device Management  
**Kind**: dictionary  
**Role**: Device Management Command

The command to get a list of the installed extensions for a user on a device.

**Availability**:
- macOS 10.13+

## Declaration

```
object NSExtensionMappingsCommand.Command
```

## Properties

- `RequestRequiresNetworkTether` (boolean): If `true`, the device needs to be network-tethered to run the command.

  **Default**: `false`
- `RequestType` (string) *(required)*: The request type for this command.

  **Allowed Values**: `NSExtensionMappings`


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/nsextensionmappingscommand/command-data.dictionary)*
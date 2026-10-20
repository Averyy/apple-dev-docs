# ActiveNSExtensionsCommand.Command

**Framework**: Device Management  
**Kind**: dictionary  
**Role**: Device Management Command

The command to get a list of active extensions for a user on a device.

**Availability**:
- macOS 10.13+

## Declaration

```
object ActiveNSExtensionsCommand.Command
```

## Properties

- `FilterExtensionPoints` ([string]): An array of extension points. If you choose to provide this value, the response only includes the app extensions for the extension points you specify.
- `RequestRequiresNetworkTether` (boolean): If `true`, the device needs to be network-tethered to run the command.

  **Default**: `false`
- `RequestType` (string) *(required)*: The request type for this command.

  **Allowed Values**: `ActiveNSExtensions`


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/activensextensionscommand/command-data.dictionary)*
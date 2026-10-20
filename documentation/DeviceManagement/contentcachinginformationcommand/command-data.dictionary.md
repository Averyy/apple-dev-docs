# ContentCachingInformationCommand.Command

**Framework**: Device Management  
**Kind**: dictionary  
**Role**: Device Management Command

The command to get the status of the content caches on a device.

**Availability**:
- macOS 10.15.4+

## Declaration

```
object ContentCachingInformationCommand.Command
```

## Properties

- `RequestRequiresNetworkTether` (boolean): If `true`, the device needs to be network-tethered to run the command.

  **Default**: `false`
- `RequestType` (string) *(required)*: The request type for this command.

  **Allowed Values**: `ContentCachingInformation`


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/contentcachinginformationcommand/command-data.dictionary)*
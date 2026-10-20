# EnableRemoteDesktopCommand.Command

**Framework**: Device Management  
**Kind**: dictionary  
**Role**: Device Management Command

The command to enable Remote Desktop on a device.

**Availability**:
- macOS 10.14.4+

## Declaration

```
object EnableRemoteDesktopCommand.Command
```

## Properties

- `RequestRequiresNetworkTether` (boolean): If `true`, the device needs to be network-tethered to run the command.

  **Default**: `false`
- `RequestType` (string) *(required)*: The request type for this command.

  **Allowed Values**: `EnableRemoteDesktop`


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/enableremotedesktopcommand/command-data.dictionary)*
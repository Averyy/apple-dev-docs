# LOMSetupRequestCommand.Command

**Framework**: Device Management  
**Kind**: dictionary  
**Role**: Device Management Command

The command to get information from a device to set up lights-out management (LOM).

**Availability**:
- macOS 11.0+

## Declaration

```
object LOMSetupRequestCommand.Command
```

## Properties

- `RequestRequiresNetworkTether` (boolean): If `true`, the device needs to be network-tethered to run the command.

  **Default**: `false`
- `RequestType` (string) *(required)*: The request type for this command.

  **Allowed Values**: `LOMSetupRequest`


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/lomsetuprequestcommand/command-data.dictionary)*
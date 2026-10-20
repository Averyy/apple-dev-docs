# VerifyFirmwarePasswordCommand.Command

**Framework**: Device Management  
**Kind**: dictionary  
**Role**: Device Management Command

The command to verify the firmware password on a device.

**Availability**:
- macOS 10.13+

## Declaration

```
object VerifyFirmwarePasswordCommand.Command
```

## Properties

- `Password` (string) *(required)*: The password to verify.
- `RequestRequiresNetworkTether` (boolean): If `true`, the device needs to be network-tethered to run the command.

  **Default**: `false`
- `RequestType` (string) *(required)*: The request type for this command.

  **Allowed Values**: `VerifyFirmwarePassword`


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/verifyfirmwarepasswordcommand/command-data.dictionary)*
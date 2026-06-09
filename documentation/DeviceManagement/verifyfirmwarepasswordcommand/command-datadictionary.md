# VerifyFirmwarePasswordCommand.Command

**Framework**: Device Management  
**Kind**: dictionary

The command to verify the firmware password on a device.

**Availability**:
- macOS 10.13+

## Declaration

```swift
object VerifyFirmwarePasswordCommand.Command
```

## Properties

- `Password` (string) *(required)*: The password to verify.
- `RequestRequiresNetworkTether` (boolean): If `true`, the device needs to be network-tethered to run the command.
- `RequestType` (string) *(required)*: The request type for this command.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/verifyfirmwarepasswordcommand/command-data.dictionary)*
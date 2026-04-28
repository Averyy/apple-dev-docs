# SetFirmwarePasswordCommand.Command

**Framework**: Device Management  
**Kind**: dictionary

The command to change or clear the firmware password on a device.

**Availability**:
- macOS 10.13+
- Device Assignment Services ?+
- VPP License Management ?+

## Declaration

```swift
object SetFirmwarePasswordCommand.Command
```

## Properties

- `AllowOroms` (boolean): If `true`, enable ROMs.
- `CurrentPassword` (string): The current password, which you must set if the device has a firmware password.
- `NewPassword` (string) *(required)*: The new firmware password. Set to an empty string to clear the password. The characters in this value must consist of low-ASCII, printable characters (`0x20` through `0x7E`) to ensure that all characters are enterable on the EFI login screen.
- `RequestRequiresNetworkTether` (boolean): If `true`, the device needs to be network-tethered to run the command.
- `RequestType` (string) *(required)*: The request type for this command.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/setfirmwarepasswordcommand/command-data.dictionary)*
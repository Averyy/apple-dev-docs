# DisableRemoteDesktopCommand.Command

**Framework**: Device Management  
**Kind**: dictionary

The command to disable Remote Desktop on a device.

**Availability**:
- macOS 10.14.4+
- Device Assignment Services ?+
- VPP License Management ?+

## Declaration

```swift
object DisableRemoteDesktopCommand.Command
```

## Properties

- `RequestRequiresNetworkTether` (boolean): If `true`, the device needs to be network-tethered to run the command.
- `RequestType` (string) *(required)*: The request type for this command.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/disableremotedesktopcommand/command-data.dictionary)*
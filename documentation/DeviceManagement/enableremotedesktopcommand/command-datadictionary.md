# EnableRemoteDesktopCommand.Command

**Framework**: Device Management  
**Kind**: dictionary

The command to enable Remote Desktop on a device.

**Availability**:
- macOS 10.14.4+

## Declaration

```swift
object EnableRemoteDesktopCommand.Command
```

## Properties

- `RequestRequiresNetworkTether` (boolean): If `true`, the device needs to be network-tethered to run the command.
- `RequestType` (string) *(required)*: The request type for this command.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/enableremotedesktopcommand/command-data.dictionary)*
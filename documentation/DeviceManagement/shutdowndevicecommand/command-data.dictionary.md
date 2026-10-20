# ShutDownDeviceCommand.Command

**Framework**: Device Management  
**Kind**: dictionary  
**Role**: Device Management Command

The command to remotely and immediately shut down a device.

**Availability**:
- iOS 10.3+
- iPadOS 10.3+
- Mac Catalyst 10.3+
- macOS 10.13+

## Declaration

```
object ShutDownDeviceCommand.Command
```

## Properties

- `RequestRequiresNetworkTether` (boolean): If `true`, the device needs to be network-tethered to run the command.

  **Default**: `false`
- `RequestType` (string) *(required)*: The request type for this command.

  **Allowed Values**: `ShutDownDevice`


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/shutdowndevicecommand/command-data.dictionary)*
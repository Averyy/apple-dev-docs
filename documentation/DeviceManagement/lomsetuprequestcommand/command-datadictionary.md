# LOMSetupRequestCommand.Command

**Framework**: Device Management  
**Kind**: dictionary

The command to get information from a device to set up lights-out management (LOM).

**Availability**:
- macOS 11.0+
- Device Assignment Services ?+
- VPP License Management ?+

## Declaration

```swift
object LOMSetupRequestCommand.Command
```

## Properties

- `RequestRequiresNetworkTether` (boolean): If `true`, the device needs to be network-tethered to run the command.
- `RequestType` (string) *(required)*: The request type for this command.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/lomsetuprequestcommand/command-data.dictionary)*
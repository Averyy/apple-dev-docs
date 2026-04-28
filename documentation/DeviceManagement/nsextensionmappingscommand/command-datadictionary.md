# NSExtensionMappingsCommand.Command

**Framework**: Device Management  
**Kind**: dictionary

The command to get a list of the installed extensions for a user on a device.

**Availability**:
- macOS 10.13+
- Device Assignment Services ?+
- VPP License Management ?+

## Declaration

```swift
object NSExtensionMappingsCommand.Command
```

## Properties

- `RequestRequiresNetworkTether` (boolean): If `true`, the device needs to be network-tethered to run the command.
- `RequestType` (string) *(required)*: The request type for this command.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/nsextensionmappingscommand/command-data.dictionary)*
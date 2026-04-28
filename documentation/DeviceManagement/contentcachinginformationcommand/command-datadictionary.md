# ContentCachingInformationCommand.Command

**Framework**: Device Management  
**Kind**: dictionary

The command to get the status of the content caches on a device.

**Availability**:
- macOS 10.15.4+
- Device Assignment Services ?+
- VPP License Management ?+

## Declaration

```swift
object ContentCachingInformationCommand.Command
```

## Properties

- `RequestRequiresNetworkTether` (boolean): If `true`, the device needs to be network-tethered to run the command.
- `RequestType` (string) *(required)*: The request type for this command.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/contentcachinginformationcommand/command-data.dictionary)*
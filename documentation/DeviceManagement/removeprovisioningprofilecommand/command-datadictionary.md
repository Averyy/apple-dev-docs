# RemoveProvisioningProfileCommand.Command

**Framework**: Device Management  
**Kind**: dictionary

The command to remove a previously installed provisioning profile from a device.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- macOS 11.0+
- tvOS 10.2+
- visionOS 1.1+
- watchOS 10.0+

## Declaration

```swift
object RemoveProvisioningProfileCommand.Command
```

## Properties

- `RequestRequiresNetworkTether` (boolean): If `true`, the device needs to be network-tethered to run the command.
- `RequestType` (string) *(required)*: The request type for this command.
- `UUID` (string) *(required)*: The unique identifier of the provisioning profile to remove.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/removeprovisioningprofilecommand/command-data.dictionary)*
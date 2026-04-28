# InstallProvisioningProfileCommand.Command

**Framework**: Device Management  
**Kind**: dictionary

The command to install a provisioning profile on a device.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 4.0+
- macOS 11.0+
- tvOS 10.2+
- visionOS 1.1+
- watchOS 10.0+
- Device Assignment Services ?+
- VPP License Management ?+

## Declaration

```swift
object InstallProvisioningProfileCommand.Command
```

## Properties

- `ProvisioningProfile` (data) *(required)*: The provisioning profile.
- `RequestRequiresNetworkTether` (boolean): If `true`, the device needs to be network-tethered to run the command.
- `RequestType` (string) *(required)*: The request type for this command.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/installprovisioningprofilecommand/command-data.dictionary)*
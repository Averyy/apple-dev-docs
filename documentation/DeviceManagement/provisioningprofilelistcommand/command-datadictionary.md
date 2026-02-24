# ProvisioningProfileListCommand.Command

**Framework**: Device Management  
**Kind**: dictionary

The command to get a list of installed provisioning profiles on a device.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- macOS 11.0+
- tvOS 10.2+
- visionOS 1.1+
- watchOS 10.0+

## Declaration

```swift
object ProvisioningProfileListCommand.Command
```

## Properties

- `ManagedOnly` (boolean): If `true`, only include profiles that MDM has installed. For user enrollments, the device ignores this key and always limits the results to managed profiles. This value is available in iOS 13 and later, and tvOS 13 and later.
- `RequestRequiresNetworkTether` (boolean): If `true`, the device needs to be network-tethered to run the command.
- `RequestType` (string) *(required)*: The request type for this command.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/provisioningprofilelistcommand/command-data.dictionary)*
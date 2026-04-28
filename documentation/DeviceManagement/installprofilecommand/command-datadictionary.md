# InstallProfileCommand.Command

**Framework**: Device Management  
**Kind**: dictionary

The command to install a configuration profile on a device.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 4.0+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.1+
- watchOS 10.0+
- Device Assignment Services ?+
- VPP License Management ?+

## Declaration

```swift
object InstallProfileCommand.Command
```

## Properties

- `Payload` (data) *(required)*: The profile to install, which you can encrypt using any identity certificate installed on the device. You can also sign the profile.
- `RequestRequiresNetworkTether` (boolean): If `true`, the device needs to be network-tethered to run the command.
- `RequestType` (string) *(required)*: The request type for this command.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/installprofilecommand/command-data.dictionary)*
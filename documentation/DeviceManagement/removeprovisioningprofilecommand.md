# RemoveProvisioningProfileCommand

**Framework**: Device Management  
**Kind**: dictionary

The command to remove a previously installed provisioning profile from a device.

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
object RemoveProvisioningProfileCommand
```

## Topics

### Objects
- [object RemoveProvisioningProfileCommand.Command](removeprovisioningprofilecommand/command-data.dictionary.md)
  The command to remove a previously installed provisioning profile from a device.

## Properties

- `Command` (RemoveProvisioningProfileCommand.Command) *(required)*: The command dictionary.
- `CommandUUID` (string) *(required)*: The unique identifier of the command.

## See Also

- [object RemoveProvisioningProfileResponse](removeprovisioningprofileresponse.md)
  A response from the device after it processes the command to remove a previously installed provisioning profile from a device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/removeprovisioningprofilecommand)*
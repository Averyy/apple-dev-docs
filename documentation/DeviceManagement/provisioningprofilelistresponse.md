# ProvisioningProfileListResponse

**Framework**: Device Management  
**Kind**: dictionary

A response from the device after it processes the command to get a list of its provisioning profiles.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- macOS 11.0+
- tvOS 10.2+
- visionOS 1.1+
- watchOS 10.0+
- Device Assignment Services ?+
- VPP License Management ?+

## Declaration

```swift
object ProvisioningProfileListResponse
```

## Topics

### Commands
- [object ProvisioningProfileListResponse.ProvisioningProfileListItem](provisioningprofilelistresponse/provisioningprofilelistitem.md)
  A dictionary that describes a provisioning profile list item.
- [object ProvisioningProfileListResponse.ErrorChainItem](provisioningprofilelistresponse/errorchainitem.md)
  A dictionary that describes an error chain item.

## See Also

- [object ProvisioningProfileListCommand](provisioningprofilelistcommand.md)
  The command to get a list of installed provisioning profiles on a device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/provisioningprofilelistresponse)*
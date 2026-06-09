# ProvisioningProfileListResponse.ProvisioningProfileListItem

**Framework**: Device Management  
**Kind**: dictionary

A dictionary that describes a provisioning profile list item.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 4.0+
- macOS 11.0+
- tvOS 10.2+
- visionOS 1.1+
- watchOS 10.0+

## Declaration

```swift
object ProvisioningProfileListResponse.ProvisioningProfileListItem
```

## Properties

- `ExpiryDate` (date): The expiry date of the provisioning profile.
- `Name` (string) *(required)*: The display name of the provisioning profile.
- `UUID` (string) *(required)*: The unique identifier for the provisioning profile.

## See Also

- [object ProvisioningProfileListResponse.ErrorChainItem](provisioningprofilelistresponse/errorchainitem.md)
  A dictionary that describes an error chain item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/provisioningprofilelistresponse/provisioningprofilelistitem)*
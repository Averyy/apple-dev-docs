# ProvisioningProfileListResponse.ErrorChainItem

**Framework**: Device Management  
**Kind**: dictionary

A dictionary that describes an error chain item.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- macOS 11.0+
- tvOS 10.2+
- visionOS 1.1+
- watchOS 10.0+

## Declaration

```swift
object ProvisioningProfileListResponse.ErrorChainItem
```

## Properties

- `ErrorCode` (integer) *(required)*: The error code.
- `ErrorDomain` (string) *(required)*: The error domain.
- `LocalizedDescription` (string) *(required)*: A description of the error in the device’s localized language.
- `USEnglishDescription` (string): A description of the error in U.S. English.

## See Also

- [object ProvisioningProfileListResponse.ProvisioningProfileListItem](provisioningprofilelistresponse/provisioningprofilelistitem.md)
  A dictionary that describes a provisioning profile list item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/provisioningprofilelistresponse/errorchainitem)*
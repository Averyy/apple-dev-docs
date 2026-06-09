# ManagedApplicationListResponse.ErrorChainItem

**Framework**: Device Management  
**Kind**: dictionary

A dictionary that describes an error chain item.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 5.0+
- macOS 11.0+
- tvOS 10.2+
- visionOS 1.1+
- watchOS 10.0+

## Declaration

```swift
object ManagedApplicationListResponse.ErrorChainItem
```

## Properties

- `ErrorCode` (integer) *(required)*: The error code.
- `ErrorDomain` (string) *(required)*: The error domain.
- `LocalizedDescription` (string) *(required)*: A description of the error in the device’s localized language.
- `USEnglishDescription` (string): A description of the error in U.S. English.

## See Also

- [object ManagedApplicationListResponse.ManagedApplicationList](managedapplicationlistresponse/managedapplicationlist-data.dictionary.md)
  A dictionary that contains status information about managed apps.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/managedapplicationlistresponse/errorchainitem)*
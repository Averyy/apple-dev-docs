# ManagedApplicationAttributesResponse.ErrorChainItem

**Framework**: Device Management  
**Kind**: dictionary

A dictionary that describes an error chain item.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 7.0+
- tvOS 10.2+
- visionOS 1.1+
- watchOS 10.0+

## Declaration

```swift
object ManagedApplicationAttributesResponse.ErrorChainItem
```

## Properties

- `ErrorCode` (integer) *(required)*: The error code.
- `ErrorDomain` (string) *(required)*: The error domain.
- `LocalizedDescription` (string) *(required)*: A description of the error in the device’s localized language.
- `USEnglishDescription` (string): A description of the error in U.S. English.

## See Also

- [object ManagedApplicationAttributesResponse.ApplicationAttributesItem](managedapplicationattributesresponse/applicationattributesitem.md)
  A dictionary that contains a managed app attributes item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/managedapplicationattributesresponse/errorchainitem)*
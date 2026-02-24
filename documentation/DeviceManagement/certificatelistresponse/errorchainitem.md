# CertificateListResponse.ErrorChainItem

**Framework**: Device Management  
**Kind**: dictionary

A dictionary that describes an error chain item.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.1+
- watchOS 10.0+

## Declaration

```swift
object CertificateListResponse.ErrorChainItem
```

## Properties

- `ErrorCode` (integer) *(required)*: The error code.
- `ErrorDomain` (string) *(required)*: The error domain.
- `LocalizedDescription` (string) *(required)*: A description of the error in the device’s localized language.
- `USEnglishDescription` (string): A description of the error in U.S. English.

## See Also

- [object CertificateListResponse.CertificateListItem](certificatelistresponse/certificatelistitem.md)
  A dictionary that contains information about a certificate list item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/certificatelistresponse/errorchainitem)*
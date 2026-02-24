# ManagedMediaListResponse.ErrorChainItem

**Framework**: Device Management  
**Kind**: dictionary

A dictionary that describes an error chain item.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+

## Declaration

```swift
object ManagedMediaListResponse.ErrorChainItem
```

## Properties

- `ErrorCode` (integer) *(required)*: The error code.
- `ErrorDomain` (string) *(required)*: The error domain.
- `LocalizedDescription` (string) *(required)*: A description of the error in the device’s localized language.
- `USEnglishDescription` (string): A description of the error in U.S. English.

## See Also

- [object ManagedMediaListResponse.BooksItem](managedmedialistresponse/booksitem.md)
  A dictionary that describes a managed book.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/managedmedialistresponse/errorchainitem)*
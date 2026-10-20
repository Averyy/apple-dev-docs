# Representation

**Framework**: Core Transferable  
**Kind**: associatedtype  
**Role**: Associated Type  
**Required**: Yes

The type of the representation used to import and export the item.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
associatedtype Representation : TransferRepresentation
```

#### Discussion

Swift infers this type from the return value of the [`transferRepresentation`](./transferrepresentation.md) property.

## See Also

### Implementing a transfer representation
- [static var transferRepresentation: Self.Representation](./transferrepresentation.md)
  The representation used to import and export the item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretransferable/transferable/representation)*
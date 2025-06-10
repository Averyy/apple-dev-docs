# CollectionDifference.Change

**Framework**: Swift  
**Kind**: enum

A single change to a collection.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
@frozen
enum Change
```

## Topics

### Enumeration Cases
- [case insert(offset: Int, element: ChangeElement, associatedWith: Int?)](collectiondifference/change/insert(offset:element:associatedwith:).md)
  An insertion.
- [case remove(offset: Int, element: ChangeElement, associatedWith: Int?)](collectiondifference/change/remove(offset:element:associatedwith:).md)
  A removal.
### Default Implementations
- [Decodable Implementations](collectiondifference/change/decodable-implementations.md)
- [Encodable Implementations](collectiondifference/change/encodable-implementations.md)
- [Equatable Implementations](collectiondifference/change/equatable-implementations.md)
- [Hashable Implementations](collectiondifference/change/hashable-implementations.md)

## Relationships

### Conforms To
- [Copyable](copyable.md)
- [Decodable](decodable.md)
- [Encodable](encodable.md)
- [Equatable](equatable.md)
- [Hashable](hashable.md)
- [Sendable](sendable.md)
- [SendableMetatype](sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/collectiondifference/change)*
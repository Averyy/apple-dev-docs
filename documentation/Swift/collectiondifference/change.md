# CollectionDifference.Change

**Framework**: Swift  
**Kind**: enum  
**Role**: Enumeration

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
- [case insert(offset: Int, element: ChangeElement, associatedWith: Int?)](./change/insert%28offset,element,associatedwith%29.md)
  An insertion.
- [case remove(offset: Int, element: ChangeElement, associatedWith: Int?)](./change/remove%28offset,element,associatedwith%29.md)
  A removal.
### Default Implementations
- [Decodable Implementations](./change/decodable-implementations.md)
- [Encodable Implementations](./change/encodable-implementations.md)
- [Equatable Implementations](./change/equatable-implementations.md)
- [Hashable Implementations](./change/hashable-implementations.md)

## Relationships

### Conforms To
- [Copyable](../copyable.md)
- [Decodable](../decodable.md)
- [Encodable](../encodable.md)
- [Equatable](../equatable.md)
- [Escapable](../escapable.md)
- [Hashable](../hashable.md)
- [Sendable](../sendable.md)
- [SendableMetatype](../sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/collectiondifference/change)*
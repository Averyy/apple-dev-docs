# ReversedCollection.Index

**Framework**: Swift  
**Kind**: struct

An index that traverses the same positions as an underlying index, with inverted traversal direction.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.0+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
@frozen
struct Index
```

## Topics

### Initializers
- [init(Base.Index)](reversedcollection/index/init(_:).md)
  Creates a new index into a reversed collection for the position before the specified index.
### Instance Properties
- [let base: Base.Index](reversedcollection/index/base.md)
  The position after this position in the underlying collection.
### Default Implementations
- [Comparable Implementations](reversedcollection/index/comparable-implementations.md)
- [Equatable Implementations](reversedcollection/index/equatable-implementations.md)
- [Hashable Implementations](reversedcollection/index/hashable-implementations.md)

## Relationships

### Conforms To
- [Comparable](comparable.md)
- [Copyable](copyable.md)
- [Equatable](equatable.md)
- [Hashable](hashable.md)
- [Sendable](sendable.md)
- [SendableMetatype](sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/reversedcollection/index)*
# HistoryTombstone

**Framework**: SwiftData  
**Kind**: struct

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+
- Swift 5.9+

## Declaration

```swift
struct HistoryTombstone<Model> where Model : PersistentModel
```

## Topics

### Structures
- [HistoryTombstone.Iterator](historytombstone/iterator.md)
  A type that provides the sequence’s iteration interface and encapsulates its iteration state.
### Instance Methods
- [func makeIterator() -> HistoryTombstone<Model>.Iterator](historytombstone/makeiterator.md)
  Returns an iterator over the elements of this sequence.
### Subscripts
- [subscript(PartialKeyPath<Model>) -> (any Sendable)?](historytombstone/subscript(_:).md)
### Type Aliases
- [HistoryTombstone.Element](historytombstone/element.md)
  A type representing the sequence’s elements.
### Default Implementations
- [Sequence Implementations](historytombstone/sequence-implementations.md)

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [Sequence](../Swift/Sequence.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftdata/historytombstone)*
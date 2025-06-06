# AnyIterator

**Framework**: Swift  
**Kind**: struct

A type-erased iterator of `Element`.

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
struct AnyIterator<Element>
```

#### Overview

This iterator forwards its `next()` method to an arbitrary underlying iterator having the same `Element` type, hiding the specifics of the underlying `IteratorProtocol`.

## Topics

### Initializers
- [init<I>(I)](anyiterator/init(_:)-3m1u6.md)
  Creates an iterator that wraps a base iterator but whose type depends only on the base iterator’s element type.
- [init(() -> Element?)](anyiterator/init(_:)-5l6js.md)
  Creates an iterator that wraps the given closure in its `next()` method.
### Default Implementations
- [IteratorProtocol Implementations](anyiterator/iteratorprotocol-implementations.md)
- [Sequence Implementations](anyiterator/sequence-implementations.md)

## Relationships

### Conforms To
- [Copyable](copyable.md)
- [IteratorProtocol](iteratorprotocol.md)
- [Sequence](sequence.md)

## See Also

- [struct AnySequence](anysequence.md)
  A type-erased sequence.
- [struct AnyCollection](anycollection.md)
  A type-erased wrapper over any collection with indices that support forward traversal.
- [struct AnyBidirectionalCollection](anybidirectionalcollection.md)
  A type-erased wrapper over any collection with indices that support bidirectional traversal.
- [struct AnyRandomAccessCollection](anyrandomaccesscollection.md)
  A type-erased wrapper over any collection with indices that support random access traversal.
- [struct AnyIndex](anyindex.md)
  A wrapper over an underlying index that hides the specific underlying type.
- [struct AnyHashable](anyhashable.md)
  A type-erased hashable value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/anyiterator)*
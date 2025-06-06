# IteratorSequence

**Framework**: Swift  
**Kind**: struct

A sequence built around an iterator of type `Base`.

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
struct IteratorSequence<Base> where Base : IteratorProtocol
```

#### Overview

Useful mostly to recover the ability to use `for`…`in`, given just an iterator `i`:

```swift
for x in IteratorSequence(i) { ... }
```

## Topics

### Initializers
- [init(Base)](iteratorsequence/init(_:).md)
  Creates an instance whose iterator is a copy of `base`.
### Default Implementations
- [IteratorProtocol Implementations](iteratorsequence/iteratorprotocol-implementations.md)
- [Sequence Implementations](iteratorsequence/sequence-implementations.md)

## Relationships

### Conforms To
- [Copyable](copyable.md)
- [IteratorProtocol](iteratorprotocol.md)
- [Sendable](sendable.md)
- [Sequence](sequence.md)

## See Also

- [struct IndexingIterator](indexingiterator.md)
  A type that iterates over a collection using its indices.
- [typealias EnumeratedIterator](enumeratediterator.md)
- [typealias SetIterator](setiterator.md)
- [struct StrideThroughIterator](stridethroughiterator.md)
  An iterator for a `StrideThrough` instance.
- [struct StrideToIterator](stridetoiterator.md)
  An iterator for a `StrideTo` instance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/iteratorsequence)*
# StrideToIterator

**Framework**: Swift  
**Kind**: struct

An iterator for a `StrideTo` instance.

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
struct StrideToIterator<Element> where Element : Strideable
```

## Topics

### Default Implementations
- [IteratorProtocol Implementations](stridetoiterator/iteratorprotocol-implementations.md)

## Relationships

### Conforms To
- [Copyable](copyable.md)
- [IteratorProtocol](iteratorprotocol.md)
- [Sendable](sendable.md)
- [SendableMetatype](sendablemetatype.md)

## See Also

- [struct IteratorSequence](iteratorsequence.md)
  A sequence built around an iterator of type `Base`.
- [struct IndexingIterator](indexingiterator.md)
  A type that iterates over a collection using its indices.
- [typealias EnumeratedIterator](enumeratediterator.md)
- [typealias SetIterator](setiterator.md)
- [struct StrideThroughIterator](stridethroughiterator.md)
  An iterator for a `StrideThrough` instance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/stridetoiterator)*
# EnumeratedIterator

**Framework**: Swift  
**Kind**: typealias  
**Role**: Type Alias

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.0+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+
- Swift - Deprecated in 4.2 (renamed: EnumeratedSequence.Iterator)

## Declaration

```swift
typealias EnumeratedIterator<T> = EnumeratedSequence<T>.Iterator where T : Sequence
```

## See Also

### Indices and Iterators
- [struct IteratorSequence](./iteratorsequence.md)
  A sequence built around an iterator of type `Base`.
- [struct IndexingIterator](./indexingiterator.md)
  A type that iterates over a collection using its indices.
- [typealias SetIterator](./setiterator.md)
- [struct StrideThroughIterator](./stridethroughiterator.md)
  An iterator for a `StrideThrough` instance.
- [struct StrideToIterator](./stridetoiterator.md)
  An iterator for a `StrideTo` instance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/enumeratediterator)*
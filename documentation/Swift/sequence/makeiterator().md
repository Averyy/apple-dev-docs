# makeIterator()

**Framework**: Swift  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Returns an iterator over the elements of this sequence.

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
func makeIterator() -> Self.Iterator
```

## Default Implementations

### Sequence Implementations
- [func makeIterator() -> IndexingIterator<Self>](./makeiterator%28%29-85cyw.md)
  Returns an iterator over the elements of the collection.
- [func makeIterator() -> Self](./makeiterator%28%29-9859q.md)
  Returns an iterator over the elements of this sequence.

## See Also

### Creating an Iterator
- [associatedtype Iterator : IteratorProtocol](./iterator.md)
  A type that provides the sequence’s iteration interface and encapsulates its iteration state.
- [associatedtype Element](./element.md)
  A type representing the sequence’s elements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/sequence/makeiterator())*
# Iterator

**Framework**: Swift  
**Kind**: associatedtype  
**Required**: Yes

A type that provides the sequence’s iteration interface and encapsulates its iteration state.

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
associatedtype Iterator : IteratorProtocol
```

## See Also

- [func makeIterator() -> Self.Iterator](sequence/makeiterator.md)
  Returns an iterator over the elements of this sequence.
- [associatedtype Element](sequence/element.md)
  A type representing the sequence’s elements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/sequence/iterator)*
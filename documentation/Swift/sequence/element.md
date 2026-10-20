# Element

**Framework**: Swift  
**Kind**: associatedtype  
**Role**: Associated Type  
**Required**: Yes

A type representing the sequence’s elements.

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
associatedtype Element where Self.Element == Self.Iterator.Element
```

## See Also

### Creating an Iterator
- [func makeIterator() -> Self.Iterator](./makeiterator%28%29.md)
  Returns an iterator over the elements of this sequence.
- [associatedtype Iterator : IteratorProtocol](./iterator.md)
  A type that provides the sequence’s iteration interface and encapsulates its iteration state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/sequence/element)*
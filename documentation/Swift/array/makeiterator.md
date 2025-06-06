# makeIterator()

**Framework**: Swift  
**Kind**: method

Returns an iterator over the elements of the collection.

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
func makeIterator() -> IndexingIterator<Self>
```

## See Also

- [func forEach((Self.Element) throws -> Void) rethrows](array/foreach(_:).md)
  Calls the given closure on each element in the sequence in the same order as a `for`-`in` loop.
- [func enumerated() -> EnumeratedSequence<Self>](array/enumerated.md)
  Returns a sequence of pairs (, ), where  represents a consecutive integer starting at zero and  represents an element of the sequence.
- [var underestimatedCount: Int](array/underestimatedcount.md)
  A value less than or equal to the number of elements in the collection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/array/makeiterator())*
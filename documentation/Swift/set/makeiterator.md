# makeIterator()

**Framework**: Swift  
**Kind**: method

Returns an iterator over the members of the set.

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
func makeIterator() -> Set<Element>.Iterator
```

## See Also

- [func enumerated() -> EnumeratedSequence<Self>](set/enumerated.md)
  Returns a sequence of pairs (, ), where  represents a consecutive integer starting at zero and  represents an element of the sequence.
- [func forEach((Self.Element) throws -> Void) rethrows](set/foreach(_:).md)
  Calls the given closure on each element in the sequence in the same order as a `for`-`in` loop.
- [var underestimatedCount: Int](set/underestimatedcount.md)
  A value less than or equal to the number of elements in the collection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/set/makeiterator())*
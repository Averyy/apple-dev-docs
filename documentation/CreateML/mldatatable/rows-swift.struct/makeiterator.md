# makeIterator()

**Framework**: Create ML  
**Kind**: method

Returns an iterator over the elements of the collection.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 10.14+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
func makeIterator() -> IndexingIterator<Self>
```

## See Also

- [func forEach((Self.Element) throws -> Void) rethrows](mldatatable/rows-swift.struct/foreach(_:).md)
  Calls the given closure on each element in the sequence in the same order as a `for`-`in` loop.
- [func enumerated() -> EnumeratedSequence<Self>](mldatatable/rows-swift.struct/enumerated.md)
  Returns a sequence of pairs (, ), where  represents a consecutive integer starting at zero and  represents an element of the sequence.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mldatatable/rows-swift.struct/makeiterator())*
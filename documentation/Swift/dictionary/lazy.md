# lazy

**Framework**: Swift  
**Kind**: property

A sequence containing the same elements as this sequence, but on which some operations, such as `map` and `filter`, are implemented lazily.

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
var lazy: LazySequence<Self> { get }
```

## See Also

- [func forEach((Self.Element) throws -> Void) rethrows](dictionary/foreach(_:).md)
  Calls the given closure on each element in the sequence in the same order as a `for`-`in` loop.
- [func enumerated() -> EnumeratedSequence<Self>](dictionary/enumerated.md)
  Returns a sequence of pairs (, ), where  represents a consecutive integer starting at zero and  represents an element of the sequence.
- [func makeIterator() -> Dictionary<Key, Value>.Iterator](dictionary/makeiterator.md)
  Returns an iterator over the dictionary’s key-value pairs.
- [var underestimatedCount: Int](dictionary/underestimatedcount.md)
  A value less than or equal to the number of elements in the collection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/dictionary/lazy)*
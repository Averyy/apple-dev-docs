# underestimatedCount

**Framework**: Swift  
**Kind**: property

A value less than or equal to the number of elements in the collection.

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
var underestimatedCount: Int { get }
```

#### Discussion

> **Note**: O(1) if the collection conforms to `RandomAccessCollection`; otherwise, O(), where  is the length of the collection.

O(1) if the collection conforms to `RandomAccessCollection`; otherwise, O(), where  is the length of the collection.

## See Also

- [func forEach((Self.Element) throws -> Void) rethrows](dictionary/foreach(_:).md)
  Calls the given closure on each element in the sequence in the same order as a `for`-`in` loop.
- [func enumerated() -> EnumeratedSequence<Self>](dictionary/enumerated.md)
  Returns a sequence of pairs (, ), where  represents a consecutive integer starting at zero and  represents an element of the sequence.
- [var lazy: LazySequence<Self>](dictionary/lazy.md)
  A sequence containing the same elements as this sequence, but on which some operations, such as `map` and `filter`, are implemented lazily.
- [func makeIterator() -> Dictionary<Key, Value>.Iterator](dictionary/makeiterator.md)
  Returns an iterator over the dictionary’s key-value pairs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/dictionary/underestimatedcount)*
# underestimatedCount

**Framework**: Swift  
**Kind**: property  
**Role**: Instance Property

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

> **Complexity**: O(1) if the collection conforms to `RandomAccessCollection`; otherwise, O(*n*), where *n* is the length of the collection.

## See Also

### Iterating over a Set
- [func enumerated() -> EnumeratedSequence<Self>](./enumerated%28%29.md)
  Returns a sequence of pairs (*n*, *x*), where *n* represents a consecutive integer starting at zero and *x* represents an element of the sequence.
- [func forEach((Self.Element) throws -> Void) rethrows](./foreach%28_%29.md)
  Calls the given closure on each element in the sequence in the same order as a `for`-`in` loop.
- [func makeIterator() -> Set<Element>.Iterator](./makeiterator%28%29.md)
  Returns an iterator over the members of the set.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/set/underestimatedcount)*
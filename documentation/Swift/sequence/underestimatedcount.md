# underestimatedCount

**Framework**: Swift  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

A value less than or equal to the number of elements in the sequence, calculated nondestructively.

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

## Discussion

The default implementation returns 0. If you provide your own implementation, make sure to compute the value nondestructively.

> **Complexity**: O(1), except if the sequence also conforms to `Collection`. In this case, see the documentation of `Collection.underestimatedCount`.

## Default Implementations

### Sequence Implementations
- [var underestimatedCount: Int](./underestimatedcount-3n9ne.md)
  A value less than or equal to the number of elements in the collection.
- [var underestimatedCount: Int](./underestimatedcount-7sn1i.md)
- [var underestimatedCount: Int](./underestimatedcount-7vi5w.md)
- [var underestimatedCount: Int](./underestimatedcount-9oyup.md)
  A value less than or equal to the number of elements in the sequence, calculated nondestructively.

## See Also

### Iterating Over a Sequence’s Elements
- [func forEach((Self.Element) throws -> Void) rethrows](./foreach%28_%29.md)
  Calls the given closure on each element in the sequence in the same order as a `for`-`in` loop.
- [func enumerated() -> EnumeratedSequence<Self>](./enumerated%28%29.md)
  Returns a sequence of pairs (*n*, *x*), where *n* represents a consecutive integer starting at zero and *x* represents an element of the sequence.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/sequence/underestimatedcount)*
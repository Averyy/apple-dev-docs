# underestimatedCount

**Framework**: RealityKit  
**Kind**: property

A value less than or equal to the number of elements in the sequence, calculated nondestructively.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- visionOS ?+

## Declaration

```swift
var underestimatedCount: Int { get }
```

#### Discussion

The default implementation returns 0. If you provide your own implementation, make sure to compute the value nondestructively.

> **Note**: O(1), except if the sequence also conforms to `Collection`. In this case, see the documentation of `Collection.underestimatedCount`.

O(1), except if the sequence also conforms to `Collection`. In this case, see the documentation of `Collection.underestimatedCount`.

## See Also

- [func forEach((Self.Element) throws -> Void) rethrows](queryresult/foreach(_:).md)
  Calls the given closure on each element in the sequence in the same order as a `for`-`in` loop.
- [func enumerated() -> EnumeratedSequence<Self>](queryresult/enumerated.md)
  Returns a sequence of pairs (, ), where  represents a consecutive integer starting at zero and  represents an element of the sequence.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/queryresult/underestimatedcount)*
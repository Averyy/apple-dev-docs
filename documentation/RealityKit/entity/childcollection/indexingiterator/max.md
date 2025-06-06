# max()

**Framework**: RealityKit  
**Kind**: method

Returns the maximum element in the sequence.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- visionOS ?+

## Declaration

```swift
@warn_unqualified_access
func max() -> Self.Element?
```

#### Return Value

The sequence’s maximum element. If the sequence has no elements, returns `nil`.

#### Discussion

This example finds the largest value in an array of height measurements.

```None
let heights = [67.5, 65.7, 64.3, 61.1, 58.5, 60.3, 64.9]
let greatestHeight = heights.max()
print(greatestHeight)
// Prints "Optional(67.5)"
```

> **Note**: O(), where  is the length of the sequence.

O(), where  is the length of the sequence.

## See Also

- [func contains(Self.Element) -> Bool](entity/childcollection/indexingiterator/contains(_:).md)
  Returns a Boolean value indicating whether the sequence contains the given element.
- [func contains(where: (Self.Element) throws -> Bool) rethrows -> Bool](entity/childcollection/indexingiterator/contains(where:).md)
  Returns a Boolean value indicating whether the sequence contains an element that satisfies the given predicate.
- [func allSatisfy((Self.Element) throws -> Bool) rethrows -> Bool](entity/childcollection/indexingiterator/allsatisfy(_:).md)
  Returns a Boolean value indicating whether every element of a sequence satisfies a given predicate.
- [func first(where: (Self.Element) throws -> Bool) rethrows -> Self.Element?](entity/childcollection/indexingiterator/first(where:).md)
  Returns the first element of the sequence that satisfies the given predicate.
- [func max(by: (Self.Element, Self.Element) throws -> Bool) rethrows -> Self.Element?](entity/childcollection/indexingiterator/max(by:).md)
  Returns the maximum element in the sequence, using the given predicate as the comparison between elements.
- [func min() -> Self.Element?](entity/childcollection/indexingiterator/min.md)
  Returns the minimum element in the sequence.
- [func min(by: (Self.Element, Self.Element) throws -> Bool) rethrows -> Self.Element?](entity/childcollection/indexingiterator/min(by:).md)
  Returns the minimum element in the sequence, using the given predicate as the comparison between elements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/entity/childcollection/indexingiterator/max())*
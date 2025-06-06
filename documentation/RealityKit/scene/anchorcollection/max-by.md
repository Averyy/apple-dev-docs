# max(by:)

**Framework**: RealityKit  
**Kind**: method

Returns the maximum element in the sequence, using the given predicate as the comparison between elements.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- visionOS ?+

## Declaration

```swift
@warn_unqualified_access
func max(by areInIncreasingOrder: (Self.Element, Self.Element) throws -> Bool) rethrows -> Self.Element?
```

#### Return Value

The sequence’s maximum element if the sequence is not empty; otherwise, `nil`.

#### Discussion

The predicate must be a  over the elements. That is, for any elements `a`, `b`, and `c`, the following conditions must hold:

- `areInIncreasingOrder(a, a)` is always `false`. (Irreflexivity)
- If `areInIncreasingOrder(a, b)` and `areInIncreasingOrder(b, c)` are both `true`, then `areInIncreasingOrder(a, c)` is also `true`. (Transitive comparability)
- Two elements are  if neither is ordered before the other according to the predicate. If `a` and `b` are incomparable, and `b` and `c` are incomparable, then `a` and `c` are also incomparable. (Transitive incomparability)

This example shows how to use the `max(by:)` method on a dictionary to find the key-value pair with the highest value.

```None
let hues = ["Heliotrope": 296, "Coral": 16, "Aquamarine": 156]
let greatestHue = hues.max { a, b in a.value < b.value }
print(greatestHue)
// Prints "Optional((key: "Heliotrope", value: 296))"
```

> **Note**: O(), where  is the length of the sequence.

O(), where  is the length of the sequence.

## Parameters

- `areInIncreasingOrder`: A predicate that returns   if its   first argument should be ordered before its second argument;   otherwise,  .

## See Also

- [func contains(where: (Self.Element) throws -> Bool) rethrows -> Bool](scene/anchorcollection/contains(where:).md)
  Returns a Boolean value indicating whether the sequence contains an element that satisfies the given predicate.
- [func allSatisfy((Self.Element) throws -> Bool) rethrows -> Bool](scene/anchorcollection/allsatisfy(_:).md)
  Returns a Boolean value indicating whether every element of a sequence satisfies a given predicate.
- [var first: Self.Element?](scene/anchorcollection/first.md)
  The first element of the collection.
- [func first(where: (Self.Element) throws -> Bool) rethrows -> Self.Element?](scene/anchorcollection/first(where:).md)
  Returns the first element of the sequence that satisfies the given predicate.
- [func min(by: (Self.Element, Self.Element) throws -> Bool) rethrows -> Self.Element?](scene/anchorcollection/min(by:).md)
  Returns the minimum element in the sequence, using the given predicate as the comparison between elements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/scene/anchorcollection/max(by:))*
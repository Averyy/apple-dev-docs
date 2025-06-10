# max(by:)

**Framework**: Foundation  
**Kind**: method

Returns the maximum element in the sequence, using the given predicate as the comparison between elements.

**Availability**:
- Mac Catalyst 13.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

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

## Parameters

- `areInIncreasingOrder`: A predicate that returns   if its   first argument should be ordered before its second argument;   otherwise,  .

## See Also

- [func first(where: (Self.Element) throws -> Bool) rethrows -> Self.Element?](data/first(where:).md)
  Returns the first element of the sequence that satisfies the given predicate.
- [func max() -> Self.Element?](data/max.md)
  Returns the maximum element in the sequence.
- [func min() -> Self.Element?](data/min.md)
  Returns the minimum element in the sequence.
- [func min(by: (Self.Element, Self.Element) throws -> Bool) rethrows -> Self.Element?](data/min(by:).md)
  Returns the minimum element in the sequence, using the given predicate as the comparison between elements.
- [func range(of: Data, options: Data.SearchOptions, in: Range<Data.Index>?) -> Range<Data.Index>?](data/range(of:options:in:).md)
  Finds the range of the specified data as a subsequence of this data, if it exists.
- [typealias SearchOptions](data/searchoptions.md)
  Options that control a data search operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/data/max(by:))*
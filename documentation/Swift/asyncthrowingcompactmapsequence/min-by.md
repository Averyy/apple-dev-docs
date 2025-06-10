# min(by:)

**Framework**: Swift  
**Kind**: method

Returns the minimum element in the asynchronous sequence, using the given predicate as the comparison between elements.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
@warn_unqualified_access
func min(by areInIncreasingOrder: (Self.Element, Self.Element) async throws -> Bool) async rethrows -> Self.Element?
```

#### Return Value

The sequence’s minimum element, according to `areInIncreasingOrder`. If the sequence has no elements, returns `nil`.

#### Discussion

Use this method when the asynchronous sequence’s values don’t conform to `Comparable`, or when you want to apply a custom ordering to the sequence.

The predicate must be a  over the elements. That is, for any elements `a`, `b`, and `c`, the following conditions must hold:

- `areInIncreasingOrder(a, a)` is always `false`. (Irreflexivity)
- If `areInIncreasingOrder(a, b)` and `areInIncreasingOrder(b, c)` are both `true`, then `areInIncreasingOrder(a, c)` is also `true`. (Transitive comparability)
- Two elements are  if neither is ordered before the other according to the predicate. If `a` and `b` are incomparable, and `b` and `c` are incomparable, then `a` and `c` are also incomparable. (Transitive incomparability)

The following example uses an enumeration of playing cards ranks, `Rank`, which ranges from `ace` (low) to `king` (high). An asynchronous sequence called `RankCounter` produces all elements of the array. The predicate provided to the `min(by:)` method sorts ranks based on their `rawValue`:

```swift
enum Rank: Int {
    case ace = 1, two, three, four, five, six, seven, eight, nine, ten, jack, queen, king
}

let min = await RankCounter()
    .min { $0.rawValue < $1.rawValue }
print(min ?? "none")
// Prints "ace"
```

## Parameters

- `areInIncreasingOrder`: A predicate that returns   if its   first argument should be ordered before its second argument; otherwise,   .


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/asyncthrowingcompactmapsequence/min(by:))*
# min(by:)

**Framework**: RealityKit  
**Kind**: method

Returns the minimum element in the sequence, using the given predicate as the comparison between elements.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- visionOS ?+

## Declaration

```swift
@warn_unqualified_access
func min(by areInIncreasingOrder: (Self.Element, Self.Element) throws -> Bool) rethrows -> Self.Element?
```

#### Return Value

The sequence’s minimum element, according to `areInIncreasingOrder`. If the sequence has no elements, returns `nil`.

#### Discussion

The predicate must be a  over the elements. That is, for any elements `a`, `b`, and `c`, the following conditions must hold:

- `areInIncreasingOrder(a, a)` is always `false`. (Irreflexivity)
- If `areInIncreasingOrder(a, b)` and `areInIncreasingOrder(b, c)` are both `true`, then `areInIncreasingOrder(a, c)` is also `true`. (Transitive comparability)
- Two elements are  if neither is ordered before the other according to the predicate. If `a` and `b` are incomparable, and `b` and `c` are incomparable, then `a` and `c` are also incomparable. (Transitive incomparability)

This example shows how to use the `min(by:)` method on a dictionary to find the key-value pair with the lowest value.

```None
let hues = ["Heliotrope": 296, "Coral": 16, "Aquamarine": 156]
let leastHue = hues.min { a, b in a.value < b.value }
print(leastHue)
// Prints "Optional((key: "Coral", value: 16))"
```

> **Note**: O(), where  is the length of the sequence.

O(), where  is the length of the sequence.

## Parameters

- `areInIncreasingOrder`: A predicate that returns    if its first argument should be ordered before its second   argument; otherwise,  .


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/realityviewentitycollection/min(by:))*
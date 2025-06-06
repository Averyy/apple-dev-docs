# difference(from:by:)

**Framework**: TabularData  
**Kind**: method

Returns the difference needed to produce this collection’s ordered elements from the given collection, using the given predicate as an equivalence test.

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
func difference<C>(from other: C, by areEquivalent: (C.Element, Self.Element) -> Bool) -> CollectionDifference<Self.Element> where C : BidirectionalCollection, Self.Element == C.Element
```

#### Return Value

The difference needed to produce the receiver’s state from the parameter’s state.

#### Discussion

This function does not infer element moves. If you need to infer moves, call the `inferringMoves()` method on the resulting difference.

> **Note**: Worst case performance is O( * ), where  is the count of this collection and  is `other.count`. You can expect faster execution when the collections share many common elements.

Worst case performance is O( * ), where  is the count of this collection and  is `other.count`. You can expect faster execution when the collections share many common elements.

## Parameters

- `other`: The base state.
- `areEquivalent`: A closure that returns a Boolean value indicating   whether two elements are equivalent.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabulardata/rowgrouping/difference(from:by:))*
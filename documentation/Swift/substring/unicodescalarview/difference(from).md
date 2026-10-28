# difference(from:)

**Framework**: Swift  
**Kind**: method  
**Role**: Instance Method

Returns the difference needed to produce this collection’s ordered elements from the given collection.

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
func difference<C>(from other: C) -> CollectionDifference<Self.Element> where C : BidirectionalCollection, Self.Element == C.Element
```

Available when `Element` conforms to `Equatable`.

## Return Value

The difference needed to produce this collection’s ordered elements from the given collection.

## Discussion

This function does not infer element moves. If you need to infer moves, call the `inferringMoves()` method on the resulting difference.

> **Complexity**: Worst case performance is O(*n* * *m*), where *n* is the count of this collection and *m* is `other.count`. You can expect faster execution when the collections share many common elements, or if `Element` conforms to `Hashable`.

## Parameters

- `other`: The base state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/substring/unicodescalarview/difference(from:))*
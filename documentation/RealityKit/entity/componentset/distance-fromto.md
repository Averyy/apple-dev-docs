# distance(from:to:)

**Framework**: RealityKit  
**Kind**: method

Returns the distance between two indices.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 2.0+

## Declaration

```swift
@MainActor
@preconcurrency func distance(from start: Entity.ComponentSet.Index, to end: Entity.ComponentSet.Index) -> Int
```

#### Return Value

The distance between `start` and `end`. The result can be negative only if the collection conforms to the `BidirectionalCollection` protocol.

#### Discussion

Unless the collection conforms to the `BidirectionalCollection` protocol, `start` must be less than or equal to `end`.

> **Note**: O(1) if the collection conforms to `RandomAccessCollection`; otherwise, O(), where  is the resulting distance.

O(1) if the collection conforms to `RandomAccessCollection`; otherwise, O(), where  is the resulting distance.

## Parameters

- `start`: A valid index of the collection.
- `end`: Another valid index of the collection. If   is equal to   , the result is zero.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/entity/componentset/distance(from:to:))*
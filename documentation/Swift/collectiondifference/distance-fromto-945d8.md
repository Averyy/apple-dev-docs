# distance(from:to:)

**Framework**: Swift  
**Kind**: method

Returns the distance between two indices.

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
func distance(from start: Self.Index, to end: Self.Index) -> Int
```

#### Return Value

The distance between `start` and `end`. The result can be negative only if the collection conforms to the `BidirectionalCollection` protocol.

#### Discussion

Unless the collection conforms to the `BidirectionalCollection` protocol, `start` must be less than or equal to `end`.

> **Note**: O(1) if the collection conforms to `RandomAccessCollection`; otherwise, O(), where  is the resulting distance.

## Parameters

- `start`: A valid index of the collection.
- `end`: Another valid index of the collection. If   is equal to   , the result is zero.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/collectiondifference/distance(from:to:)-945d8)*
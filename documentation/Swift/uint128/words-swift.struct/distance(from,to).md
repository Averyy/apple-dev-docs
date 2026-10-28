# distance(from:to:)

**Framework**: Swift  
**Kind**: method  
**Role**: Instance Method

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
func distance(from start: Self.Index, to end: Self.Index) -> Self.Index.Stride
```

Available when `Index` conforms to `Strideable`, `Indices` is `Range<Self.Index>`, and `Index.Stride` is `Int`.

## Return Value

The distance between `start` and `end`.

## Discussion

> **Complexity**: O(1)

## Parameters

- `start`: A valid index of the collection.
- `end`: Another valid index of the collection. If `end` is equal to `start`, the result is zero.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/uint128/words-swift.struct/distance(from:to:))*
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
func distance(from start: Self.Index, to end: Self.Index) -> Self.Index.Stride
```

#### Return Value

The distance between `start` and `end`.

#### Discussion

> **Note**: O(1)

## Parameters

- `start`: A valid index of the collection.
- `end`: Another valid index of the collection. If   is equal to   , the result is zero.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/uint16/words-swift.struct/distance(from:to:))*
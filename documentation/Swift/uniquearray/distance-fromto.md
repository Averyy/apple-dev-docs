# distance(from:to:)

**Framework**: Swift  
**Kind**: method

Returns the distance between two indices.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
func distance(from start: UniqueArray<Element>.Index, to end: UniqueArray<Element>.Index) -> Int
```

#### Return Value

The distance between `start` and `end`.

#### Discussion

> **Note**: To improve performance, this method does not validate that the given index is valid before offseting it. Index validation is deferred until the resulting index is used to access an element. This optimization may be removed in future versions; do not rely on it.

> **Note**: O(1)

## Parameters

- `start`: A valid index of the collection.
- `end`: Another valid index of the collection. If end is equal to start, the result is zero.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/uniquearray/distance(from:to:))*
# distance(from:to:)

**Framework**: Swift  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

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

> **Complexity**: O(1) if the collection conforms to `RandomAccessCollection`; otherwise, O(*k*), where *k* is the resulting distance.

## Parameters

- `start`: A valid index of the collection.
- `end`: Another valid index of the collection. If `end` is equal to `start`, the result is zero.

## Default Implementations

### BidirectionalCollection Implementations
- [func distance(from: Self.Index, to: Self.Index) -> Int](../bidirectionalcollection/distance%28from,to%29-5ofg0.md)
- [func distance(from: Self.Index, to: Self.Index) -> Self.Index.Stride](../bidirectionalcollection/distance%28from,to%29-6p3we.md)
  Returns the distance between two indices.
### Collection Implementations
- [func distance<T>(from: Self.Index, to: Self.Index) -> T](./distance%28from,to%29-2rytr.md)
- [func distance(from: Self.Index, to: Self.Index) -> Int](./distance%28from,to%29-zoy0.md)
  Returns the distance between two indices.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/collection/distance(from:to:))*
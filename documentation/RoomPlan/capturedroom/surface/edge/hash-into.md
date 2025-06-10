# hash(into:)

**Framework**: RoomPlan  
**Kind**: method

Hashes the essential components of this value by feeding them into the given hasher.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+

## Declaration

```swift
func hash(into hasher: inout Hasher)
```

#### Discussion

Implement this method to conform to the `Hashable` protocol. The components used for hashing must be the same as the components compared in your type’s `==` operator implementation. Call `hasher.combine(_:)` with each of these components.

> ❗ **Important**: In your implementation of `hash(into:)`, don’t call `finalize()` on the `hasher` instance provided, or replace it with a different instance. Doing so may become a compile-time error in the future.

## Parameters

- `hasher`: The hasher to use when combining the components   of this instance.

## See Also

- [static func == (CapturedRoom.Surface.Edge, CapturedRoom.Surface.Edge) -> Bool](capturedroom/surface/edge/==(_:_:).md)
  Determines whether two surface edges are equal.
- [static func != (Self, Self) -> Bool](capturedroom/surface/edge/!=(_:_:).md)
  Determines whether two surface edges aren’t equal.
- [var hashValue: Int](capturedroom/surface/edge/hashvalue.md)
  The hash value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/roomplan/capturedroom/surface/edge/hash(into:))*
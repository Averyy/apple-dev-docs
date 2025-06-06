# hash(into:)

**Framework**: RoomPlan  
**Kind**: method

Hashes the essential components of this value by feeding them into the given hasher.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- visionOS 16.0+

## Declaration

```swift
func hash(into hasher: inout Hasher)
```

#### Discussion

Implement this method to conform to the `Hashable` protocol. The components used for hashing must be the same as the components compared in your type’s `==` operator implementation. Call `hasher.combine(_:)` with each of these components.

> ❗ **Important**: In your implementation of `hash(into:)`, don’t call `finalize()` on the `hasher` instance provided, or replace it with a different instance. Doing so may become a compile-time error in the future.

In your implementation of `hash(into:)`, don’t call `finalize()` on the `hasher` instance provided, or replace it with a different instance. Doing so may become a compile-time error in the future.

## Parameters

- `hasher`: The hasher to use when combining the components   of this instance.

## See Also

- [static func == (RoomBuilder.BuildError, RoomBuilder.BuildError) -> Bool](roombuilder/builderror/==(_:_:).md)
  Determines whether two errors are equal.
- [static func != (Self, Self) -> Bool](roombuilder/builderror/!=(_:_:).md)
  Determines whether two errors aren’t equal.
- [var hashValue: Int](roombuilder/builderror/hashvalue.md)
  The hash value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/roomplan/roombuilder/builderror/hash(into:))*
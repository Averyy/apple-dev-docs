# hash(into:)

**Framework**: RealityKit  
**Kind**: method

Hashes the essential components of this value by feeding them into the given hasher.

**Availability**:
- iOS 13.4+
- iPadOS 13.4+
- Mac Catalyst 13.4+
- macOS 10.15.4+
- visionOS ?+

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

- [var hashValue: Int](networkcompatibilitytoken/compatibility/hashvalue.md)
  The hash value.
- [static func != (Self, Self) -> Bool](networkcompatibilitytoken/compatibility/!=(_:_:).md)
  Returns a Boolean value indicating whether two values are not equal.
- [static func == (NetworkCompatibilityToken.Compatibility, NetworkCompatibilityToken.Compatibility) -> Bool](networkcompatibilitytoken/compatibility/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/networkcompatibilitytoken/compatibility/hash(into:))*
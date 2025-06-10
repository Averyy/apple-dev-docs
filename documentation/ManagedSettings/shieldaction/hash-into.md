# hash(into:)

**Framework**: ManagedSettings  
**Kind**: method

Hashes the essential components of this value by feeding them into the given hasher.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+

## Declaration

```swift
func hash(into hasher: inout Hasher)
```

#### Discussion

Implement this method to conform to the [`Hashable`](https://developer.apple.com/documentation/Swift/Hashable) protocol. The components used for hashing must be the same as the components compared in your type’s `==` operator implementation. Call `hasher.combine(_:)` with each of these components.

> ❗ **Important**: Never call `finalize()` on hasher; it may cause a compile-time error.

## Parameters

- `hasher`: The hasher to use when combining the components of this instance.

## See Also

- [static func != (Self, Self) -> Bool](shieldaction/!=(_:_:).md)
  Returns a Boolean value that indicates whether two values aren’t equal.
- [var hashValue: Int](shieldaction/hashvalue.md)
  The hash value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/managedsettings/shieldaction/hash(into:))*
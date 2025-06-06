# hashValue

**Framework**: RoomPlan  
**Kind**: property

The hash value.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+

## Declaration

```swift
var hashValue: Int { get }
```

#### Discussion

Hash values are not guaranteed to be equal across different executions of your program. Do not save hash values to use during a future execution.

> ❗ **Important**: `hashValue` is deprecated as a `Hashable` requirement. To conform to `Hashable`, implement the `hash(into:)` requirement instead. The compiler provides an implementation for `hashValue` for you.

`hashValue` is deprecated as a `Hashable` requirement. To conform to `Hashable`, implement the `hash(into:)` requirement instead. The compiler provides an implementation for `hashValue` for you.

## See Also

- [static func == (CapturedRoom.Surface.Edge, CapturedRoom.Surface.Edge) -> Bool](capturedroom/surface/edge/==(_:_:).md)
  Determines whether two surface edges are equal.
- [static func != (Self, Self) -> Bool](capturedroom/surface/edge/!=(_:_:).md)
  Determines whether two surface edges aren’t equal.
- [func hash(into: inout Hasher)](capturedroom/surface/edge/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.


---

*[View on Apple Developer](https://developer.apple.com/documentation/roomplan/capturedroom/surface/edge/hashvalue)*
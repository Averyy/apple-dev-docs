# !=(_:_:)

**Framework**: RoomPlan  
**Kind**: op

Determines whether two captured room errors aren’t equal.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+

## Declaration

```swift
static func != (lhs: Self, rhs: Self) -> Bool
```

#### Return Value

`true` if the errors aren’t equal. Otherwise, returns `false`.

## Parameters

- `lhs`: The error argument on the left-hand side of the operator.
- `rhs`: The error argument on the right-hand side of the operator.

## See Also

- [static func == (CapturedRoom.Error, CapturedRoom.Error) -> Bool](capturedroom/error/==(_:_:).md)
  Determines whether two captured room errors are equal.
- [func hash(into: inout Hasher)](capturedroom/error/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
- [var hashValue: Int](capturedroom/error/hashvalue.md)
  The hash value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/roomplan/capturedroom/error/!=(_:_:))*
# !=(_:_:)

**Framework**: RoomPlan  
**Kind**: op

Determines whether two confidence values aren’t equal.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+

## Declaration

```swift
static func != (lhs: Self, rhs: Self) -> Bool
```

#### Return Value

`true` if the confidence values aren’t equal. Otherwise, returns `false`.

## Parameters

- `lhs`: The confidence argument on the left-hand side of the operator.
- `rhs`: The confidence argument on the right-hand side of the operator.

## See Also

- [static func == (CapturedRoom.Confidence, CapturedRoom.Confidence) -> Bool](capturedroom/confidence/==(_:_:).md)
  Determines whether two confidence values are equal.
- [func hash(into: inout Hasher)](capturedroom/confidence/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
- [var hashValue: Int](capturedroom/confidence/hashvalue.md)
  The hash value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/roomplan/capturedroom/confidence/!=(_:_:))*
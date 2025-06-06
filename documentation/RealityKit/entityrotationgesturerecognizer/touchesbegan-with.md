# touchesBegan(_:with:)

**Framework**: RealityKit  
**Kind**: method

Sent to the gesture recognizer when one or more fingers touch down on the associated entity.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 14.0+

## Declaration

```swift
@MainActor
@preconcurrency override dynamic func touchesBegan(_ touches: Set<UITouch>, with event: UIEvent)
```

## Parameters

- `touches`: A set of   instances in the event represented by   that represent the touches in the    phase.
- `event`: A   object representing the event to which the touches belong.

## See Also

- [var entity: (any HasCollision)?](entityrotationgesturerecognizer/entity.md)
  The entity the receiver is associated with
- [func canPrevent(UIGestureRecognizer) -> Bool](entityrotationgesturerecognizer/canprevent(_:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/entityrotationgesturerecognizer/touchesbegan(_:with:))*
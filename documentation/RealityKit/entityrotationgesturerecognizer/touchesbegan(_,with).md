# touchesBegan(_:with:)

**Framework**: RealityKit  
**Kind**: method  
**Role**: Instance Method

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

- `touches`: A set of `UITouch` instances in the event represented by `event` that represent the touches in the `UITouch.Phase.began` phase.
- `event`: A `UIEvent` object representing the event to which the touches belong.

## See Also

### Using the recognizer
- [var entity: (any HasCollision)?](./entity.md)
  The entity the receiver is associated with
- [func canPrevent(UIGestureRecognizer) -> Bool](./canprevent%28_%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/entityrotationgesturerecognizer/touchesbegan(_:with:))*
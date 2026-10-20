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
- [func location(in: Entity?) -> SIMD3<Float>?](./location%28in%29.md)
  Returns the unprojected location of the gesture represented by the receiver in the space of the given entity.
- [func reset()](./reset%28%29.md)
  Overridden to reset internal state when a gesture recognition attempt completes.
- [func setTranslation(SIMD3<Float>, in: Entity?)](./settranslation%28_,in%29.md)
  Sets the translation of the receiver in the entity’s coordinate space
- [func touchesCancelled(Set<UITouch>, with: UIEvent)](./touchescancelled%28_,with%29.md)
  Sent to the gesture recognizer when a system event (such as an incoming phone call) cancels a touch event.
- [func touchesEnded(Set<UITouch>, with: UIEvent)](./touchesended%28_,with%29.md)
  Sent to the gesture recognizer when one or more fingers lift from the associated view.
- [func touchesMoved(Set<UITouch>, with: UIEvent)](./touchesmoved%28_,with%29.md)
  Sent to the gesture recognizer when one or more fingers move in the associated view.
- [func translation(in: Entity?) -> SIMD3<Float>?](./translation%28in%29.md)
  The translation of the gesture in the space of the specified entity.
- [func velocity(in: Entity?) -> SIMD3<Float>](./velocity%28in%29.md)
  The velocity of the translation gesture in the space of the specified entity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/entitytranslationgesturerecognizer/touchesbegan(_:with:))*
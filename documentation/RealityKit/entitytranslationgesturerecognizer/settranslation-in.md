# setTranslation(_:in:)

**Framework**: RealityKit  
**Kind**: method

Sets the translation of the receiver in the entity’s coordinate space

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 14.0+

## Declaration

```swift
@MainActor
@preconcurrency func setTranslation(_ translation: SIMD3<Float>, in entity: Entity?)
```

## Parameters

- `translation`: A point that identifies the new translation value.
- `entity`: An entity in whose space the translation is to occur.   A   entity will result in world space.

## See Also

- [var entity: (any HasCollision)?](entitytranslationgesturerecognizer/entity.md)
  The entity the receiver is associated with
- [func canPrevent(UIGestureRecognizer) -> Bool](entitytranslationgesturerecognizer/canprevent(_:).md)
- [func location(in: Entity?) -> SIMD3<Float>?](entitytranslationgesturerecognizer/location(in:).md)
  Returns the unprojected location of the gesture represented by the receiver in the space of the given entity.
- [func reset()](entitytranslationgesturerecognizer/reset.md)
  Overridden to reset internal state when a gesture recognition attempt completes.
- [func touchesBegan(Set<UITouch>, with: UIEvent)](entitytranslationgesturerecognizer/touchesbegan(_:with:).md)
  Sent to the gesture recognizer when one or more fingers touch down on the associated entity.
- [func touchesCancelled(Set<UITouch>, with: UIEvent)](entitytranslationgesturerecognizer/touchescancelled(_:with:).md)
  Sent to the gesture recognizer when a system event (such as an incoming phone call) cancels a touch event.
- [func touchesEnded(Set<UITouch>, with: UIEvent)](entitytranslationgesturerecognizer/touchesended(_:with:).md)
  Sent to the gesture recognizer when one or more fingers lift from the associated view.
- [func touchesMoved(Set<UITouch>, with: UIEvent)](entitytranslationgesturerecognizer/touchesmoved(_:with:).md)
  Sent to the gesture recognizer when one or more fingers move in the associated view.
- [func translation(in: Entity?) -> SIMD3<Float>?](entitytranslationgesturerecognizer/translation(in:).md)
  The translation of the gesture in the space of the specified entity.
- [func velocity(in: Entity?) -> SIMD3<Float>](entitytranslationgesturerecognizer/velocity(in:).md)
  The velocity of the translation gesture in the space of the specified entity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/entitytranslationgesturerecognizer/settranslation(_:in:))*
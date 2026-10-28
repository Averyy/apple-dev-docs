# location(in:)

**Framework**: RealityKit  
**Kind**: method  
**Role**: Instance Method

Returns the unprojected location of the gesture represented by the receiver in the space of the given entity.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 14.0+

## Declaration

```swift
@MainActor
@preconcurrency func location(in entity: Entity?) -> SIMD3<Float>?
```

## Return Value

The 3D position identifying the location of the gesture in the space specified.

## Discussion

The location is typically the result of a centroid of touches for a gesture, unprojected onto the associated `entity`, and then converted into the space of the entity passed in, or world space if `nil` is passed in.

## Parameters

- `entity`: An entity in whose space the location is computed. A `nil` entity will result in world space.

## See Also

### Using the recognizer
- [var entity: (any HasCollision)?](./entity.md)
  The entity the receiver is associated with
- [func canPrevent(UIGestureRecognizer) -> Bool](./canprevent%28_%29.md)
- [func reset()](./reset%28%29.md)
  Overridden to reset internal state when a gesture recognition attempt completes.
- [func setTranslation(SIMD3<Float>, in: Entity?)](./settranslation%28_,in%29.md)
  Sets the translation of the receiver in the entity’s coordinate space
- [func touchesBegan(Set<UITouch>, with: UIEvent)](./touchesbegan%28_,with%29.md)
  Sent to the gesture recognizer when one or more fingers touch down on the associated entity.
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

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/entitytranslationgesturerecognizer/location(in:))*
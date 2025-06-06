# EntityTranslationGestureRecognizer

**Framework**: RealityKit  
**Kind**: class

A gesture recognizer that uses a pan gesture to move an entity.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 14.0+

## Declaration

```swift
@MainActor
@objc @preconcurrency class EntityTranslationGestureRecognizer
```

#### Overview

A gesture recognizer that handles pan and dragging gestures on an entity.

## Topics

### Creating a recognizer
- [init(target: Any?, action: Selector?)](entitytranslationgesturerecognizer/init(target:action:).md)
### Using the recognizer
- [var entity: (any HasCollision)?](entitytranslationgesturerecognizer/entity.md)
  The entity the receiver is associated with
- [func canPrevent(UIGestureRecognizer) -> Bool](entitytranslationgesturerecognizer/canprevent(_:).md)
- [func location(in: Entity?) -> SIMD3<Float>?](entitytranslationgesturerecognizer/location(in:).md)
  Returns the unprojected location of the gesture represented by the receiver in the space of the given entity.
- [func reset()](entitytranslationgesturerecognizer/reset.md)
  Overridden to reset internal state when a gesture recognition attempt completes.
- [func setTranslation(SIMD3<Float>, in: Entity?)](entitytranslationgesturerecognizer/settranslation(_:in:).md)
  Sets the translation of the receiver in the entity’s coordinate space
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
### Default Implementations
- [EntityGestureRecognizer Implementations](entitytranslationgesturerecognizer/entitygesturerecognizer-implementations.md)

## Relationships

### Inherits From
- [UIGestureRecognizer](../UIKit/UIGestureRecognizer.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [EntityGestureRecognizer](entitygesturerecognizer.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [ARView.EntityGestures](arview/entitygestures.md)
  The set of possible entity gesture recognizers.
- [class EntityRotationGestureRecognizer](entityrotationgesturerecognizer.md)
  A gesture recognizer that uses rotation gestures involving two touches to rotate a given entity.
- [class EntityScaleGestureRecognizer](entityscalegesturerecognizer.md)
  A gesture recognizer that uses a pinch gesture to scale or zoom an entity.
- [protocol EntityGestureRecognizer](entitygesturerecognizer.md)
  A gesture recognizer that works on entities.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/entitytranslationgesturerecognizer)*
# EntityTranslationGestureRecognizer

**Framework**: RealityKit  
**Kind**: class  
**Role**: Class

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
- [init(target: Any?, action: Selector?)](./entitytranslationgesturerecognizer/init%28target,action%29.md)
### Using the recognizer
- [var entity: (any HasCollision)?](./entitytranslationgesturerecognizer/entity.md)
  The entity the receiver is associated with
- [func canPrevent(UIGestureRecognizer) -> Bool](./entitytranslationgesturerecognizer/canprevent%28_%29.md)
- [func location(in: Entity?) -> SIMD3<Float>?](./entitytranslationgesturerecognizer/location%28in%29.md)
  Returns the unprojected location of the gesture represented by the receiver in the space of the given entity.
- [func reset()](./entitytranslationgesturerecognizer/reset%28%29.md)
  Overridden to reset internal state when a gesture recognition attempt completes.
- [func setTranslation(SIMD3<Float>, in: Entity?)](./entitytranslationgesturerecognizer/settranslation%28_,in%29.md)
  Sets the translation of the receiver in the entity’s coordinate space
- [func touchesBegan(Set<UITouch>, with: UIEvent)](./entitytranslationgesturerecognizer/touchesbegan%28_,with%29.md)
  Sent to the gesture recognizer when one or more fingers touch down on the associated entity.
- [func touchesCancelled(Set<UITouch>, with: UIEvent)](./entitytranslationgesturerecognizer/touchescancelled%28_,with%29.md)
  Sent to the gesture recognizer when a system event (such as an incoming phone call) cancels a touch event.
- [func touchesEnded(Set<UITouch>, with: UIEvent)](./entitytranslationgesturerecognizer/touchesended%28_,with%29.md)
  Sent to the gesture recognizer when one or more fingers lift from the associated view.
- [func touchesMoved(Set<UITouch>, with: UIEvent)](./entitytranslationgesturerecognizer/touchesmoved%28_,with%29.md)
  Sent to the gesture recognizer when one or more fingers move in the associated view.
- [func translation(in: Entity?) -> SIMD3<Float>?](./entitytranslationgesturerecognizer/translation%28in%29.md)
  The translation of the gesture in the space of the specified entity.
- [func velocity(in: Entity?) -> SIMD3<Float>](./entitytranslationgesturerecognizer/velocity%28in%29.md)
  The velocity of the translation gesture in the space of the specified entity.

## Relationships

### Inherits From
- [UIGestureRecognizer](../UIKit/uigesturerecognizer.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [EntityGestureRecognizer](./entitygesturerecognizer.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### UIKit and AppKit gestures
- [ARView.EntityGestures](./arview/entitygestures.md)
  The set of possible entity gesture recognizers.
- [class EntityRotationGestureRecognizer](./entityrotationgesturerecognizer.md)
  A gesture recognizer that uses rotation gestures involving two touches to rotate a given entity.
- [class EntityScaleGestureRecognizer](./entityscalegesturerecognizer.md)
  A gesture recognizer that uses a pinch gesture to scale or zoom an entity.
- [protocol EntityGestureRecognizer](./entitygesturerecognizer.md)
  A gesture recognizer that works on entities.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/entitytranslationgesturerecognizer)*
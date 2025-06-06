# EntityGestureRecognizer

**Framework**: RealityKit  
**Kind**: protocol

A gesture recognizer that works on entities.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 14.0+

## Declaration

```swift
protocol EntityGestureRecognizer : UIGestureRecognizer
```

## Topics

### Using the gesture recognizer
- [var entity: (any HasCollision)?](entitygesturerecognizer/entity.md)
  The entity the receiver is associated with
- [func location(in: Entity?) -> SIMD3<Float>?](entitygesturerecognizer/location(in:).md)
  Returns the unprojected location of the gesture represented by the receiver in the space of the given entity.

## Relationships

### Inherits From
- [UIGestureRecognizer](../UIKit/UIGestureRecognizer.md)
### Conforming Types
- [EntityRotationGestureRecognizer](entityrotationgesturerecognizer.md)
- [EntityScaleGestureRecognizer](entityscalegesturerecognizer.md)
- [EntityTranslationGestureRecognizer](entitytranslationgesturerecognizer.md)

## See Also

- [ARView.EntityGestures](arview/entitygestures.md)
  The set of possible entity gesture recognizers.
- [class EntityRotationGestureRecognizer](entityrotationgesturerecognizer.md)
  A gesture recognizer that uses rotation gestures involving two touches to rotate a given entity.
- [class EntityScaleGestureRecognizer](entityscalegesturerecognizer.md)
  A gesture recognizer that uses a pinch gesture to scale or zoom an entity.
- [class EntityTranslationGestureRecognizer](entitytranslationgesturerecognizer.md)
  A gesture recognizer that uses a pan gesture to move an entity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/entitygesturerecognizer)*
# ARView.EntityGestures

**Framework**: RealityKit  
**Kind**: struct

The set of possible entity gesture recognizers.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 14.0+

## Declaration

```swift
struct EntityGestures
```

## Topics

### Recognizing gesture types
- [static let all: ARView.EntityGestures](arview/entitygestures/all.md)
  All gesture types.
- [static let rotation: ARView.EntityGestures](arview/entitygestures/rotation.md)
  A multitouch gesture used to rotate an entity.
- [static let scale: ARView.EntityGestures](arview/entitygestures/scale.md)
  A pinch gesture used to scale an entity.
- [static let translation: ARView.EntityGestures](arview/entitygestures/translation.md)
  A single touch pan gesture used to move entities along their anchoring plane.
### Using entity gestures
- [protocol EntityGestureRecognizer](entitygesturerecognizer.md)
  A gesture recognizer that works on entities.
- [class EntityRotationGestureRecognizer](entityrotationgesturerecognizer.md)
  A gesture recognizer that uses rotation gestures involving two touches to rotate a given entity.
- [class EntityScaleGestureRecognizer](entityscalegesturerecognizer.md)
  A gesture recognizer that uses a pinch gesture to scale or zoom an entity.
- [class EntityTranslationGestureRecognizer](entitytranslationgesturerecognizer.md)
  A gesture recognizer that uses a pan gesture to move an entity.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [OptionSet](../Swift/OptionSet.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [SetAlgebra](../Swift/SetAlgebra.md)

## See Also

- [class EntityRotationGestureRecognizer](entityrotationgesturerecognizer.md)
  A gesture recognizer that uses rotation gestures involving two touches to rotate a given entity.
- [class EntityScaleGestureRecognizer](entityscalegesturerecognizer.md)
  A gesture recognizer that uses a pinch gesture to scale or zoom an entity.
- [class EntityTranslationGestureRecognizer](entitytranslationgesturerecognizer.md)
  A gesture recognizer that uses a pan gesture to move an entity.
- [protocol EntityGestureRecognizer](entitygesturerecognizer.md)
  A gesture recognizer that works on entities.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/arview/entitygestures)*
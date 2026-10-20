# EntityScaleGestureRecognizer

**Framework**: RealityKit  
**Kind**: class  
**Role**: Class

A gesture recognizer that uses a pinch gesture to scale or zoom an entity.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 14.0+

## Declaration

```swift
@MainActor
@objc @preconcurrency class EntityScaleGestureRecognizer
```

## Topics

### Creating the recognizer
- [init(target: Any?, action: Selector?)](./entityscalegesturerecognizer/init%28target,action%29.md)
### Using the recognizer
- [var entity: (any HasCollision)?](./entityscalegesturerecognizer/entity.md)
  The entity the receiver is associated with
- [func canPrevent(UIGestureRecognizer) -> Bool](./entityscalegesturerecognizer/canprevent%28_%29.md)
- [func touchesBegan(Set<UITouch>, with: UIEvent)](./entityscalegesturerecognizer/touchesbegan%28_,with%29.md)
  Sent to the gesture recognizer when one or more fingers touch down on the associated entity.

## Relationships

### Inherits From
- [UIPinchGestureRecognizer](../UIKit/uipinchgesturerecognizer.md)
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
- [class EntityTranslationGestureRecognizer](./entitytranslationgesturerecognizer.md)
  A gesture recognizer that uses a pan gesture to move an entity.
- [protocol EntityGestureRecognizer](./entitygesturerecognizer.md)
  A gesture recognizer that works on entities.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/entityscalegesturerecognizer)*
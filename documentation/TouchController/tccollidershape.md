# TCColliderShape

**Framework**: Touch Controller  
**Kind**: enum

Defines the shape of a control collider.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+

## Declaration

```swift
enum TCColliderShape
```

## Topics

### Shapes
- [TCColliderShape.circle](tccollidershape/circle.md)
  A circular collider.
- [TCColliderShape.leftSide](tccollidershape/leftside.md)
  A collider representing the left side of the view the touch controller is embedded in. Useful for thumbsticks and delta controls, so the user can easily hit the control without looking closely.
- [TCColliderShape.rect](tccollidershape/rect.md)
  A rectangular collider.
- [TCColliderShape.rightSide](tccollidershape/rightside.md)
  A collider representing the right side of the view the touch controller is embedded in. Useful for thumbsticks and delta controls, so the user can easily hit the control without looking closely.
### Creating a collider shape
- [init?(rawValue: Int)](tccollidershape/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../swift/bitwisecopyable.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [RawRepresentable](../swift/rawrepresentable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [var colliderShape: TCColliderShape](tcbutton/collidershape.md)
  The collider shape for the button.


---

*[View on Apple Developer](https://developer.apple.com/documentation/touchcontroller/tccollidershape)*
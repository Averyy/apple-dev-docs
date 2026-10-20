# TCColliderShape

**Framework**: Touch Controller  
**Kind**: enum  
**Role**: Enumeration

Defines the shape of a control collider.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+

## Declaration

```swift
enum TCColliderShape
```

```c
enum TCColliderShape : NSInteger;
```

## Topics

### Shapes
- [TCColliderShape.circle](./tccollidershape/circle.md)
  A circular collider.
- [TCColliderShape.leftSide](./tccollidershape/leftside.md)
  A collider representing the left side of the view the touch controller is embedded in. Useful for thumbsticks and delta controls, so the user can easily hit the control without looking closely.
- [TCColliderShape.rect](./tccollidershape/rect.md)
  A rectangular collider.
- [TCColliderShape.rightSide](./tccollidershape/rightside.md)
  A collider representing the right side of the view the touch controller is embedded in. Useful for thumbsticks and delta controls, so the user can easily hit the control without looking closely.
### Creating a collider shape
- [init?(rawValue: Int)](./tccollidershape/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Getting the collider shape
- [var colliderShape: TCColliderShape](./tcbutton/collidershape.md)
  The collider shape for the button.


---

*[View on Apple Developer](https://developer.apple.com/documentation/touchcontroller/tccollidershape)*
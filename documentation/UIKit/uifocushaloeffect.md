# UIFocusHaloEffect

**Framework**: UIKit  
**Kind**: class  
**Role**: Class

A visual focus effect that draws a halo around the focus item.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- visionOS 1.0+

## Declaration

```swift
class UIFocusHaloEffect
```

```objc
@interface UIFocusHaloEffect : UIFocusEffect
```

## Topics

### Creating a halo effect
- [convenience init(roundedRect: CGRect, cornerRadius: CGFloat, curve: CALayerCornerCurve)](./uifocushaloeffect/init%28roundedrect,cornerradius,curve%29.md)
  Creates a rounded halo effect using the specified corner radius and corner curve.
- [convenience init(rect: CGRect)](./uifocushaloeffect/init%28rect%29.md)
  Creates a rectangular halo effect using the specified rectangle.
- [convenience init(path: UIBezierPath)](./uifocushaloeffect/init%28path%29.md)
  Creates a halo effect using the specified Bézier path.
### Configuring a halo effect
- [var containerView: UIView?](./uifocushaloeffect/containerview.md)
  The container view to place the halo effect into.
- [var referenceView: UIView?](./uifocushaloeffect/referenceview.md)
  The view to place the halo effect above.
- [var position: UIFocusHaloEffect.Position](./uifocushaloeffect/position-swift.property.md)
  The position of the halo effect relative to its shape.
- [UIFocusHaloEffect.Position](./uifocushaloeffect/position-swift.enum.md)
  Constants that describe positions for drawing the halo focus effect.

## Relationships

### Inherits From
- [UIFocusEffect](./uifocuseffect.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Focus effects
- [class UIFocusEffect](./uifocuseffect.md)
  The base class for defining a visual focus effect.
- [UIFocusHaloEffect.Position](./uifocushaloeffect/position-swift.enum.md)
  Constants that describe positions for drawing the halo focus effect.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uifocushaloeffect)*
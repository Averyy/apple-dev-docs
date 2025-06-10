# UIFocusHaloEffect

**Framework**: UIKit  
**Kind**: class

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

## Topics

### Creating a halo effect
- [convenience init(roundedRect: CGRect, cornerRadius: CGFloat, curve: CALayerCornerCurve)](uifocushaloeffect/init(roundedrect:cornerradius:curve:).md)
  Creates a rounded halo effect using the specified corner radius and corner curve.
- [convenience init(rect: CGRect)](uifocushaloeffect/init(rect:).md)
  Creates a rectangular halo effect using the specified rectangle.
- [convenience init(path: UIBezierPath)](uifocushaloeffect/init(path:).md)
  Creates a halo effect using the specified Bézier path.
### Configuring a halo effect
- [var containerView: UIView?](uifocushaloeffect/containerview.md)
  The container view to place the halo effect into.
- [var referenceView: UIView?](uifocushaloeffect/referenceview.md)
  The view to place the halo effect above.
- [var position: UIFocusHaloEffect.Position](uifocushaloeffect/position-swift.property.md)
  The position of the halo effect relative to its shape.
- [UIFocusHaloEffect.Position](uifocushaloeffect/position-swift.enum.md)
  Constants that describe positions for drawing the halo focus effect.

## Relationships

### Inherits From
- [UIFocusEffect](uifocuseffect.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [class UIFocusEffect](uifocuseffect.md)
  The base class for defining a visual focus effect.
- [UIFocusHaloEffect.Position](uifocushaloeffect/position-swift.enum.md)
  Constants that describe positions for drawing the halo focus effect.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uifocushaloeffect)*
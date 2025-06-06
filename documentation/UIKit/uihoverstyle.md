# UIHoverStyle

**Framework**: UIKit  
**Kind**: class

The hover style to apply to a view, including an effect and a shape to use for displaying that effect.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
class UIHoverStyle
```

## Topics

### Creating a hover style
- [convenience init(effect: some UIHoverEffect, shape: UIShape?)](uihoverstyle/init(effect:shape:).md)
  Creates a hover style with the provided effect and shape.
- [convenience init(shape: UIShape?)](uihoverstyle/init(shape:).md)
  Creates a hover style with the provided shape and an automatic hover effect.
### Specifying a hover shape
- [var shape: UIShape?](uihoverstyle/shape-21npk.md)
  The shape to use for the hover effect.
- [struct UIShape](uishape-swift.struct.md)
  An abstract representation of a shape.
### Specifying a hover effect
- [var effect: any UIHoverEffect](uihoverstyle/effect-4vdoj.md)
  The effect to apply to the view with this style.
- [struct UIHoverAutomaticEffect](uihoverautomaticeffect-swift.struct.md)
  A system-default hover effect that automatically selects the appropriate effect based on the view to which it applies.
- [struct UIHoverHighlightEffect](uihoverhighlighteffect-swift.struct.md)
  An effect that applies a highlight to the view on hover.
- [struct UIHoverLiftEffect](uihoverlifteffect-swift.struct.md)
  An effect that can visually lift the view on hover where appropriate.
- [protocol UIHoverEffect](uihovereffect-40091.md)
  A hover effect that can apply to a view through a hover style.
### Managing the state of the hover effect
- [var isEnabled: Bool](uihoverstyle/isenabled.md)
  A Boolean value that determines whether the hover effect is active.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Inherited By
- [UIPointerStyle](uipointerstyle.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [var hoverStyle: UIHoverStyle?](uiview/hoverstyle.md)
  The hover style for the view.
- [class UIHoverEffectLayer](uihovereffectlayer.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uihoverstyle)*
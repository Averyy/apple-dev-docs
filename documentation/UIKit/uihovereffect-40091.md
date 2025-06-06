# UIHoverEffect

**Framework**: UIKit  
**Kind**: protocol

A hover effect that can apply to a view through a hover style.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst ?+
- visionOS 1.0+

## Declaration

```swift
protocol UIHoverEffect
```

#### Overview

You don’t conform to this protocol directly. Instead, you use a built-in [`UIHoverEffect`](uihovereffect-40091.md) like [`UIHoverAutomaticEffect`](uihoverautomaticeffect-swift.struct.md).

## Topics

### Choosing a hover effect
- [static var automatic: UIHoverAutomaticEffect](uihovereffect-40091/automatic.md)
  A system-default hover effect that automatically selects the appropriate effect based on the view to which it applies.
- [static var highlight: UIHoverHighlightEffect](uihovereffect-40091/highlight.md)
  An effect that applies a highlight to the view on hover.
- [static var lift: UIHoverLiftEffect](uihovereffect-40091/lift.md)
  An effect that can visually lift the view on hover where appropriate.

## Relationships

### Conforming Types
- [UIHoverAutomaticEffect](uihoverautomaticeffect-swift.struct.md)
- [UIHoverHighlightEffect](uihoverhighlighteffect-swift.struct.md)
- [UIHoverLiftEffect](uihoverlifteffect-swift.struct.md)
- [UIPointerEffect](uipointereffect-swift.enum.md)

## See Also

- [var effect: any UIHoverEffect](uihoverstyle/effect-4vdoj.md)
  The effect to apply to the view with this style.
- [struct UIHoverAutomaticEffect](uihoverautomaticeffect-swift.struct.md)
  A system-default hover effect that automatically selects the appropriate effect based on the view to which it applies.
- [struct UIHoverHighlightEffect](uihoverhighlighteffect-swift.struct.md)
  An effect that applies a highlight to the view on hover.
- [struct UIHoverLiftEffect](uihoverlifteffect-swift.struct.md)
  An effect that can visually lift the view on hover where appropriate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uihovereffect-40091)*
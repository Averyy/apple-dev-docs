# effect

**Framework**: UIKit  
**Kind**: property

The effect to apply to the view with this style.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
@preconcurrency var effect: any UIHoverEffect { get set }
```

#### Discussion

Use [`UIHoverAutomaticEffect`](uihoverautomaticeffect-swift.struct.md) to apply a system-default effect to the view.

## See Also

- [struct UIHoverAutomaticEffect](uihoverautomaticeffect-swift.struct.md)
  A system-default hover effect that automatically selects the appropriate effect based on the view to which it applies.
- [struct UIHoverHighlightEffect](uihoverhighlighteffect-swift.struct.md)
  An effect that applies a highlight to the view on hover.
- [struct UIHoverLiftEffect](uihoverlifteffect-swift.struct.md)
  An effect that can visually lift the view on hover where appropriate.
- [protocol UIHoverEffect](uihovereffect-40091.md)
  A hover effect that can apply to a view through a hover style.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uihoverstyle/effect-4vdoj)*
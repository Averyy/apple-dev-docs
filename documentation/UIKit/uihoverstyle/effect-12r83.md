# effect

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The effect to apply to the view with this style.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- visionOS 1.0+

## Declaration

```objc
@property (nonatomic, strong) id<UIHoverEffect> effect;
```

#### Discussion

Use [`UIHoverAutomaticEffect`](../uihoverautomaticeffect-swift.struct.md) to apply a system-default effect to the view.

## See Also

### Specifying a hover effect
- [UIHoverAutomaticEffect](../uihoverautomaticeffect-c.class.md)
  A system-default hover effect that automatically selects the appropriate effect based on the view to which it applies.
- [UIHoverHighlightEffect](../uihoverhighlighteffect-c.class.md)
  An effect that applies a highlight to the view on hover.
- [UIHoverLiftEffect](../uihoverlifteffect-c.class.md)
  An effect that can visually lift the view on hover where appropriate.
- [UIHoverEffect](../uihovereffect-ukid.md)
  A hover effect that can apply to a view through a hover style.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uihoverstyle/effect-12r83)*
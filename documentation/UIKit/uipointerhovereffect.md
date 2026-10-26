# UIPointerHoverEffect

**Framework**: UIKit  
**Kind**: class  
**Role**: Class

An effect where visual changes apply to the view and the pointer retains its default shape.

**Availability**:
- iOS 13.4+
- iPadOS 13.4+
- Mac Catalyst 13.4+
- visionOS 1.0+

## Declaration

```objc
@interface UIPointerHoverEffect : UIPointerEffect
```

#### Overview

Use the properties of [`UIPointerHoverEffect`](./uipointerhovereffect.md) to define the visual changes to apply to the view.

## Topics

### Specifying the tint mode
- [preferredTintMode](./uipointerhovereffect/preferredtintmode.md)
  The preferred tint mode for the effect.
- [UIPointerEffectTintMode](./uipointereffecttintmode.md)
  An effect that defines how to apply a tint to a view during a pointer interaction.
### Customizing the effect
- [prefersShadow](./uipointerhovereffect/prefersshadow.md)
  A Boolean value that determines whether to add a shadow.
- [prefersScaledContent](./uipointerhovereffect/prefersscaledcontent.md)
  A Boolean value that determines whether to scale the content.

## Relationships

### Inherits From
- [UIPointerEffect](./uipointereffect-c.class.md)

## See Also

### Creating a specific effect
- [UIPointerHighlightEffect](./uipointerhighlighteffect.md)
  An effect where the pointer slides under the given view and morphs into the view’s shape.
- [UIPointerLiftEffect](./uipointerlifteffect.md)
  An effect where the pointer slides under the given view and disappears as the view scales up and gains a shadow.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipointerhovereffect)*
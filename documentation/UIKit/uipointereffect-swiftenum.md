# UIPointerEffect

**Framework**: UIKit  
**Kind**: enum

An effect that alters a view’s appearance when a pointer enters the current region.

**Availability**:
- iOS 13.4+
- iPadOS 13.4+
- Mac Catalyst ?+
- visionOS ?+

## Declaration

```swift
enum UIPointerEffect
```

#### Overview

`UIPointerEffect` automatically attempts to determine the appropriate effect for the given preview. Use one of its enumeration cases to request a specific system-provided effect.

## Topics

### Accessing the preview
- [var preview: UITargetedPreview](uipointereffect-swift.enum/preview.md)
  A preview of the view used during an interaction’s animations.
### Creating a default effect
- [case automatic(UITargetedPreview)](uipointereffect-swift.enum/automatic(_:).md)
  A pointer content effect with the given preview’s view.
### Creating a specific effect
- [case highlight(UITargetedPreview)](uipointereffect-swift.enum/highlight(_:).md)
  An effect where the pointer slides under the given view and morphs into the view’s shape.
- [case hover(UITargetedPreview, preferredTintMode: UIPointerEffect.TintMode, prefersShadow: Bool, prefersScaledContent: Bool)](uipointereffect-swift.enum/hover(_:preferredtintmode:prefersshadow:prefersscaledcontent:).md)
  An effect where visual changes apply to the view and the pointer retains its default shape.
- [case lift(UITargetedPreview)](uipointereffect-swift.enum/lift(_:).md)
  An effect where the pointer slides under the given view and disappears as the view scales up and gains a shadow.
### Enumerations
- [UIPointerEffect.TintMode](uipointereffect-swift.enum/tintmode.md)
  An effect that defines how to apply a tint to a view during a pointer interaction.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Sendable](../Swift/Sendable.md)
- [UIHoverEffect](uihovereffect-40091.md)

## See Also

- [class UIPointerStyle](uipointerstyle.md)
  An object that defines the pointer shape and effect.
- [enum UIPointerShape](uipointershape-swift.enum.md)
  An object that defines the shape of custom pointers.
- [class UIPointerAccessory](uipointeraccessory.md)
  Constants that describe accessories to display alongside the primary pointer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipointereffect-swift.enum)*
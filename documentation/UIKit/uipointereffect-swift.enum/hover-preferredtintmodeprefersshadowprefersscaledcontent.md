# UIPointerEffect.hover(_:preferredTintMode:prefersShadow:prefersScaledContent:)

**Framework**: UIKit  
**Kind**: case

An effect where visual changes apply to the view and the pointer retains its default shape.

**Availability**:
- iOS 13.4+
- iPadOS 13.4+
- Mac Catalyst ?+
- visionOS ?+

## Declaration

```swift
case hover(UITargetedPreview, preferredTintMode: UIPointerEffect.TintMode = .overlay, prefersShadow: Bool = false, prefersScaledContent: Bool = true)
```

## Topics

### Specifying the Tint Mode
- [UIPointerEffect.TintMode](uipointereffect-swift.enum/tintmode.md)
  An effect that defines how to apply a tint to a view during a pointer interaction.

## See Also

- [case highlight(UITargetedPreview)](uipointereffect-swift.enum/highlight(_:).md)
  An effect where the pointer slides under the given view and morphs into the view’s shape.
- [case lift(UITargetedPreview)](uipointereffect-swift.enum/lift(_:).md)
  An effect where the pointer slides under the given view and disappears as the view scales up and gains a shadow.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipointereffect-swift.enum/hover(_:preferredtintmode:prefersshadow:prefersscaledcontent:))*
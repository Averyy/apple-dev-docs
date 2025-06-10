# NSViewAnimation.EffectName

**Framework**: AppKit  
**Kind**: struct

The following constants specify the animation effect to apply and are used as values for the animation effect property of the animation view. See the description of [`effect`](nsviewanimation/key/effect.md) for usage details.

**Availability**:
- macOS ?+

## Declaration

```swift
struct EffectName
```

## Topics

### Effect Names
- [static let fadeIn: NSViewAnimation.EffectName](nsviewanimation/effectname/fadein.md)
  Specifies a fade-in type of effect.
- [static let fadeOut: NSViewAnimation.EffectName](nsviewanimation/effectname/fadeout.md)
  Specifies a fade-out type of effect.
### Initializers
- [init(rawValue: String)](nsviewanimation/effectname/init(rawvalue:).md)

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var viewAnimations: [[NSViewAnimation.Key : Any]]](nsviewanimation/viewanimations.md)
  The dictionaries defining the objects to animate.
- [NSViewAnimation.Key](nsviewanimation/key.md)
  The following string constants are keys for the dictionaries in the array passed into [`init(viewAnimations:)`](nsviewanimation/init(viewanimations:).md) and [`viewAnimations`](nsviewanimation/viewanimations.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsviewanimation/effectname)*
# NSViewAnimation.Key

**Framework**: AppKit  
**Kind**: struct

The following string constants are keys for the dictionaries in the array passed into [`init(viewAnimations:)`](nsviewanimation/init(viewanimations:).md) and [`viewAnimations`](nsviewanimation/viewanimations.md).

**Availability**:
- macOS ?+

## Declaration

```swift
struct Key
```

## Topics

### Keys
- [static let effect: NSViewAnimation.Key](nsviewanimation/key/effect.md)
  An effect to apply to the animation.
- [static let endFrame: NSViewAnimation.Key](nsviewanimation/key/endframe.md)
  The size and location of the window or view at the end of the animation.
- [static let startFrame: NSViewAnimation.Key](nsviewanimation/key/startframe.md)
  The size and location of the window or view at the start of the animation.
- [static let target: NSViewAnimation.Key](nsviewanimation/key/target.md)
  The target of the animation.
### Initializers
- [init(rawValue: String)](nsviewanimation/key/init(rawvalue:).md)

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
- [NSViewAnimation.EffectName](nsviewanimation/effectname.md)
  The following constants specify the animation effect to apply and are used as values for the animation effect property of the animation view. See the description of [`effect`](nsviewanimation/key/effect.md) for usage details.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsviewanimation/key)*
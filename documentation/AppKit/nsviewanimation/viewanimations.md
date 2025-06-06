# viewAnimations

**Framework**: AppKit  
**Kind**: property

The dictionaries defining the objects to animate.

**Availability**:
- macOS ?+

## Declaration

```swift
var viewAnimations: [[NSViewAnimation.Key : Any]] { get set }
```

## See Also

- [NSViewAnimation.Key](nsviewanimation/key.md)
  The following string constants are keys for the dictionaries in the array passed into [`init(viewAnimations:)`](nsviewanimation/init(viewanimations:).md) and [`viewAnimations`](nsviewanimation/viewanimations.md).
- [NSViewAnimation.EffectName](nsviewanimation/effectname.md)
  The following constants specify the animation effect to apply and are used as values for the animation effect property of the animation view. See the description of [`effect`](nsviewanimation/key/effect.md) for usage details.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsviewanimation/viewanimations)*
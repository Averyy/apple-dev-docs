# viewAnimations

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The dictionaries defining the objects to animate.

**Availability**:
- macOS

## Declaration

```swift
var viewAnimations: [[NSViewAnimation.Key : Any]] { get set }
```

```objc
@property (copy) NSArray<NSDictionary<NSString *,id> *> * viewAnimations;
```

## See Also

### Getting and setting view-animation dictionaries
- [NSViewAnimation.Key](./key.md)
  The following string constants are keys for the dictionaries in the array passed into [`init(viewAnimations:)`](./init%28viewanimations%29.md) and [`viewAnimations`](./viewanimations.md).
- [NSViewAnimation.EffectName](./effectname.md)
  The following constants specify the animation effect to apply and are used as values for the animation effect property of the animation view. See the description of [`effect`](./key/effect.md) for usage details.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsviewanimation/viewanimations)*
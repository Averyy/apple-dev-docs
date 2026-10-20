# NSViewAnimation.Key

**Framework**: AppKit  
**Kind**: struct  
**Role**: Structure

The following string constants are keys for the dictionaries in the array passed into [`init(viewAnimations:)`](./init%28viewanimations%29.md) and [`viewAnimations`](./viewanimations.md).

**Availability**:
- macOS

## Declaration

```swift
struct Key
```

```c
typedef NSString * NSViewAnimationKey;
```

## Topics

### Keys
- [static let effect: NSViewAnimation.Key](./key/effect.md)
  An effect to apply to the animation.
- [static let endFrame: NSViewAnimation.Key](./key/endframe.md)
  The size and location of the window or view at the end of the animation.
- [static let startFrame: NSViewAnimation.Key](./key/startframe.md)
  The size and location of the window or view at the start of the animation.
- [static let target: NSViewAnimation.Key](./key/target.md)
  The target of the animation.
### Initializers
- [init(rawValue: String)](./key/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Getting and setting view-animation dictionaries
- [var viewAnimations: [[NSViewAnimation.Key : Any]]](./viewanimations.md)
  The dictionaries defining the objects to animate.
- [NSViewAnimation.EffectName](./effectname.md)
  The following constants specify the animation effect to apply and are used as values for the animation effect property of the animation view. See the description of [`effect`](./key/effect.md) for usage details.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsviewanimation/key)*
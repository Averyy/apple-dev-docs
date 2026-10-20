# NSViewAnimation.EffectName

**Framework**: AppKit  
**Kind**: struct  
**Role**: Structure

The following constants specify the animation effect to apply and are used as values for the animation effect property of the animation view. See the description of [`effect`](./key/effect.md) for usage details.

**Availability**:
- macOS

## Declaration

```swift
struct EffectName
```

```c
typedef NSString * NSViewAnimationEffectName;
```

## Topics

### Effect Names
- [static let fadeIn: NSViewAnimation.EffectName](./effectname/fadein.md)
  Specifies a fade-in type of effect.
- [static let fadeOut: NSViewAnimation.EffectName](./effectname/fadeout.md)
  Specifies a fade-out type of effect.
### Initializers
- [init(rawValue: String)](./effectname/init%28rawvalue%29.md)

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
- [NSViewAnimation.Key](./key.md)
  The following string constants are keys for the dictionaries in the array passed into [`init(viewAnimations:)`](./init%28viewanimations%29.md) and [`viewAnimations`](./viewanimations.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsviewanimation/effectname)*
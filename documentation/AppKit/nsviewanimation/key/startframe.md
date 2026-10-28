# startFrame

**Framework**: AppKit  
**Kind**: property  
**Role**: Type Property

The size and location of the window or view at the start of the animation.

**Availability**:
- macOS

## Declaration

```swift
static let startFrame: NSViewAnimation.Key
```

```c
extern NSViewAnimationKey NSViewAnimationStartFrameKey;
```

## Discussion

The size and location are specified by an [`NSRect`](../../../Foundation/nsrect.md) structure encoded in an [`NSValue`](../../../Foundation/nsvalue.md) object. This property is optional. If it is not specified, `NSViewAnimation` uses the frame of the window or view at the start of the animation.

## See Also

### Keys
- [static let effect: NSViewAnimation.Key](./effect.md)
  An effect to apply to the animation.
- [static let endFrame: NSViewAnimation.Key](./endframe.md)
  The size and location of the window or view at the end of the animation.
- [static let target: NSViewAnimation.Key](./target.md)
  The target of the animation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsviewanimation/key/startframe)*
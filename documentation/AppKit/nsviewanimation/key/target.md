# target

**Framework**: AppKit  
**Kind**: property  
**Role**: Type Property

The target of the animation.

**Availability**:
- macOS

## Declaration

```swift
static let target: NSViewAnimation.Key
```

```c
extern NSViewAnimationKey NSViewAnimationTargetKey;
```

#### Discussion

The target can be either an [`NSView`](../../nsview.md) object or an [`NSWindow`](../../nswindow.md) object. This property is required.

## See Also

### Keys
- [static let effect: NSViewAnimation.Key](./effect.md)
  An effect to apply to the animation.
- [static let endFrame: NSViewAnimation.Key](./endframe.md)
  The size and location of the window or view at the end of the animation.
- [static let startFrame: NSViewAnimation.Key](./startframe.md)
  The size and location of the window or view at the start of the animation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsviewanimation/key/target)*
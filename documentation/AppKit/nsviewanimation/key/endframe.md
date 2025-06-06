# endFrame

**Framework**: AppKit  
**Kind**: property

The size and location of the window or view at the end of the animation.

**Availability**:
- macOS ?+

## Declaration

```swift
static let endFrame: NSViewAnimation.Key
```

#### Discussion

The size and location are specified by an [`NSRect`](https://developer.apple.com/documentation/Foundation/NSRect) structure encoded in an [`NSValue`](https://developer.apple.com/documentation/Foundation/NSValue) object. This property is optional. If it is not specified, `NSViewAnimation` uses the frame of the window or view at the start of the animation. If the target is a view and the end frame is empty, the view is hidden at the end.

## See Also

- [static let effect: NSViewAnimation.Key](nsviewanimation/key/effect.md)
  An effect to apply to the animation.
- [static let startFrame: NSViewAnimation.Key](nsviewanimation/key/startframe.md)
  The size and location of the window or view at the start of the animation.
- [static let target: NSViewAnimation.Key](nsviewanimation/key/target.md)
  The target of the animation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsviewanimation/key/endframe)*
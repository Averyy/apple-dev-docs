# preferredFrameRate

**Framework**: SpriteKit  
**Kind**: property

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var preferredFrameRate: Float { get set }
```

#### Discussion

This function is deprecated. Use [`preferredFramesPerSecond`](skview/preferredframespersecond.md) instead.

## See Also

- [var isPaused: Bool](skview/ispaused.md)
  A Boolean value that indicates whether the view’s scene animations are paused.
- [var preferredFramesPerSecond: Int](skview/preferredframespersecond.md)
  The animation frame rate that the view uses to render its scene.
- [var delegate: (any SKViewDelegate)?](skview/delegate.md)
  A delegate that allows dynamic control of the view’s render rate.
- [protocol SKViewDelegate](skviewdelegate.md)
  Methods to take custom control over the view’s render rate.
- [var frameInterval: Int](skview/frameinterval.md)
  The number of frames that must pass before the scene is called to update its contents.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skview/preferredframerate)*
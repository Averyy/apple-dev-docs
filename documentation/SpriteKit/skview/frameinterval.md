# frameInterval

**Framework**: SpriteKit  
**Kind**: property

The number of frames that must pass before the scene is called to update its contents.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var frameInterval: Int { get set }
```

#### Discussion

The default value is `1`, which results in your game being notified at the refresh rate of the display. If the value is set to a value larger than `1`, the display link notifies your game at a fraction of the native refresh rate. For example, setting the interval to `2` causes the scene to be called every other frame, providing half the frame rate.

Behavior is undefined with a value less than `1`.

This property is deprecated. Use [`preferredFramesPerSecond`](skview/preferredframespersecond.md), or [`view(_:shouldRenderAtTime:)`](skviewdelegate/view(_:shouldrenderattime:).md) instead.

## See Also

- [var isPaused: Bool](skview/ispaused.md)
  A Boolean value that indicates whether the view’s scene animations are paused.
- [var preferredFramesPerSecond: Int](skview/preferredframespersecond.md)
  The animation frame rate that the view uses to render its scene.
- [var delegate: (any SKViewDelegate)?](skview/delegate.md)
  A delegate that allows dynamic control of the view’s render rate.
- [protocol SKViewDelegate](skviewdelegate.md)
  Methods to take custom control over the view’s render rate.
- [var preferredFrameRate: Float](skview/preferredframerate.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skview/frameinterval)*
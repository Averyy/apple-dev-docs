# frameInterval

**Framework**: SpriteKit  
**Kind**: property  
**Role**: Instance Property

The number of frames that must pass before the scene is called to update its contents.

**Availability**:
- iOS 7.0+ - Deprecated in 10.0
- iPadOS 7.0+ - Deprecated in 10.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.8+ - Deprecated in 10.12
- tvOS - Deprecated in 10.0
- visionOS 1.0+ - Deprecated in 1.0

## Declaration

```swift
var frameInterval: Int { get set }
```

```objc
@property (nonatomic) NSInteger frameInterval;
```

## Discussion

The default value is `1`, which results in your game being notified at the refresh rate of the display. If the value is set to a value larger than `1`, the display link notifies your game at a fraction of the native refresh rate. For example, setting the interval to `2` causes the scene to be called every other frame, providing half the frame rate.

Behavior is undefined with a value less than `1`.

This property is deprecated. Use [`preferredFramesPerSecond`](./preferredframespersecond.md), or [`view(_:shouldRenderAtTime:)`](../skviewdelegate/view%28_,shouldrenderattime%29.md) instead.

## See Also

### Controlling the Timing of a Scene’s Rendering
- [var isPaused: Bool](./ispaused.md)
  A Boolean value that indicates whether the view’s scene animations are paused.
- [var preferredFramesPerSecond: Int](./preferredframespersecond.md)
  The animation frame rate that the view uses to render its scene.
- [var delegate: (any SKViewDelegate)?](./delegate.md)
  A delegate that allows dynamic control of the view’s render rate.
- [protocol SKViewDelegate](../skviewdelegate.md)
  Methods to take custom control over the view’s render rate.
- [var preferredFrameRate: Float](./preferredframerate.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skview/frameinterval)*
# preferredFrameRate

**Framework**: SpriteKit  
**Kind**: property  
**Role**: Instance Property

**Availability**:
- iOS 10.0+ - Deprecated in 10.0
- iPadOS 10.0+ - Deprecated in 10.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.12+ - Deprecated in 10.12
- tvOS 10.0+ - Deprecated in 10.0
- visionOS 1.0+ - Deprecated in 1.0

## Declaration

```swift
var preferredFrameRate: Float { get set }
```

```objc
@property (nonatomic) float preferredFrameRate;
```

#### Discussion

This function is deprecated. Use [`preferredFramesPerSecond`](./preferredframespersecond.md) instead.

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
- [var frameInterval: Int](./frameinterval.md)
  The number of frames that must pass before the scene is called to update its contents.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skview/preferredframerate)*
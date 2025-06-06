# preferredFramesPerSecond

**Framework**: SpriteKit  
**Kind**: property

The animation frame rate that the view uses to render its scene.

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
var preferredFramesPerSecond: Int { get set }
```

#### Discussion

When your application sets its preferred frame rate, the view chooses a frame rate as close to that as possible based on the capabilities of the screen the view is displayed on. The actual frame rate chosen is usually a factor of the maximum refresh rate of the screen to provide a consistent frame rate. For example, if the maximum refresh rate of the screen is 60 frames per second, that is also the highest frame rate the view sets as the actual frame rate. However, if you ask for a lower frame rate, the view might choose 30, 20, or 15 frames per second, or another rate, as the actual frame rate.

Your application should choose a frame rate that it can consistently maintain.

The default value is 60 frames per second.

## See Also

- [var isPaused: Bool](skview/ispaused.md)
  A Boolean value that indicates whether the view’s scene animations are paused.
- [var delegate: (any SKViewDelegate)?](skview/delegate.md)
  A delegate that allows dynamic control of the view’s render rate.
- [protocol SKViewDelegate](skviewdelegate.md)
  Methods to take custom control over the view’s render rate.
- [var frameInterval: Int](skview/frameinterval.md)
  The number of frames that must pass before the scene is called to update its contents.
- [var preferredFrameRate: Float](skview/preferredframerate.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skview/preferredframespersecond)*
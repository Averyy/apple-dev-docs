# isPaused

**Framework**: SpriteKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the view’s scene animations are paused.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS

## Declaration

```swift
var isPaused: Bool { get set }
```

```objc
@property (nonatomic, getter=isPaused) BOOL paused;
```

#### Discussion

If the value is [`true`](../../Swift/true.md), the scene’s content is fixed onscreen. No actions are executed and no physics simulation is performed.

When an application moves from an active to an inactive state, [`isPaused`](./ispaused.md) is automatically set to [`true`](../../Swift/true.md). When an application returns to an active state, [`isPaused`](./ispaused.md) is automatically set to its previous value.

## See Also

### Controlling the Timing of a Scene’s Rendering
- [var preferredFramesPerSecond: Int](./preferredframespersecond.md)
  The animation frame rate that the view uses to render its scene.
- [var delegate: (any SKViewDelegate)?](./delegate.md)
  A delegate that allows dynamic control of the view’s render rate.
- [protocol SKViewDelegate](../skviewdelegate.md)
  Methods to take custom control over the view’s render rate.
- [var frameInterval: Int](./frameinterval.md)
  The number of frames that must pass before the scene is called to update its contents.
- [var preferredFrameRate: Float](./preferredframerate.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skview/ispaused)*
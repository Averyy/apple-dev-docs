# isPaused

**Framework**: SpriteKit  
**Kind**: property

A Boolean value that indicates whether the view’s scene animations are paused.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
@MainActor
var isPaused: Bool { get set }
```

#### Discussion

If the value is [`true`](https://developer.apple.com/documentation/swift/true), the scene’s content is fixed onscreen. No actions are executed and no physics simulation is performed.

When an application moves from an active to an inactive state, [`isPaused`](skview/ispaused.md) is automatically set to [`true`](https://developer.apple.com/documentation/swift/true). When an application returns to an active state, [`isPaused`](skview/ispaused.md) is automatically set to its previous value.

## See Also

- [var preferredFramesPerSecond: Int](skview/preferredframespersecond.md)
  The animation frame rate that the view uses to render its scene.
- [var delegate: (any SKViewDelegate)?](skview/delegate.md)
  A delegate that allows dynamic control of the view’s render rate.
- [protocol SKViewDelegate](skviewdelegate.md)
  Methods to take custom control over the view’s render rate.
- [var frameInterval: Int](skview/frameinterval.md)
  The number of frames that must pass before the scene is called to update its contents.
- [var preferredFrameRate: Float](skview/preferredframerate.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skview/ispaused)*
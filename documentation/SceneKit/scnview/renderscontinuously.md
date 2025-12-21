# rendersContinuously

**Framework**: SceneKit  
**Kind**: property

A Boolean value that determines whether the view always renders at its preferred frame rate or only when its visible content changes.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
@MainActor
var rendersContinuously: Bool { get set }
```

#### Discussion

When this value is [`false`](https://developer.apple.com/documentation/Swift/false) (the default), the view redraws its contents only when something in its scene graph change or animates. Use this option to maximize energy efficiency.

If you change this value to [`true`](https://developer.apple.com/documentation/Swift/true), the view redraws itself continually, at the rate specified by the [`preferredFramesPerSecond`](scnview/preferredframespersecond.md) property, regardless of whether content is changing or animating.

## See Also

- [var backgroundColor: NSColor](scnview/backgroundcolor.md)
  The background color of the view.
- [var preferredFramesPerSecond: Int](scnview/preferredframespersecond.md)
  The animation frame rate that the view uses to render its scene.
- [var antialiasingMode: SCNAntialiasingMode](scnview/antialiasingmode.md)
  The antialiasing mode used for rendering the view’s scene.
- [enum SCNAntialiasingMode](scnantialiasingmode.md)
  Modes for antialiased rendering of the view’s scene, used by the [`SCNView`](scnview.md) property.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnview/renderscontinuously)*
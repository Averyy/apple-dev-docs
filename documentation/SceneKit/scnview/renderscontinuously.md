# rendersContinuously

**Framework**: SceneKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that determines whether the view always renders at its preferred frame rate or only when its visible content changes.

**Availability**:
- iOS 8.0+ - Deprecated in 26.0
- iPadOS 8.0+ - Deprecated in 26.0
- Mac Catalyst 13.1+ - Deprecated in 26.0
- macOS 10.8+ - Deprecated in 26.0
- tvOS 9.0+ - Deprecated in 26.0
- visionOS 1.0+ - Deprecated in 26.0
- watchOS 3.0+ - Deprecated in 26.0

## Declaration

```swift
var rendersContinuously: Bool { get set }
```

```objc
@property (nonatomic, assign) BOOL rendersContinuously;
```

## Discussion

When this value is [`false`](../../Swift/false.md) (the default), the view redraws its contents only when something in its scene graph change or animates. Use this option to maximize energy efficiency.

If you change this value to [`true`](../../Swift/true.md), the view redraws itself continually, at the rate specified by the [`preferredFramesPerSecond`](./preferredframespersecond.md) property, regardless of whether content is changing or animating.

## See Also

### Configuring a View
- [var backgroundColor: NSColor](./backgroundcolor.md)
  The background color of the view.
- [var preferredFramesPerSecond: Int](./preferredframespersecond.md)
  The animation frame rate that the view uses to render its scene.
- [var antialiasingMode: SCNAntialiasingMode](./antialiasingmode.md)
  The antialiasing mode used for rendering the view’s scene.
- [enum SCNAntialiasingMode](../scnantialiasingmode.md)
  Modes for antialiased rendering of the view’s scene, used by the [`SCNView`](../scnview.md) property.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnview/renderscontinuously)*
# backgroundColor

**Framework**: SceneKit  
**Kind**: property

The background color of the view.

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
@NSCopying
@MainActor var backgroundColor: NSColor { get set }
```

#### Discussion

SceneKit displays this color behind the contents of the rendered scene. If the scene contents fill the view or if the scene provides its own background using the [`background`](scnscene/background.md) property, the view’s background color may not be visible.

This property’s value must be a color that can be represented using RGBA components.

## See Also

- [var preferredFramesPerSecond: Int](scnview/preferredframespersecond.md)
  The animation frame rate that the view uses to render its scene.
- [var rendersContinuously: Bool](scnview/renderscontinuously.md)
  A Boolean value that determines whether the view always renders at its preferred frame rate or only when its visible content changes.
- [var antialiasingMode: SCNAntialiasingMode](scnview/antialiasingmode.md)
  The antialiasing mode used for rendering the view’s scene.
- [enum SCNAntialiasingMode](scnantialiasingmode.md)
  Modes for antialiased rendering of the view’s scene, used by the [`SCNView`](scnview.md) property.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnview/backgroundcolor)*
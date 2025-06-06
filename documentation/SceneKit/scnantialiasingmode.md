# SCNAntialiasingMode

**Framework**: SceneKit  
**Kind**: enum

Modes for antialiased rendering of the view’s scene, used by the [`SCNView`](scnview.md) property.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
enum SCNAntialiasingMode
```

## Topics

### Constants
- [SCNAntialiasingMode.none](scnantialiasingmode/none.md)
  Disables antialiased rendering.
- [SCNAntialiasingMode.multisampling2X](scnantialiasingmode/multisampling2x.md)
  Enables multisample antialiasing, with two samples per screen pixel.
- [SCNAntialiasingMode.multisampling4X](scnantialiasingmode/multisampling4x.md)
  Enables multisample antialiasing, with four samples per screen pixel.
- [SCNAntialiasingMode.multisampling8X](scnantialiasingmode/multisampling8x.md)
  Enables multisample antialiasing, with eight samples per screen pixel.
- [SCNAntialiasingMode.multisampling16X](scnantialiasingmode/multisampling16x.md)
  Enables multisample antialiasing, with sixteen samples per screen pixel.
### Initializers
- [init?(rawValue: UInt)](scnantialiasingmode/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [var backgroundColor: NSColor](scnview/backgroundcolor.md)
  The background color of the view.
- [var preferredFramesPerSecond: Int](scnview/preferredframespersecond.md)
  The animation frame rate that the view uses to render its scene.
- [var rendersContinuously: Bool](scnview/renderscontinuously.md)
  A Boolean value that determines whether the view always renders at its preferred frame rate or only when its visible content changes.
- [var antialiasingMode: SCNAntialiasingMode](scnview/antialiasingmode.md)
  The antialiasing mode used for rendering the view’s scene.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnantialiasingmode)*
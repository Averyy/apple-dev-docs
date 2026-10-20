# SCNAntialiasingMode

**Framework**: SceneKit  
**Kind**: enum  
**Role**: Enumeration

Modes for antialiased rendering of the view’s scene, used by the [`SCNView`](./scnview.md) property.

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
enum SCNAntialiasingMode
```

```c
enum SCNAntialiasingMode : NSUInteger;
```

## Topics

### Constants
- [SCNAntialiasingMode.none](./scnantialiasingmode/none.md)
  Disables antialiased rendering.
- [SCNAntialiasingMode.multisampling2X](./scnantialiasingmode/multisampling2x.md)
  Enables multisample antialiasing, with two samples per screen pixel.
- [SCNAntialiasingMode.multisampling4X](./scnantialiasingmode/multisampling4x.md)
  Enables multisample antialiasing, with four samples per screen pixel.
- [SCNAntialiasingMode.multisampling8X](./scnantialiasingmode/multisampling8x.md)
  Enables multisample antialiasing, with eight samples per screen pixel.
- [SCNAntialiasingMode.multisampling16X](./scnantialiasingmode/multisampling16x.md)
  Enables multisample antialiasing, with sixteen samples per screen pixel.
### Initializers
- [init?(rawValue: UInt)](./scnantialiasingmode/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Configuring a View
- [var backgroundColor: NSColor](./scnview/backgroundcolor.md)
  The background color of the view.
- [var preferredFramesPerSecond: Int](./scnview/preferredframespersecond.md)
  The animation frame rate that the view uses to render its scene.
- [var rendersContinuously: Bool](./scnview/renderscontinuously.md)
  A Boolean value that determines whether the view always renders at its preferred frame rate or only when its visible content changes.
- [var antialiasingMode: SCNAntialiasingMode](./scnview/antialiasingmode.md)
  The antialiasing mode used for rendering the view’s scene.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnantialiasingmode)*
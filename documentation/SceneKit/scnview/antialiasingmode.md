# antialiasingMode

**Framework**: SceneKit  
**Kind**: property  
**Role**: Instance Property

The antialiasing mode used for rendering the view’s scene.

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
var antialiasingMode: SCNAntialiasingMode { get set }
```

```objc
@property (nonatomic) SCNAntialiasingMode antialiasingMode;
```

#### Discussion

SceneKit can provide antialiasing, which smooths edges in a rendered scene, using a technique called *multisampling*. Multisampling renders each pixel multiple times and combines the results, creating a higher quality image at a performance cost proportional to the number of samples it uses.

For available values, see [`SCNView`](../scnview.md). In macOS, the default mode is [`SCNAntialiasingMode.multisampling4X`](../scnantialiasingmode/multisampling4x.md). In iOS, the default mode is [`SCNAntialiasingMode.none`](../scnantialiasingmode/none.md).

## See Also

### Configuring a View
- [var backgroundColor: NSColor](./backgroundcolor.md)
  The background color of the view.
- [var preferredFramesPerSecond: Int](./preferredframespersecond.md)
  The animation frame rate that the view uses to render its scene.
- [var rendersContinuously: Bool](./renderscontinuously.md)
  A Boolean value that determines whether the view always renders at its preferred frame rate or only when its visible content changes.
- [enum SCNAntialiasingMode](../scnantialiasingmode.md)
  Modes for antialiased rendering of the view’s scene, used by the [`SCNView`](../scnview.md) property.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnview/antialiasingmode)*
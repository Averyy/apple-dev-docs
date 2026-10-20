# readsFromDepthBuffer

**Framework**: SceneKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that determines whether SceneKit uses depth information when rendering the material.

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
var readsFromDepthBuffer: Bool { get set }
```

```objc
@property (nonatomic) BOOL readsFromDepthBuffer;
```

#### Discussion

SceneKit’s rendering process uses a depth buffer to determine the ordering of rendered surfaces relative to the viewer. The default value of this property is [`true`](../../Swift/true.md), specifying that SceneKit compares the depth of each rendered pixel to the corresponding value in its depth buffer when rendering the material. If the pixel is at a greater depth than the corresponding point in the depth buffer, SceneKit does not render the pixel.

Typically, you disable reading from the depth buffer when rendering objects that should always be visible regardless of the already rendered content in the scene—for example, a heads-up display in a game. In such cases, you should also set a high value for the [`renderingOrder`](../scnnode/renderingorder.md) property of the node containing whatever content is to be always visible.

## See Also

### Managing Render Targets
- [var writesToDepthBuffer: Bool](./writestodepthbuffer.md)
  A Boolean value that determines whether SceneKit produces depth information when rendering the material.
- [var colorBufferWriteMask: SCNColorMask](./colorbufferwritemask.md)
- [struct SCNColorMask](../scncolormask.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnmaterial/readsfromdepthbuffer)*
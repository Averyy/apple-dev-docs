# readsFromDepthBuffer

**Framework**: SceneKit  
**Kind**: property

A Boolean value that determines whether SceneKit uses depth information when rendering the material.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
var readsFromDepthBuffer: Bool { get set }
```

#### Discussion

SceneKit’s rendering process uses a depth buffer to determine the ordering of rendered surfaces relative to the viewer. The default value of this property is [`true`](https://developer.apple.com/documentation/swift/true), specifying that SceneKit compares the depth of each rendered pixel to the corresponding value in its depth buffer when rendering the material. If the pixel is at a greater depth than the corresponding point in the depth buffer, SceneKit does not render the pixel.

Typically, you disable reading from the depth buffer when rendering objects that should always be visible regardless of the already rendered content in the scene—for example, a heads-up display in a game. In such cases, you should also set a high value for the [`renderingOrder`](scnnode/renderingorder.md) property of the node containing whatever content is to be always visible.

## See Also

- [var writesToDepthBuffer: Bool](scnmaterial/writestodepthbuffer.md)
  A Boolean value that determines whether SceneKit produces depth information when rendering the material.
- [var colorBufferWriteMask: SCNColorMask](scnmaterial/colorbufferwritemask.md)
- [struct SCNColorMask](scncolormask.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnmaterial/readsfromdepthbuffer)*
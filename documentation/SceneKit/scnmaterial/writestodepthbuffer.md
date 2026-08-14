# writesToDepthBuffer

**Framework**: SceneKit  
**Kind**: property

A Boolean value that determines whether SceneKit produces depth information when rendering the material.

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
var writesToDepthBuffer: Bool { get set }
```

#### Discussion

SceneKit’s rendering process uses a depth buffer to determine the ordering of rendered surfaces relative to the viewer. The default value of this property is [`true`](https://developer.apple.com/documentation/swift/true), specifying that SceneKit saves depth information for each rendered pixel for use by later rendering passes.

Typically, you disable writing to the depth buffer when rendering semitransparent objects, because later stages of the rendering process may require depth information about the opaque objects behind them.

## See Also

- [var readsFromDepthBuffer: Bool](scnmaterial/readsfromdepthbuffer.md)
  A Boolean value that determines whether SceneKit uses depth information when rendering the material.
- [var colorBufferWriteMask: SCNColorMask](scnmaterial/colorbufferwritemask.md)
- [struct SCNColorMask](scncolormask.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnmaterial/writestodepthbuffer)*
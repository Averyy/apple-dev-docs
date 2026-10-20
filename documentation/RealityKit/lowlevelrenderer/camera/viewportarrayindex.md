# viewportArrayIndex

**Framework**: RealityKit  
**Kind**: property  
**Role**: Instance Property

The index into the output viewports and scissor rects arrays for this camera.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
var viewportArrayIndex: Int { get set }
```

#### Discussion

Corresponds to the vertex amplification viewport array index in `MTLRenderCommandEncoder`.

## See Also

### Specifying render targets
- [var renderTargetArrayIndex: Int](./rendertargetarrayindex.md)
  The index into the render target texture array slice for this camera.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowlevelrenderer/camera/viewportarrayindex)*
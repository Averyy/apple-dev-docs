# renderTargetArrayIndex

**Framework**: RealityKit  
**Kind**: property  
**Role**: Instance Property

The index into the render target texture array slice for this camera.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
var renderTargetArrayIndex: Int { get set }
```

## Discussion

Corresponds to `MTLRenderPassDescriptor.renderTargetArrayLength` slices.

## See Also

### Specifying render targets
- [var viewportArrayIndex: Int](./viewportarrayindex.md)
  The index into the output viewports and scissor rects arrays for this camera.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowlevelrenderer/camera/rendertargetarrayindex)*
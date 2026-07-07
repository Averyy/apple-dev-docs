# viewportArrayIndex

**Framework**: RealityKit  
**Kind**: property

The index into the output viewports and scissor rects arrays for this camera.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
var viewportArrayIndex: Int { get set }
```

#### Discussion

Corresponds to the vertex amplification viewport array index in `MTLRenderCommandEncoder`.

## See Also

- [var renderTargetArrayIndex: Int](lowlevelrenderer/camera/rendertargetarrayindex.md)
  The index into the render target texture array slice for this camera.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowlevelrenderer/camera/viewportarrayindex)*
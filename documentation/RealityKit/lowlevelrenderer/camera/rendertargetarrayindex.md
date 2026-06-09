# renderTargetArrayIndex

**Framework**: RealityKit  
**Kind**: property

The index into the render target texture array slice for this camera.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
var renderTargetArrayIndex: Int { get set }
```

#### Discussion

Corresponds to `MTLRenderPassDescriptor.renderTargetArrayLength` slices.

## See Also

- [var viewportArrayIndex: Int](lowlevelrenderer/camera/viewportarrayindex.md)
  The index into the output viewports and scissor rects arrays for this camera.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowlevelrenderer/camera/rendertargetarrayindex)*
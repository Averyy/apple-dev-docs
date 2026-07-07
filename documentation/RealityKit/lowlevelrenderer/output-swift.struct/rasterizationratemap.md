# rasterizationRateMap

**Framework**: RealityKit  
**Kind**: property

The rasterization rate map to use when rendering.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
var rasterizationRateMap: (any MTLRasterizationRateMap)? { get set }
```

#### Discussion

Corresponds to `MTLRenderPassDescriptor.rasterizationRateMap`.

## See Also

- [var viewports: [MTLViewport]?](lowlevelrenderer/output-swift.struct/viewports.md)
  Per-camera viewport rectangles within the render target.
- [var scissorRects: [MTLScissorRect]?](lowlevelrenderer/output-swift.struct/scissorrects.md)
  Per-camera scissor rectangles within the render target.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowlevelrenderer/output-swift.struct/rasterizationratemap)*
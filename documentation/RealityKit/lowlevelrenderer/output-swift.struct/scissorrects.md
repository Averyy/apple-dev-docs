# scissorRects

**Framework**: RealityKit  
**Kind**: property

Per-camera scissor rectangles within the render target.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
var scissorRects: [MTLScissorRect]? { get set }
```

#### Discussion

Corresponds to `MTLRenderCommandEncoder.setScissorRects(_:)`.

## See Also

- [var viewports: [MTLViewport]?](lowlevelrenderer/output-swift.struct/viewports.md)
  Per-camera viewport rectangles within the render target.
- [var rasterizationRateMap: (any MTLRasterizationRateMap)?](lowlevelrenderer/output-swift.struct/rasterizationratemap.md)
  The rasterization rate map to use when rendering.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowlevelrenderer/output-swift.struct/scissorrects)*
# viewports

**Framework**: RealityKit  
**Kind**: property

Per-camera viewport rectangles within the render target.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
var viewports: [MTLViewport]? { get set }
```

#### Discussion

Each entry corresponds to a camera’s `viewportArrayIndex`. Corresponds to `MTLRenderCommandEncoder.setViewports(_:)`.

## See Also

- [var scissorRects: [MTLScissorRect]?](lowlevelrenderer/output-swift.struct/scissorrects.md)
  Per-camera scissor rectangles within the render target.
- [var rasterizationRateMap: (any MTLRasterizationRateMap)?](lowlevelrenderer/output-swift.struct/rasterizationratemap.md)
  The rasterization rate map to use when rendering.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowlevelrenderer/output-swift.struct/viewports)*
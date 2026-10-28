# viewports

**Framework**: RealityKit  
**Kind**: property  
**Role**: Instance Property

Per-camera viewport rectangles within the render target.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
var viewports: [MTLViewport]? { get set }
```

## Discussion

Each entry corresponds to a camera’s `viewportArrayIndex`. Corresponds to `MTLRenderCommandEncoder.setViewports(_:)`.

## See Also

### Setting the viewport
- [var scissorRects: [MTLScissorRect]?](./scissorrects.md)
  Per-camera scissor rectangles within the render target.
- [var rasterizationRateMap: (any MTLRasterizationRateMap)?](./rasterizationratemap.md)
  The rasterization rate map to use when rendering.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowlevelrenderer/output-swift.struct/viewports)*
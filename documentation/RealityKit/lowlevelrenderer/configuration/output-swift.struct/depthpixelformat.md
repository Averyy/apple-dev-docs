# depthPixelFormat

**Framework**: RealityKit  
**Kind**: property  
**Role**: Instance Property

The pixel format of the depth attachment, or `nil` to omit depth.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
var depthPixelFormat: MTLPixelFormat? { get set }
```

## Discussion

Corresponds to `MTLRenderPassDepthAttachmentDescriptor.texture.pixelFormat`.

## See Also

### Specifying pixel formats
- [var colorPixelFormat: MTLPixelFormat?](./colorpixelformat.md)
  The pixel format of the color attachment, or `nil` for depth-only passes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowlevelrenderer/configuration/output-swift.struct/depthpixelformat)*
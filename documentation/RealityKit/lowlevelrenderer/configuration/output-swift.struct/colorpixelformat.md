# colorPixelFormat

**Framework**: RealityKit  
**Kind**: property

The pixel format of the color attachment, or `nil` for depth-only passes.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
var colorPixelFormat: MTLPixelFormat? { get set }
```

#### Discussion

Corresponds to `MTLRenderPassColorAttachmentDescriptor.texture.pixelFormat`.

## See Also

- [var depthPixelFormat: MTLPixelFormat?](lowlevelrenderer/configuration/output-swift.struct/depthpixelformat.md)
  The pixel format of the depth attachment, or `nil` to omit depth.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowlevelrenderer/configuration/output-swift.struct/colorpixelformat)*
# depthPixelFormat

**Framework**: RealityKit  
**Kind**: property

The pixel format of the depth attachment, or `nil` to omit depth.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
var depthPixelFormat: MTLPixelFormat? { get set }
```

#### Discussion

Corresponds to `MTLRenderPassDepthAttachmentDescriptor.texture.pixelFormat`.

## See Also

- [var colorPixelFormat: MTLPixelFormat?](lowlevelrenderer/configuration/output-swift.struct/colorpixelformat.md)
  The pixel format of the color attachment, or `nil` for depth-only passes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowlevelrenderer/configuration/output-swift.struct/depthpixelformat)*
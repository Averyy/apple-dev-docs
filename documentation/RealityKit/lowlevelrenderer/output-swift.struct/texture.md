# LowLevelRenderer.Output.Texture

**Framework**: RealityKit  
**Kind**: struct

A reference to a specific mip level, slice, and depth plane within a Metal texture.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
struct Texture
```

#### Overview

Corresponds to the level/slice/depthPlane parameters on `MTLRenderPassAttachmentDescriptor`.

## Topics

### Creating a texture reference
- [init(texture: any MTLTexture, level: Int, slice: Int, depthPlane: Int)](lowlevelrenderer/output-swift.struct/texture/init(texture:level:slice:depthplane:).md)
  Creates a texture reference with the given texture, mip level, slice, and depth plane.
### Addressing the texture
- [var level: Int](lowlevelrenderer/output-swift.struct/texture/level.md)
  The mipmap level of the texture to use. Corresponds to `MTLRenderPassAttachmentDescriptor.level`.
- [var slice: Int](lowlevelrenderer/output-swift.struct/texture/slice.md)
  The slice of the texture to use. Corresponds to `MTLRenderPassAttachmentDescriptor.slice`.
- [var depthPlane: Int](lowlevelrenderer/output-swift.struct/texture/depthplane.md)
  The depth plane of the texture to use. Corresponds to `MTLRenderPassAttachmentDescriptor.depthPlane`.
### Instance Properties
- [var texture: any MTLTexture](lowlevelrenderer/output-swift.struct/texture/texture.md)
  The underlying Metal texture.

## See Also

- [init(color: LowLevelRenderer.Output.Texture?, depth: LowLevelRenderer.Output.Texture?)](lowlevelrenderer/output-swift.struct/init(color:depth:).md)
  Creates an output configuration with the given color and depth texture targets.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowlevelrenderer/output-swift.struct/texture)*
# LowLevelRenderer.Output.Texture

**Framework**: RealityKit  
**Kind**: struct  
**Role**: Structure

A reference to a specific mip level, slice, and depth plane within a Metal texture.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
struct Texture
```

## Overview

Corresponds to the level/slice/depthPlane parameters on `MTLRenderPassAttachmentDescriptor`.

## Topics

### Creating a texture reference
- [init(texture: any MTLTexture, level: Int, slice: Int, depthPlane: Int)](./texture/init%28texture,level,slice,depthplane%29.md)
  Creates a texture reference with the given texture, mip level, slice, and depth plane.
### Addressing the texture
- [var level: Int](./texture/level.md)
  The mipmap level of the texture to use. Corresponds to `MTLRenderPassAttachmentDescriptor.level`.
- [var slice: Int](./texture/slice.md)
  The slice of the texture to use. Corresponds to `MTLRenderPassAttachmentDescriptor.slice`.
- [var depthPlane: Int](./texture/depthplane.md)
  The depth plane of the texture to use. Corresponds to `MTLRenderPassAttachmentDescriptor.depthPlane`.
### Instance Properties
- [var texture: any MTLTexture](./texture/texture.md)
  The underlying Metal texture.

## See Also

### Creating an output
- [init(color: LowLevelRenderer.Output.Texture?, depth: LowLevelRenderer.Output.Texture?)](./init%28color,depth%29.md)
  Creates an output configuration with the given color and depth texture targets.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowlevelrenderer/output-swift.struct/texture)*
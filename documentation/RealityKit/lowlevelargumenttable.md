# LowLevelArgumentTable

**Framework**: RealityKit  
**Kind**: class

A table of buffer slices and textures bound to a single shader function.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
final class LowLevelArgumentTable
```

#### Overview

A `LowLevelArgumentTable` binds a set of `LowLevelBufferSlice` and `LowLevelTextureResource` objects at indexed slots. Its layout is described by an `LowLevelArgumentTable.Descriptor` that must match the `argumentTableDescriptor` on the corresponding material function.

Create a `LowLevelArgumentTable` using [`makeArgumentTable(descriptor:buffers:textures:)`](lowlevelrendercontext/makeargumenttable(descriptor:buffers:textures:).md).

## Topics

### Inspecting the table
- [var descriptor: LowLevelArgumentTable.Descriptor](lowlevelargumenttable/descriptor-swift.property.md)
  The descriptor that describes the buffer and texture slots of this argument table.
- [LowLevelArgumentTable.Descriptor](lowlevelargumenttable/descriptor-swift.struct.md)
  The buffer and texture slot configuration for an argument table.
### Accessing textures
- [func texture(at: Int) -> LowLevelTextureResource?](lowlevelargumenttable/texture(at:).md)
  Returns the texture bound at the given index, or `nil` if the slot is unset.
- [func setTexture(LowLevelTextureResource, at: Int) throws(LowLevelRenderContextError)](lowlevelargumenttable/settexture(_:at:).md)
  Binds a texture to the slot at the given index.
### Accessing buffer slices
- [func bufferSlice(at: Int) -> LowLevelBufferSlice?](lowlevelargumenttable/bufferslice(at:).md)
  Returns the buffer slice bound at the given index, or `nil` if the slot is unset.
- [func setBufferSlice(LowLevelBufferSlice, at: Int) throws(LowLevelRenderContextError)](lowlevelargumenttable/setbufferslice(_:at:).md)
  Binds a buffer slice to the slot at the given index.

## See Also

- [class LowLevelRenderPipelineState](lowlevelrenderpipelinestate.md)
  A compiled Metal render pipeline state for a specific mesh descriptor, material, and render target configuration.
- [class LowLevelRenderTarget](lowlevelrendertarget.md)
  An object that describes the pixel format configuration for a render pass’s color and depth attachments.
- [struct LowLevelMaterialParameterMapping](lowlevelmaterialparametermapping.md)
  A mapping of named buffer and texture parameters to binding indices for a compiled shader function.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowlevelargumenttable)*
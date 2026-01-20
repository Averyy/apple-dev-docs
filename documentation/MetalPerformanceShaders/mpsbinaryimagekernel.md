# MPSBinaryImageKernel

**Framework**: Metal Performance Shaders  
**Kind**: class

A kernel that consumes two textures and produces one texture.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.0+
- macOS 10.13+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
class MPSBinaryImageKernel
```

## Mentions

- [The MPSKernel Class](the-mpskernel-class.md)

#### Overview

[`MPSBinaryImageKernel`](mpsbinaryimagekernel.md) defines shared behavior for most image processing kernels (filters) such as edging modes, clipping, and tiling support for image operations that consume two source textures. It is not meant to be used directly, but provides API abstraction and in some cases may allow some level of polymorphic manipulation of image kernel objects.

## Topics

### Initializers
- [init?(coder: NSCoder, device: any MTLDevice)](mpsbinaryimagekernel/init(coder:device:).md)
- [init(device: any MTLDevice)](mpsbinaryimagekernel/init(device:).md)
### Methods
- [func encode(commandBuffer: any MTLCommandBuffer, primaryTexture: any MTLTexture, inPlaceSecondaryTexture: UnsafeMutablePointer<any MTLTexture>, fallbackCopyAllocator: MPSCopyAllocator?) -> Bool](mpsbinaryimagekernel/encode(commandbuffer:primarytexture:inplacesecondarytexture:fallbackcopyallocator:).md)
  This method attempts to apply a kernel in place on a texture.
- [func encode(commandBuffer: any MTLCommandBuffer, inPlacePrimaryTexture: UnsafeMutablePointer<any MTLTexture>, secondaryTexture: any MTLTexture, fallbackCopyAllocator: MPSCopyAllocator?) -> Bool](mpsbinaryimagekernel/encode(commandbuffer:inplaceprimarytexture:secondarytexture:fallbackcopyallocator:).md)
  This method attempts to apply a kernel in place on a texture.
- [func encode(commandBuffer: any MTLCommandBuffer, primaryTexture: any MTLTexture, secondaryTexture: any MTLTexture, destinationTexture: any MTLTexture)](mpsbinaryimagekernel/encode(commandbuffer:primarytexture:secondarytexture:destinationtexture:).md)
  Encodes a kernel into a command buffer, out-of-place.
- [func encode(commandBuffer: any MTLCommandBuffer, primaryImage: MPSImage, secondaryImage: MPSImage, destinationImage: MPSImage)](mpsbinaryimagekernel/encode(commandbuffer:primaryimage:secondaryimage:destinationimage:).md)
- [func primarySourceRegion(forDestinationSize: MTLSize) -> MPSRegion](mpsbinaryimagekernel/primarysourceregion(fordestinationsize:).md)
  Determines the region of the primary source texture that will be read for an encode operation.
- [func secondarySourceRegion(forDestinationSize: MTLSize) -> MPSRegion](mpsbinaryimagekernel/secondarysourceregion(fordestinationsize:).md)
  Determines the region of the secondary source texture that will be read for an encode operation.
### Properties
- [var primaryOffset: MPSOffset](mpsbinaryimagekernel/primaryoffset.md)
  The position of the destination clip rectangle origin relative to the primary source buffer.
- [var secondaryOffset: MPSOffset](mpsbinaryimagekernel/secondaryoffset.md)
  The position of the destination clip rectangle origin relative to the secondary source buffer.
- [var primaryEdgeMode: MPSImageEdgeMode](mpsbinaryimagekernel/primaryedgemode.md)
  The edge mode to use when texture reads stray off the edge of the primary source image.
- [var secondaryEdgeMode: MPSImageEdgeMode](mpsbinaryimagekernel/secondaryedgemode.md)
  The edge mode to use when texture reads stray off the edge of the secondary source image.
- [var clipRect: MTLRegion](mpsbinaryimagekernel/cliprect.md)
  An optional clip rectangle to use when writing data. Only the pixels in the rectangle will be overwritten.

## Relationships

### Inherits From
- [MPSKernel](mpskernel.md)
### Inherited By
- [MPSImageArithmetic](mpsimagearithmetic.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)

## See Also

- [class MPSUnaryImageKernel](mpsunaryimagekernel.md)
  A kernel that consumes one texture and produces one texture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsbinaryimagekernel)*
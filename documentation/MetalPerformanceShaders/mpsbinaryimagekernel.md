# MPSBinaryImageKernel

**Framework**: Metal Performance Shaders  
**Kind**: class  
**Role**: Class

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

```objc
@interface MPSBinaryImageKernel : MPSKernel
```

## Mentions

- [The MPSKernel Class](./the-mpskernel-class.md)

## Overview

[`MPSBinaryImageKernel`](./mpsbinaryimagekernel.md) defines shared behavior for most image processing kernels (filters) such as edging modes, clipping, and tiling support for image operations that consume two source textures. It is not meant to be used directly, but provides API abstraction and in some cases may allow some level of polymorphic manipulation of image kernel objects.

## Topics

### Initializers
- [init?(coder: NSCoder, device: any MTLDevice)](./mpsbinaryimagekernel/init%28coder,device%29.md)
- [init(device: any MTLDevice)](./mpsbinaryimagekernel/init%28device%29.md)
### Methods
- [func encode(commandBuffer: any MTLCommandBuffer, primaryTexture: any MTLTexture, inPlaceSecondaryTexture: UnsafeMutablePointer<any MTLTexture>, fallbackCopyAllocator: MPSCopyAllocator?) -> Bool](./mpsbinaryimagekernel/encode%28commandbuffer,primarytexture,inplacesecondarytexture,fallbackcopyallocator%29.md)
  This method attempts to apply a kernel in place on a texture.
- [func encode(commandBuffer: any MTLCommandBuffer, inPlacePrimaryTexture: UnsafeMutablePointer<any MTLTexture>, secondaryTexture: any MTLTexture, fallbackCopyAllocator: MPSCopyAllocator?) -> Bool](./mpsbinaryimagekernel/encode%28commandbuffer,inplaceprimarytexture,secondarytexture,fallbackcopyallocator%29.md)
  This method attempts to apply a kernel in place on a texture.
- [func encode(commandBuffer: any MTLCommandBuffer, primaryTexture: any MTLTexture, secondaryTexture: any MTLTexture, destinationTexture: any MTLTexture)](./mpsbinaryimagekernel/encode%28commandbuffer,primarytexture,secondarytexture,destinationtexture%29.md)
  Encodes a kernel into a command buffer, out-of-place.
- [func encode(commandBuffer: any MTLCommandBuffer, primaryImage: MPSImage, secondaryImage: MPSImage, destinationImage: MPSImage)](./mpsbinaryimagekernel/encode%28commandbuffer,primaryimage,secondaryimage,destinationimage%29.md)
- [func primarySourceRegion(forDestinationSize: MTLSize) -> MPSRegion](./mpsbinaryimagekernel/primarysourceregion%28fordestinationsize%29.md)
  Determines the region of the primary source texture that will be read for an encode operation.
- [func secondarySourceRegion(forDestinationSize: MTLSize) -> MPSRegion](./mpsbinaryimagekernel/secondarysourceregion%28fordestinationsize%29.md)
  Determines the region of the secondary source texture that will be read for an encode operation.
### Properties
- [var primaryOffset: MPSOffset](./mpsbinaryimagekernel/primaryoffset.md)
  The position of the destination clip rectangle origin relative to the primary source buffer.
- [var secondaryOffset: MPSOffset](./mpsbinaryimagekernel/secondaryoffset.md)
  The position of the destination clip rectangle origin relative to the secondary source buffer.
- [var primaryEdgeMode: MPSImageEdgeMode](./mpsbinaryimagekernel/primaryedgemode.md)
  The edge mode to use when texture reads stray off the edge of the primary source image.
- [var secondaryEdgeMode: MPSImageEdgeMode](./mpsbinaryimagekernel/secondaryedgemode.md)
  The edge mode to use when texture reads stray off the edge of the secondary source image.
- [var clipRect: MTLRegion](./mpsbinaryimagekernel/cliprect.md)
  An optional clip rectangle to use when writing data. Only the pixels in the rectangle will be overwritten.

## Relationships

### Inherits From
- [MPSKernel](./mpskernel.md)
### Inherited By
- [MPSImageArithmetic](./mpsimagearithmetic.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)

## See Also

### Image Filter Base Classes
- [class MPSUnaryImageKernel](./mpsunaryimagekernel.md)
  A kernel that consumes one texture and produces one texture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsbinaryimagekernel)*
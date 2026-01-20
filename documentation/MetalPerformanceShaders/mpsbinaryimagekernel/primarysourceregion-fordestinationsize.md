# primarySourceRegion(forDestinationSize:)

**Framework**: Metal Performance Shaders  
**Kind**: method

Determines the region of the primary source texture that will be read for an encode operation.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.0+
- macOS 10.13+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func primarySourceRegion(forDestinationSize destinationSize: MTLSize) -> MPSRegion
```

#### Return Value

The area in the virtual source image that will be read.

#### Discussion

This method is used to determine which region of the primary source texture will be read by the [`encode(commandBuffer:primaryTexture:secondaryTexture:destinationTexture:)`](mpsbinaryimagekernel/encode(commandbuffer:primarytexture:secondarytexture:destinationtexture:).md) method when the filter runs. This information may be needed if the primary source image is broken into multiple textures. The size of the full (untiled) destination image is provided. The region of the full (untiled) source image that will be read is returned. You can then piece together an appropriate texture containing that information for use in your tiled context.

This method will consult the [`primaryOffset`](mpsbinaryimagekernel/primaryoffset.md) and [`clipRect`](mpsbinaryimagekernel/cliprect.md) properties to determine the full region read by the function. Other properties, such as kernel height and width, will be consulted as necessary. All properties should be set to their intended values prior to calling this method.

> ❗ **Important**:  This function operates using global image coordinates, but the [`encode(commandBuffer:primaryTexture:secondaryTexture:destinationTexture:)`](mpsbinaryimagekernel/encode(commandbuffer:primarytexture:secondarytexture:destinationtexture:).md) method uses coordinates local to the source and destination image textures. Consequently, the [`primaryOffset`](mpsbinaryimagekernel/primaryoffset.md) and [`clipRect`](mpsbinaryimagekernel/cliprect.md) properties attached to this object will need to be updated using a global-to-local coordinate transform before the [`encode(commandBuffer:primaryTexture:secondaryTexture:destinationTexture:)`](mpsbinaryimagekernel/encode(commandbuffer:primarytexture:secondarytexture:destinationtexture:).md) method is called.

## Parameters

- `destinationSize`: The size of the full virtual destination image.

## See Also

- [func encode(commandBuffer: any MTLCommandBuffer, primaryTexture: any MTLTexture, inPlaceSecondaryTexture: UnsafeMutablePointer<any MTLTexture>, fallbackCopyAllocator: MPSCopyAllocator?) -> Bool](mpsbinaryimagekernel/encode(commandbuffer:primarytexture:inplacesecondarytexture:fallbackcopyallocator:).md)
  This method attempts to apply a kernel in place on a texture.
- [func encode(commandBuffer: any MTLCommandBuffer, inPlacePrimaryTexture: UnsafeMutablePointer<any MTLTexture>, secondaryTexture: any MTLTexture, fallbackCopyAllocator: MPSCopyAllocator?) -> Bool](mpsbinaryimagekernel/encode(commandbuffer:inplaceprimarytexture:secondarytexture:fallbackcopyallocator:).md)
  This method attempts to apply a kernel in place on a texture.
- [func encode(commandBuffer: any MTLCommandBuffer, primaryTexture: any MTLTexture, secondaryTexture: any MTLTexture, destinationTexture: any MTLTexture)](mpsbinaryimagekernel/encode(commandbuffer:primarytexture:secondarytexture:destinationtexture:).md)
  Encodes a kernel into a command buffer, out-of-place.
- [func encode(commandBuffer: any MTLCommandBuffer, primaryImage: MPSImage, secondaryImage: MPSImage, destinationImage: MPSImage)](mpsbinaryimagekernel/encode(commandbuffer:primaryimage:secondaryimage:destinationimage:).md)
- [func secondarySourceRegion(forDestinationSize: MTLSize) -> MPSRegion](mpsbinaryimagekernel/secondarysourceregion(fordestinationsize:).md)
  Determines the region of the secondary source texture that will be read for an encode operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsbinaryimagekernel/primarysourceregion(fordestinationsize:))*
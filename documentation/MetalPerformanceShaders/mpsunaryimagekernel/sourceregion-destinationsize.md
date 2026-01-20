# sourceRegion(destinationSize:)

**Framework**: Metal Performance Shaders  
**Kind**: method

Determines the region of the source texture that will be read for an encode operation.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.0+
- macOS 10.13+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func sourceRegion(destinationSize: MTLSize) -> MPSRegion
```

## Mentions

- [Tuning Hints](tuning-hints.md)

#### Return Value

The area in the virtual source image that will be read.

#### Discussion

This method is used to determine which region of the source texture will be read by the [`encode(commandBuffer:sourceTexture:destinationTexture:)`](mpsunaryimagekernel/encode(commandbuffer:sourcetexture:destinationtexture:).md) method when the filter runs. This information may be needed if the source image is broken into multiple textures. The size of the full (untiled) destination image is provided. The region of the full (untiled) source image that will be read is returned. You can then piece together an appropriate texture containing that information for use in your tiled context.

This method will consult the [`offset`](mpsunaryimagekernel/offset.md) and [`clipRect`](mpsunaryimagekernel/cliprect.md) properties to determine the full region read by the function. Other properties, such as kernel height and width, will be consulted as necessary. All properties should be set to their intended values prior to calling this method.

> ❗ **Important**:  This function operates using global image coordinates, but the [`encode(commandBuffer:sourceTexture:destinationTexture:)`](mpsunaryimagekernel/encode(commandbuffer:sourcetexture:destinationtexture:).md) method uses coordinates local to the source and destination image textures. Consequently, the [`offset`](mpsunaryimagekernel/offset.md) and [`clipRect`](mpsunaryimagekernel/cliprect.md) properties attached to this object will need to be updated using a global-to-local coordinate transform before the [`encode(commandBuffer:sourceTexture:destinationTexture:)`](mpsunaryimagekernel/encode(commandbuffer:sourcetexture:destinationtexture:).md) method is called.

## Parameters

- `destinationSize`: The size of the full virtual destination image.

## See Also

- [func encode(commandBuffer: any MTLCommandBuffer, inPlaceTexture: UnsafeMutablePointer<any MTLTexture>, fallbackCopyAllocator: MPSCopyAllocator?) -> Bool](mpsunaryimagekernel/encode(commandbuffer:inplacetexture:fallbackcopyallocator:).md)
  This method attempts to apply a kernel in place on a texture.
- [typealias MPSCopyAllocator](mpscopyallocator.md)
  A block to make a copy of a source texture for filters that can only execute out of place.
- [func encode(commandBuffer: any MTLCommandBuffer, sourceImage: MPSImage, destinationImage: MPSImage)](mpsunaryimagekernel/encode(commandbuffer:sourceimage:destinationimage:).md)
- [func encode(commandBuffer: any MTLCommandBuffer, sourceTexture: any MTLTexture, destinationTexture: any MTLTexture)](mpsunaryimagekernel/encode(commandbuffer:sourcetexture:destinationtexture:).md)
  Encodes a kernel into a command buffer, out of place.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsunaryimagekernel/sourceregion(destinationsize:))*
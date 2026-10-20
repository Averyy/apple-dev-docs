# encode(commandBuffer:primaryImage:secondaryImage:destinationImage:)

**Framework**: Metal Performance Shaders  
**Kind**: method  
**Role**: Instance Method

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.0+
- macOS 10.13+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func encode(commandBuffer: any MTLCommandBuffer, primaryImage: MPSImage, secondaryImage: MPSImage, destinationImage: MPSImage)
```

```objc
- (void) encodeToCommandBuffer:(id<MTLCommandBuffer>) commandBuffer primaryImage:(MPSImage *) primaryImage secondaryImage:(MPSImage *) secondaryImage destinationImage:(MPSImage *) destinationImage;
```

## See Also

### Methods
- [func encode(commandBuffer: any MTLCommandBuffer, primaryTexture: any MTLTexture, inPlaceSecondaryTexture: UnsafeMutablePointer<any MTLTexture>, fallbackCopyAllocator: MPSCopyAllocator?) -> Bool](./encode%28commandbuffer,primarytexture,inplacesecondarytexture,fallbackcopyallocator%29.md)
  This method attempts to apply a kernel in place on a texture.
- [func encode(commandBuffer: any MTLCommandBuffer, inPlacePrimaryTexture: UnsafeMutablePointer<any MTLTexture>, secondaryTexture: any MTLTexture, fallbackCopyAllocator: MPSCopyAllocator?) -> Bool](./encode%28commandbuffer,inplaceprimarytexture,secondarytexture,fallbackcopyallocator%29.md)
  This method attempts to apply a kernel in place on a texture.
- [func encode(commandBuffer: any MTLCommandBuffer, primaryTexture: any MTLTexture, secondaryTexture: any MTLTexture, destinationTexture: any MTLTexture)](./encode%28commandbuffer,primarytexture,secondarytexture,destinationtexture%29.md)
  Encodes a kernel into a command buffer, out-of-place.
- [func primarySourceRegion(forDestinationSize: MTLSize) -> MPSRegion](./primarysourceregion%28fordestinationsize%29.md)
  Determines the region of the primary source texture that will be read for an encode operation.
- [func secondarySourceRegion(forDestinationSize: MTLSize) -> MPSRegion](./secondarysourceregion%28fordestinationsize%29.md)
  Determines the region of the secondary source texture that will be read for an encode operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsbinaryimagekernel/encode(commandbuffer:primaryimage:secondaryimage:destinationimage:))*
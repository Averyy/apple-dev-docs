# encode(commandBuffer:primaryTexture:secondaryTexture:destinationTexture:)

**Framework**: Metal Performance Shaders  
**Kind**: method  
**Role**: Instance Method

Encodes a kernel into a command buffer, out-of-place.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.0+
- macOS 10.13+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func encode(commandBuffer: any MTLCommandBuffer, primaryTexture: any MTLTexture, secondaryTexture: any MTLTexture, destinationTexture: any MTLTexture)
```

```objc
- (void) encodeToCommandBuffer:(id<MTLCommandBuffer>) commandBuffer primaryTexture:(id<MTLTexture>) primaryTexture secondaryTexture:(id<MTLTexture>) secondaryTexture destinationTexture:(id<MTLTexture>) destinationTexture;
```

## Parameters

- `commandBuffer`: A valid command buffer to receive the encoded kernel.
- `primaryTexture`: A valid texture containing the primary source image.
- `secondaryTexture`: A valid texture containing the secondary source image.
- `destinationTexture`: A valid texture to be overwritten by the result image. `destinationTexture` may not alias `primaryTexture` nor `secondaryTexture`.

## See Also

### Methods
- [func encode(commandBuffer: any MTLCommandBuffer, primaryTexture: any MTLTexture, inPlaceSecondaryTexture: UnsafeMutablePointer<any MTLTexture>, fallbackCopyAllocator: MPSCopyAllocator?) -> Bool](./encode%28commandbuffer,primarytexture,inplacesecondarytexture,fallbackcopyallocator%29.md)
  This method attempts to apply a kernel in place on a texture.
- [func encode(commandBuffer: any MTLCommandBuffer, inPlacePrimaryTexture: UnsafeMutablePointer<any MTLTexture>, secondaryTexture: any MTLTexture, fallbackCopyAllocator: MPSCopyAllocator?) -> Bool](./encode%28commandbuffer,inplaceprimarytexture,secondarytexture,fallbackcopyallocator%29.md)
  This method attempts to apply a kernel in place on a texture.
- [func encode(commandBuffer: any MTLCommandBuffer, primaryImage: MPSImage, secondaryImage: MPSImage, destinationImage: MPSImage)](./encode%28commandbuffer,primaryimage,secondaryimage,destinationimage%29.md)
- [func primarySourceRegion(forDestinationSize: MTLSize) -> MPSRegion](./primarysourceregion%28fordestinationsize%29.md)
  Determines the region of the primary source texture that will be read for an encode operation.
- [func secondarySourceRegion(forDestinationSize: MTLSize) -> MPSRegion](./secondarysourceregion%28fordestinationsize%29.md)
  Determines the region of the secondary source texture that will be read for an encode operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsbinaryimagekernel/encode(commandbuffer:primarytexture:secondarytexture:destinationtexture:))*
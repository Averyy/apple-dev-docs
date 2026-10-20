# encode(commandBuffer:sourceTexture:destinationTexture:)

**Framework**: Metal Performance Shaders  
**Kind**: method  
**Role**: Instance Method

Encodes a kernel into a command buffer, out of place.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.0+
- macOS 10.13+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func encode(commandBuffer: any MTLCommandBuffer, sourceTexture: any MTLTexture, destinationTexture: any MTLTexture)
```

```objc
- (void) encodeToCommandBuffer:(id<MTLCommandBuffer>) commandBuffer sourceTexture:(id<MTLTexture>) sourceTexture destinationTexture:(id<MTLTexture>) destinationTexture;
```

## Parameters

- `commandBuffer`: A valid command buffer to receive the encoded kernel.
- `sourceTexture`: A valid texture containing the source image.
- `destinationTexture`: A valid texture to be overwritten by the result image. `destinationTexture` may not alias `sourceTexture`.

## See Also

### Methods
- [func encode(commandBuffer: any MTLCommandBuffer, inPlaceTexture: UnsafeMutablePointer<any MTLTexture>, fallbackCopyAllocator: MPSCopyAllocator?) -> Bool](./encode%28commandbuffer,inplacetexture,fallbackcopyallocator%29.md)
  This method attempts to apply a kernel in place on a texture.
- [typealias MPSCopyAllocator](../mpscopyallocator.md)
  A block to make a copy of a source texture for filters that can only execute out of place.
- [func encode(commandBuffer: any MTLCommandBuffer, sourceImage: MPSImage, destinationImage: MPSImage)](./encode%28commandbuffer,sourceimage,destinationimage%29.md)
- [func sourceRegion(destinationSize: MTLSize) -> MPSRegion](./sourceregion%28destinationsize%29.md)
  Determines the region of the source texture that will be read for an encode operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsunaryimagekernel/encode(commandbuffer:sourcetexture:destinationtexture:))*
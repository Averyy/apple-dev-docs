# encode(commandBuffer:inPlacePrimaryTexture:secondaryTexture:fallbackCopyAllocator:)

**Framework**: Metal Performance Shaders  
**Kind**: method  
**Role**: Instance Method

This method attempts to apply a kernel in place on a texture.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.0+
- macOS 10.13+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func encode(commandBuffer: any MTLCommandBuffer, inPlacePrimaryTexture: UnsafeMutablePointer<any MTLTexture>, secondaryTexture: any MTLTexture, fallbackCopyAllocator copyAllocator: MPSCopyAllocator? = nil) -> Bool
```

```objc
- (BOOL) encodeToCommandBuffer:(id<MTLCommandBuffer>) commandBuffer inPlacePrimaryTexture:(id<MTLTexture>*) inPlacePrimaryTexture secondaryTexture:(id<MTLTexture>) secondaryTexture fallbackCopyAllocator:(MPSCopyAllocator) copyAllocator;
```

#### Return Value

[`true`](../../Swift/true.md) if the operation succeeded (the texture may have been replaced with a new texture if a copy allocator was provided). [`false`](../../Swift/false.md) if the operation failed (the texture is unmodified).

#### Discussion

This method attempts to apply the kernel in place on a texture. In-place operation means that the same texture is used both to hold the input image and the results. Operating in-place can be an excellent way to reduce resource utilization, and save time and energy. While simple Metal kernels can not operate in place because textures can not be readable and writable at the same time, some Metal Performance Shaders kernels can operate in place because they use multi-pass algorithms. Whether a kernel can operate in-place can depend on current hardware, OS version, and the parameters and properties passed to it. You should never assume that a kernel will continue to work in place, even if you have observed it doing so before.

If the in-place operation succeeds, this method returns [`true`](../../Swift/true.md). If the in-place operation fails and no copy allocator is provided, then this method returns [`false`](../../Swift/false.md). Without a fallback copy allocator, in neither case is the pointer held at `texture` modified.

Failure during in-place operation is common. You may find it simplifies your code to provide a copy allocator. When an in-place operation fails, your copy allocator will be invoked to create a new texture in which to write the results, allowing the kernel to proceed reliably out-of-place. The original texture will be released, replaced with a pointer to the new texture and [`true`](../../Swift/true.md) will be returned. If the copy allocator returns an invalid texture, it is released, `texture` remains unmodified, and [`false`](../../Swift/false.md) is returned.

## Parameters

- `commandBuffer`: A valid command buffer to receive the encoded kernel.
- `inPlacePrimaryTexture`: A pointer to a valid texture containing the primary image. On success, the image contents and possibly the texture itself will be replaced with the result image.
- `secondaryTexture`: A pointer to a valid texture containing the secondary source image. It will not be overwritten.
- `copyAllocator`: An optional block to allocate a new texture to hold the operation results, in case in-place operation is not possible. The allocator may use a different pixel format or size than the original texture. You may enqueue operations on the provided command buffer using the provided compute command encoder to initialize the texture contents.

## See Also

### Related Documentation
- [typealias MPSCopyAllocator](../mpscopyallocator.md)
  A block to make a copy of a source texture for filters that can only execute out of place.
### Methods
- [func encode(commandBuffer: any MTLCommandBuffer, primaryTexture: any MTLTexture, inPlaceSecondaryTexture: UnsafeMutablePointer<any MTLTexture>, fallbackCopyAllocator: MPSCopyAllocator?) -> Bool](./encode%28commandbuffer,primarytexture,inplacesecondarytexture,fallbackcopyallocator%29.md)
  This method attempts to apply a kernel in place on a texture.
- [func encode(commandBuffer: any MTLCommandBuffer, primaryTexture: any MTLTexture, secondaryTexture: any MTLTexture, destinationTexture: any MTLTexture)](./encode%28commandbuffer,primarytexture,secondarytexture,destinationtexture%29.md)
  Encodes a kernel into a command buffer, out-of-place.
- [func encode(commandBuffer: any MTLCommandBuffer, primaryImage: MPSImage, secondaryImage: MPSImage, destinationImage: MPSImage)](./encode%28commandbuffer,primaryimage,secondaryimage,destinationimage%29.md)
- [func primarySourceRegion(forDestinationSize: MTLSize) -> MPSRegion](./primarysourceregion%28fordestinationsize%29.md)
  Determines the region of the primary source texture that will be read for an encode operation.
- [func secondarySourceRegion(forDestinationSize: MTLSize) -> MPSRegion](./secondarysourceregion%28fordestinationsize%29.md)
  Determines the region of the secondary source texture that will be read for an encode operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsbinaryimagekernel/encode(commandbuffer:inplaceprimarytexture:secondarytexture:fallbackcopyallocator:))*
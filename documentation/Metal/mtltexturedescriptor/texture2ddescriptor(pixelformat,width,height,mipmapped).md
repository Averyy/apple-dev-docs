# texture2DDescriptor(pixelFormat:width:height:mipmapped:)

**Framework**: Metal  
**Kind**: method  
**Role**: Type Method

Creates a texture descriptor object for a 2D texture.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS
- visionOS 1.0+

## Declaration

```swift
class func texture2DDescriptor(pixelFormat: MTLPixelFormat, width: Int, height: Int, mipmapped: Bool) -> MTLTextureDescriptor
```

```objc
+ (MTLTextureDescriptor *) texture2DDescriptorWithPixelFormat:(MTLPixelFormat) pixelFormat width:(NSUInteger) width height:(NSUInteger) height mipmapped:(BOOL) mipmapped;
```

## Return Value

A pointer to a texture descriptor object for a 2D texture.

## Parameters

- `pixelFormat`: The format describing how every pixel on the texture image is stored. The default value is [`MTLPixelFormat.rgba8Unorm`](../mtlpixelformat/rgba8unorm.md).
- `width`: The width of the 2D texture image. The value needs to be greater than or equal to `1`.
- `height`: The height of the 2D texture image. The value needs to be greater than or equal to `1`.
- `mipmapped`: A Boolean indicating whether the resulting image should be mipmapped. If [`true`](../../Swift/true.md), then the [`mipmapLevelCount`](./mipmaplevelcount.md) property in the returned descriptor is computed from `width` and `height`. If [`false`](../../Swift/false.md), then [`mipmapLevelCount`](./mipmaplevelcount.md) is `1`.

## See Also

### Related Documentation
- [Metal Shading Language Guide](https://developer.apple.com/library/archive/documentation/Metal/Reference/MetalShadingLanguageGuide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40014364)
- [Metal Programming Guide](https://developer.apple.com/library/archive/documentation/Miscellaneous/Conceptual/MetalProgrammingGuide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40014221)
### Creating texture descriptors
- [class func textureCubeDescriptor(pixelFormat: MTLPixelFormat, size: Int, mipmapped: Bool) -> MTLTextureDescriptor](./texturecubedescriptor%28pixelformat,size,mipmapped%29.md)
  Creates a texture descriptor object for a cube texture.
- [class func textureBufferDescriptor(with: MTLPixelFormat, width: Int, resourceOptions: MTLResourceOptions, usage: MTLTextureUsage) -> MTLTextureDescriptor](./texturebufferdescriptor%28with,width,resourceoptions,usage%29.md)
  Creates a texture descriptor object for a texture buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtltexturedescriptor/texture2ddescriptor(pixelformat:width:height:mipmapped:))*
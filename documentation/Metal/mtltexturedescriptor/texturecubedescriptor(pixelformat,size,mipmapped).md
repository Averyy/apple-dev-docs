# textureCubeDescriptor(pixelFormat:size:mipmapped:)

**Framework**: Metal  
**Kind**: method  
**Role**: Type Method

Creates a texture descriptor object for a cube texture.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS
- visionOS 1.0+

## Declaration

```swift
class func textureCubeDescriptor(pixelFormat: MTLPixelFormat, size: Int, mipmapped: Bool) -> MTLTextureDescriptor
```

```objc
+ (MTLTextureDescriptor *) textureCubeDescriptorWithPixelFormat:(MTLPixelFormat) pixelFormat size:(NSUInteger) size mipmapped:(BOOL) mipmapped;
```

## Return Value

A pointer to a texture descriptor object for a cube texture.

## Discussion

For a cube texture, the property values describe one slice, which is any one of its six sides. Each slice is a square.

## Parameters

- `pixelFormat`: The format describing how every pixel on the texture image is stored. The default value is [`MTLPixelFormat.rgba8Unorm`](../mtlpixelformat/rgba8unorm.md).
- `size`: The width and height of each slice of the cube texture. The value needs to be greater than or equal to `1`.
- `mipmapped`: A Boolean indicating whether the resulting image should be mipmapped. If [`true`](../../Swift/true.md), then the [`mipmapLevelCount`](./mipmaplevelcount.md) property in the returned descriptor is computed from `width` and `height`. If [`false`](../../Swift/false.md), then [`mipmapLevelCount`](./mipmaplevelcount.md) is `1`.

## See Also

### Creating texture descriptors
- [class func texture2DDescriptor(pixelFormat: MTLPixelFormat, width: Int, height: Int, mipmapped: Bool) -> MTLTextureDescriptor](./texture2ddescriptor%28pixelformat,width,height,mipmapped%29.md)
  Creates a texture descriptor object for a 2D texture.
- [class func textureBufferDescriptor(with: MTLPixelFormat, width: Int, resourceOptions: MTLResourceOptions, usage: MTLTextureUsage) -> MTLTextureDescriptor](./texturebufferdescriptor%28with,width,resourceoptions,usage%29.md)
  Creates a texture descriptor object for a texture buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtltexturedescriptor/texturecubedescriptor(pixelformat:size:mipmapped:))*
# texture2DDescriptor(pixelFormat:width:height:mipmapped:)

**Framework**: Metal  
**Kind**: method

Creates a texture descriptor object for a 2D texture.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
class func texture2DDescriptor(pixelFormat: MTLPixelFormat, width: Int, height: Int, mipmapped: Bool) -> MTLTextureDescriptor
```

#### Return Value

A pointer to a texture descriptor object for a 2D texture.

## Parameters

- `pixelFormat`: The format describing how every pixel on the texture image is stored. The default value is  .
- `width`: The width of the 2D texture image. The value needs to be greater than or equal to  .
- `height`: The height of the 2D texture image. The value needs to be greater than or equal to  .
- `mipmapped`: A Boolean indicating whether the resulting image should be mipmapped. If  , then the   property in the returned descriptor is computed from   and  . If  , then   is  .

## See Also

- [Metal Shading Language Guide](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Metal/Reference/MetalShadingLanguageGuide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40014364)
- [Metal Programming Guide](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Miscellaneous/Conceptual/MetalProgrammingGuide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40014221)
- [class func textureCubeDescriptor(pixelFormat: MTLPixelFormat, size: Int, mipmapped: Bool) -> MTLTextureDescriptor](mtltexturedescriptor/texturecubedescriptor(pixelformat:size:mipmapped:).md)
  Creates a texture descriptor object for a cube texture.
- [class func textureBufferDescriptor(with: MTLPixelFormat, width: Int, resourceOptions: MTLResourceOptions, usage: MTLTextureUsage) -> MTLTextureDescriptor](mtltexturedescriptor/texturebufferdescriptor(with:width:resourceoptions:usage:).md)
  Creates a texture descriptor object for a texture buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtltexturedescriptor/texture2ddescriptor(pixelformat:width:height:mipmapped:))*
# textureBufferDescriptor(with:width:resourceOptions:usage:)

**Framework**: Metal  
**Kind**: method

Creates a texture descriptor object for a texture buffer.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+
- macOS 10.14+
- tvOS 12.0+
- visionOS 1.0+

## Declaration

```swift
class func textureBufferDescriptor(with pixelFormat: MTLPixelFormat, width: Int, resourceOptions: MTLResourceOptions = [], usage: MTLTextureUsage) -> MTLTextureDescriptor
```

#### Return Value

A pointer to a texture descriptor object for a texture buffer.

## Parameters

- `pixelFormat`: The format describing how every pixel on the texture buffer is stored. The default value is  .
- `width`: The width of the texture buffer. The value needs to be greater than or equal to  .
- `resourceOptions`: The access options to use for the new texture buffer.
- `usage`: The allowed usage of the new texture buffer.

## See Also

- [class func texture2DDescriptor(pixelFormat: MTLPixelFormat, width: Int, height: Int, mipmapped: Bool) -> MTLTextureDescriptor](mtltexturedescriptor/texture2ddescriptor(pixelformat:width:height:mipmapped:).md)
  Creates a texture descriptor object for a 2D texture.
- [class func textureCubeDescriptor(pixelFormat: MTLPixelFormat, size: Int, mipmapped: Bool) -> MTLTextureDescriptor](mtltexturedescriptor/texturecubedescriptor(pixelformat:size:mipmapped:).md)
  Creates a texture descriptor object for a cube texture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtltexturedescriptor/texturebufferdescriptor(with:width:resourceoptions:usage:))*
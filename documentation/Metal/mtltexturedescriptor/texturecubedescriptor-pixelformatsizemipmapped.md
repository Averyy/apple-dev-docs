# textureCubeDescriptor(pixelFormat:size:mipmapped:)

**Framework**: Metal  
**Kind**: method

Creates a texture descriptor object for a cube texture.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
class func textureCubeDescriptor(pixelFormat: MTLPixelFormat, size: Int, mipmapped: Bool) -> MTLTextureDescriptor
```

#### Return Value

A pointer to a texture descriptor object for a cube texture.

#### Discussion

For a cube texture, the property values describe one slice, which is any one of its six sides. Each slice is a square.

## Parameters

- `pixelFormat`: The format describing how every pixel on the texture image is stored. The default value is  .
- `size`: The width and height of each slice of the cube texture. The value must be greater than or equal to 1.
- `mipmapped`: A Boolean indicating whether the resulting image should be mipmapped. If  , then the   property in the returned descriptor is computed from   and  . If  , then   is  .

## See Also

- [class func texture2DDescriptor(pixelFormat: MTLPixelFormat, width: Int, height: Int, mipmapped: Bool) -> MTLTextureDescriptor](mtltexturedescriptor/texture2ddescriptor(pixelformat:width:height:mipmapped:).md)
  Creates a texture descriptor object for a 2D texture.
- [class func textureBufferDescriptor(with: MTLPixelFormat, width: Int, resourceOptions: MTLResourceOptions, usage: MTLTextureUsage) -> MTLTextureDescriptor](mtltexturedescriptor/texturebufferdescriptor(with:width:resourceoptions:usage:).md)
  Creates a texture descriptor object for a texture buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtltexturedescriptor/texturecubedescriptor(pixelformat:size:mipmapped:))*
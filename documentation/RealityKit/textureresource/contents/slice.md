# TextureResource.Contents.Slice

**Framework**: RealityKit  
**Kind**: struct  
**Role**: Structure

An object that references the pixel data for a single slice of a mipmap.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+
- visionOS 2.0+

## Declaration

```swift
struct Slice
```

## Overview

2D array textures have `arrayLength` slices per mipmap, and cube textures have six slices per mipmap. 2D and 3D textures have a single slice per mipmap.

## Topics

### Creating a texture slice
- [static func slice(data: Data, bytesPerRow: Int) -> TextureResource.Contents.Slice](./slice/slice%28data,bytesperrow%29.md)
  Specifies a single mipmap level slice of a texture resource with pixel data that RealityKit copies from a byte buffer.
- [static func slice(unsafeBuffer: any MTLBuffer, offset: Int, size: Int, bytesPerRow: Int) -> TextureResource.Contents.Slice](./slice/slice%28unsafebuffer,offset,size,bytesperrow%29.md)
  Specifies a single mipmap level slice of a texture resource with pixel data that RealityKit copies from a Metal buffer.

## Relationships

### Conforms To
- [Sendable](../../../Swift/sendable.md)
- [SendableMetatype](../../../Swift/sendablemetatype.md)

## See Also

### Defining the content
- [TextureResource.Contents.MipmapLevel](./mipmaplevel.md)
  An object that references the pixel data for a single mipmap of a texture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/textureresource/contents/slice)*
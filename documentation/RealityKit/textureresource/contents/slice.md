# TextureResource.Contents.Slice

**Framework**: RealityKit  
**Kind**: struct

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

#### Overview

2D array textures have `arrayLength` slices per mipmap, and cube textures have six slices per mipmap. 2D and 3D textures have a single slice per mipmap.

## Topics

### Creating a texture slice
- [static func slice(data: Data, bytesPerRow: Int) -> TextureResource.Contents.Slice](textureresource/contents/slice/slice(data:bytesperrow:).md)
  Specifies a single mipmap level slice of a texture resource with pixel data that RealityKit copies from a byte buffer.
- [static func slice(unsafeBuffer: any MTLBuffer, offset: Int, size: Int, bytesPerRow: Int) -> TextureResource.Contents.Slice](textureresource/contents/slice/slice(unsafebuffer:offset:size:bytesperrow:).md)
  Specifies a single mipmap level slice of a texture resource with pixel data that RealityKit copies from a Metal buffer.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [TextureResource.Contents.MipmapLevel](textureresource/contents/mipmaplevel.md)
  An object that references the pixel data for a single mipmap of a texture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/textureresource/contents/slice)*
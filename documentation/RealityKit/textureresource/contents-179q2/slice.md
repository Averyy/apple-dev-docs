# TextureResource.Contents.Slice

**Framework**: RealityKit  
**Kind**: struct

An object that references the pixel data for a single slice of a mipmap.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS ?+
- visionOS 2.0+

## Declaration

```swift
struct Slice
```

#### Overview

2D array textures have `arrayLength` slices per mipmap, and cube textures have six slices per mipmap. 2D and 3D textures have a single slice per mipmap.

## Topics

### Type Methods
- [static slice(data:bytesPerRow:)](textureresource/contents-179q2/slice/slice(data:bytesperrow:).md)
  Specifies a single mipmap level slice of a texture resource with pixel data that RealityKit copies from a byte buffer.
- [static slice(unsafeBuffer:offset:size:bytesPerRow:)](textureresource/contents-179q2/slice/slice(unsafebuffer:offset:size:bytesperrow:).md)
  Specifies a single mipmap level slice of a texture resource with pixel data that RealityKit copies from a Metal buffer.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/textureresource/contents-179q2/slice)*
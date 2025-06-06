# TextureResource.Dimensions3D

**Framework**: RealityKit  
**Kind**: struct

The dimensions of the 3D texture.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 2.0+

## Declaration

```swift
struct Dimensions3D
```

#### Overview

This specifies the width, height, and depth of the 3D texture

## Topics

### Creating the 3D dimensions
- [static func dimensions(width: Int, height: Int, depth: Int) -> TextureResource.Dimensions3D](textureresource/dimensions3d/dimensions(width:height:depth:).md)
  Specifies the dimensions of the 3D texture.
### Default Implementations
- [Equatable Implementations](textureresource/dimensions3d/equatable-implementations.md)
- [Hashable Implementations](textureresource/dimensions3d/hashable-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [static func texture3D(slices: [CGImage], named: String?, options: TextureResource.CreateOptions) async throws -> TextureResource](textureresource/texture3d(slices:named:options:)-6pude.md)
  Asynchronously creates a 3D texture by generating it from images.
- [static func texture3D(slices: [CGImage], named: String?, options: TextureResource.CreateOptions) throws -> TextureResource](textureresource/texture3d(slices:named:options:)-orb.md)
  Synchronously creates a 3D texture by generating it from images.
- [convenience init(dimensions: TextureResource.Dimensions3D, format: TextureResource.Format, contents: TextureResource.Contents) throws](textureresource/init(dimensions:format:contents:)-5l84l.md)
  Synchronously creates a 3D texture resource from a pixel Metal buffer, or data.
- [convenience init(dimensions: TextureResource.Dimensions3D, format: TextureResource.Format, contents: TextureResource.Contents) async throws](textureresource/init(dimensions:format:contents:)-64sua.md)
  Asynchronously creates a 3D texture resource from a pixel Metal buffer, or data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/textureresource/dimensions3d)*
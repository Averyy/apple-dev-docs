# TextureResource.Dimensions2D

**Framework**: RealityKit  
**Kind**: struct

The dimensions of a 2D texture.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 1.0+

## Declaration

```swift
struct Dimensions2D
```

#### Overview

This specifies the width and height of a 2D texture.

## Topics

### Creating the 2D dimensions
- [static func dimensions(width: Int, height: Int) -> TextureResource.Dimensions2D](textureresource/dimensions2d/dimensions(width:height:).md)
  Specifies the dimensions of the 2D texture.
### Default Implementations
- [Equatable Implementations](textureresource/dimensions2d/equatable-implementations.md)
- [Hashable Implementations](textureresource/dimensions2d/hashable-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [convenience init(image: CGImage, withName: String?, options: TextureResource.CreateOptions) async throws](textureresource/init(image:withname:options:)-4qz9s.md)
  Asynchronously creates a texture resource from an in-memory Core Graphics image.
- [convenience init(image: CGImage, withName: String?, options: TextureResource.CreateOptions) throws](textureresource/init(image:withname:options:)-yt2w.md)
  Synchronously creates a texture resource from an in-memory Core Graphics image.
- [convenience init(dimensions: TextureResource.Dimensions2D, format: TextureResource.Format, contents: TextureResource.Contents) throws](textureresource/init(dimensions:format:contents:)-1g3ah.md)
  Synchronously creates a 2D texture resource from a pixel Metal buffer, or data.
- [convenience init(dimensions: TextureResource.Dimensions2D, format: TextureResource.Format, contents: TextureResource.Contents) async throws](textureresource/init(dimensions:format:contents:)-5wn8m.md)
  Asynchronously creates a 2D texture resource from a pixel Metal buffer, or data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/textureresource/dimensions2d)*
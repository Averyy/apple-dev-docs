# TextureResource.Dimensions2DArray

**Framework**: RealityKit  
**Kind**: struct

The dimensions of the 2D array texture.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 2.0+

## Declaration

```swift
struct Dimensions2DArray
```

#### Overview

This specifies the width, height, and length of the 2D array texture.

## Topics

### Creating the 2D array dimensions
- [static func dimensions(width: Int, height: Int, length: Int) -> TextureResource.Dimensions2DArray](textureresource/dimensions2darray/dimensions(width:height:length:).md)
  Specifies the dimensions of the 2D array texture.
### Default Implementations
- [Equatable Implementations](textureresource/dimensions2darray/equatable-implementations.md)
- [Hashable Implementations](textureresource/dimensions2darray/hashable-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [static func texture2DArray(slices: [CGImage], named: String?, options: TextureResource.CreateOptions) async throws -> TextureResource](textureresource/texture2darray(slices:named:options:)-50g10.md)
  Asynchronously creates a 2D texture array by generating it from images.
- [static func texture2DArray(slices: [CGImage], named: String?, options: TextureResource.CreateOptions) throws -> TextureResource](textureresource/texture2darray(slices:named:options:)-8m54f.md)
  Synchronously creates a 2D texture array by generating it from images.
- [convenience init(dimensions: TextureResource.Dimensions2DArray, format: TextureResource.Format, contents: TextureResource.Contents) async throws](textureresource/init(dimensions:format:contents:)-324ls.md)
  Asynchronously creates a 2D array texture resource from a pixel Metal buffer, or data.
- [convenience init(dimensions: TextureResource.Dimensions2DArray, format: TextureResource.Format, contents: TextureResource.Contents) throws](textureresource/init(dimensions:format:contents:)-7p7hr.md)
  Synchronously creates a 2D array texture resource from a pixel Metal buffer, or data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/textureresource/dimensions2darray)*
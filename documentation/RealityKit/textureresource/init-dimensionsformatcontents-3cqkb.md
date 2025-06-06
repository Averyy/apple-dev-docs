# init(dimensions:format:contents:)

**Framework**: RealityKit  
**Kind**: init

Synchronously creates a cube texture resource from a pixel Metal buffer, or data.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 2.0+

## Declaration

```swift
@MainActor
@preconcurrency convenience init(dimensions: TextureResource.DimensionsCube, format: TextureResource.Format, contents: TextureResource.Contents) throws
```

#### Discussion

Loading a [`TextureResource`](textureresource.md) with this method blocks the main actor because it’s synchronous, so only call it from a command-line application. The method can stall a regular app, which makes it visibly hitch, and the system terminates an app if its UI becomes unresponsive. See [`init(named:in:)`](textureresource/init(named:in:).md) for an example that demonstrates how to safely load content.

RealityKit efficiently creates a cube texture from raw pixel bytes, with full control over the values and pixel format. See [`init(dimensions:format:contents:)`](textureresource/init(dimensions:format:contents:)-75en1.md) for more details.

## Parameters

- `dimensions`: The dimensions of the cube texture to create.
- `format`: The semantic interpretation of the pixel data.
- `contents`: Pixel data the system copies into the created texture.

## See Also

- [convenience init(cubeFromEquirectangular: CGImage, named: String?, quality: TextureResource.SamplingQuality, faceSize: Int?, options: TextureResource.CreateOptions) throws](textureresource/init(cubefromequirectangular:named:quality:facesize:options:)-5k2py.md)
  Synchronously creates a cube texture resource from an equirectangular image.
- [convenience init(cubeFromEquirectangular: CGImage, named: String?, quality: TextureResource.SamplingQuality, faceSize: Int?, options: TextureResource.CreateOptions) async throws](textureresource/init(cubefromequirectangular:named:quality:facesize:options:)-bqd7.md)
  Asynchronously creates a cube texture resource from an equirectangular image.
- [convenience init(cubeFromImage: CGImage, named: String?, options: TextureResource.CreateOptions) throws](textureresource/init(cubefromimage:named:options:)-3247o.md)
  Synchronously creates a cube texture resource from a 2D image of cube faces.
- [convenience init(cubeFromImage: CGImage, named: String?, options: TextureResource.CreateOptions) async throws](textureresource/init(cubefromimage:named:options:)-9dcus.md)
  Asynchronously creates a cube texture resource from a 2D image of cube faces.
- [static func cube(slices: [CGImage], named: String?, options: TextureResource.CreateOptions) async throws -> TextureResource](textureresource/cube(slices:named:options:)-57yj1.md)
  Asynchronously creates a cube texture resource from face images.
- [static func cube(slices: [CGImage], named: String?, options: TextureResource.CreateOptions) throws -> TextureResource](textureresource/cube(slices:named:options:)-8qsiu.md)
  Synchronously creates a cube texture resource from face images.
- [convenience init(dimensions: TextureResource.DimensionsCube, format: TextureResource.Format, contents: TextureResource.Contents) async throws](textureresource/init(dimensions:format:contents:)-75en1.md)
  Asynchronously creates a cube texture resource from a pixel Metal buffer, or data.
- [TextureResource.DimensionsCube](textureresource/dimensionscube.md)
  The dimensions of the cube texture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/textureresource/init(dimensions:format:contents:)-3cqkb)*
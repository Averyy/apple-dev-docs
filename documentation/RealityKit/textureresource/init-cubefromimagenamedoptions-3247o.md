# init(cubeFromImage:named:options:)

**Framework**: RealityKit  
**Kind**: init

Synchronously creates a cube texture resource from a 2D image of cube faces.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 2.0+

## Declaration

```swift
@MainActor
@preconcurrency convenience init(cubeFromImage cgImage: CGImage, named resourceName: String? = nil, options: TextureResource.CreateOptions) throws
```

#### Discussion

Loading a [`TextureResource`](textureresource.md) with this method blocks the main actor because it’s synchronous, so only call it from a command-line application. The method can stall a regular app, which makes it visibly hitch, and the system terminates an app if its UI becomes unresponsive. See [`init(named:in:)`](textureresource/init(named:in:).md) for an example that demonstrates how to safely load content.

RealityKit extracts the cube faces from the source 2D image using a convention based on its aspect ratio. See [`init(cubeFromImage:named:options:)`](textureresource/init(cubefromimage:named:options:)-9dcus.md)  for more details.

```swift
if let source = CGImageSourceCreateWithURL(url as CFURL, nil),
    let image = CGImageSourceCreateImageAtIndex(source, 0, nil) {

    // Create a cube texture from the image.
    let cube = try TextureResource(
        cubeFromImage: image,
        options: TextureResource.CreateOptions(semantic: .hdrColor))

    // Create an environment resource from the cube texture.
    let environment = try EnvironmentResource(
        cube: cube, options: EnvironmentResource.CreateOptions())

    // Assign the environment to an image-based light component.
    let lightEntity = Entity()
    lightEntity.components.set(ImageBasedLightComponent(source: .single(environment)))
    ...
}
```

## Parameters

- `cgImage`: The source image.
- `resourceName`: A unique name for syncing the texture resource across the network.   The name is empty if you don’t include one.
- `options`: A configuration for generating the texture.

## See Also

- [convenience init(cubeFromEquirectangular: CGImage, named: String?, quality: TextureResource.SamplingQuality, faceSize: Int?, options: TextureResource.CreateOptions) throws](textureresource/init(cubefromequirectangular:named:quality:facesize:options:)-5k2py.md)
  Synchronously creates a cube texture resource from an equirectangular image.
- [convenience init(cubeFromEquirectangular: CGImage, named: String?, quality: TextureResource.SamplingQuality, faceSize: Int?, options: TextureResource.CreateOptions) async throws](textureresource/init(cubefromequirectangular:named:quality:facesize:options:)-bqd7.md)
  Asynchronously creates a cube texture resource from an equirectangular image.
- [convenience init(cubeFromImage: CGImage, named: String?, options: TextureResource.CreateOptions) async throws](textureresource/init(cubefromimage:named:options:)-9dcus.md)
  Asynchronously creates a cube texture resource from a 2D image of cube faces.
- [static func cube(slices: [CGImage], named: String?, options: TextureResource.CreateOptions) async throws -> TextureResource](textureresource/cube(slices:named:options:)-57yj1.md)
  Asynchronously creates a cube texture resource from face images.
- [static func cube(slices: [CGImage], named: String?, options: TextureResource.CreateOptions) throws -> TextureResource](textureresource/cube(slices:named:options:)-8qsiu.md)
  Synchronously creates a cube texture resource from face images.
- [convenience init(dimensions: TextureResource.DimensionsCube, format: TextureResource.Format, contents: TextureResource.Contents) throws](textureresource/init(dimensions:format:contents:)-3cqkb.md)
  Synchronously creates a cube texture resource from a pixel Metal buffer, or data.
- [convenience init(dimensions: TextureResource.DimensionsCube, format: TextureResource.Format, contents: TextureResource.Contents) async throws](textureresource/init(dimensions:format:contents:)-75en1.md)
  Asynchronously creates a cube texture resource from a pixel Metal buffer, or data.
- [TextureResource.DimensionsCube](textureresource/dimensionscube.md)
  The dimensions of the cube texture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/textureresource/init(cubefromimage:named:options:)-3247o)*
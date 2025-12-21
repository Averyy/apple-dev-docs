# TextureResource

**Framework**: RealityKit  
**Kind**: class

A representation of a texture.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 26.0+
- visionOS ?+

## Declaration

```swift
@MainActor
@preconcurrency class TextureResource
```

#### Overview

A texture resource holds pixel data accessible by the GPU, organized as an image, a cube of images, an array of images, or a 3D image (volume texture).

Assign texture resources to material parameters to provide color and fine surface-rendering details.

## Topics

### Creating a texture resource
- [TextureResource.Contents](textureresource/contents.md)
  An object that references the pixel data for each mipmap level of a texture.
- [TextureResource.Format](textureresource/format.md)
  The pixel format and encoding of a texture.
- [TextureResource.Compression](textureresource/compression.md)
  The compression to apply when importing an image as a texture.
### Creating a 2D texture resource
- [TextureResource.Dimensions2D](textureresource/dimensions2d.md)
  The dimensions of a 2D texture.
### Creating a cube texture resource
- [TextureResource.DimensionsCube](textureresource/dimensionscube.md)
  The dimensions of the cube texture.
### Creating a 2D array texture resource
- [TextureResource.Dimensions2DArray](textureresource/dimensions2darray.md)
  The dimensions of the 2D array texture.
### Creating a 3D texture resource
- [TextureResource.Dimensions3D](textureresource/dimensions3d.md)
  The dimensions of the 3D texture.
### Loading a texture
- [convenience init(named: String, in: Bundle?) async throws](textureresource/init(named:in:).md)
  Asynchronously loads a texture resource from a bundle.
- [convenience init(named: String, in: Bundle?, options: TextureResource.CreateOptions) async throws](textureresource/init(named:in:options:).md)
  Asynchronously loads a texture resource from a bundle with options.
- [convenience init(contentsOf: URL, withName: String?, options: TextureResource.CreateOptions) async throws](textureresource/init(contentsof:withname:options:).md)
  Asynchronously creates a texture resource from a file URL with creation options.
- [convenience init(contentsOf: URL, withName: String?) async throws](textureresource/init(contentsof:withname:).md)
  Synchronously creates a texture resource from a file URL.
- [static func load(named: String, in: Bundle?) throws -> TextureResource](textureresource/load(named:in:).md)
  Returns a texture resource by synchronously loading it from a bundle.
- [static func load(named: String, in: Bundle?, options: TextureResource.CreateOptions) throws -> TextureResource](textureresource/load(named:in:options:).md)
  Returns a texture resource by synchronously loading it from a bundle with options.
- [static func load(contentsOf: URL, withName: String?, options: TextureResource.CreateOptions) throws -> TextureResource](textureresource/load(contentsof:withname:options:).md)
  Synchronously loads a texture resource from a URL with options.
- [static func load(contentsOf: URL, withName: String?) throws -> TextureResource](textureresource/load(contentsof:withname:).md)
  Synchronously loads a texture resource from a URL.
- [static func loadAsync(named: String, in: Bundle?) -> LoadRequest<TextureResource>](textureresource/loadasync(named:in:).md)
  Returns a load request that creates a texture resource by asynchronously loading it from a bundle.
- [static func loadAsync(named: String, in: Bundle?, options: TextureResource.CreateOptions) -> LoadRequest<TextureResource>](textureresource/loadasync(named:in:options:).md)
  Returns a load request that creates a texture resource by asynchronously loading it from a bundle with options.
- [static func loadAsync(contentsOf: URL, withName: String?) -> LoadRequest<TextureResource>](textureresource/loadasync(contentsof:withname:).md)
  Asynchronously loads a texture resource from a URL.
### Describing the texture
- [var textureType: MTLTextureType](textureresource/texturetype.md)
  The dimension and arrangement of the texture image data.
- [var pixelFormat: MTLPixelFormat](textureresource/pixelformat.md)
  The texture’s pixel format.
- [var height: Int](textureresource/height.md)
  The height of the texture image, in pixels.
- [var width: Int](textureresource/width.md)
  The width of the texture image, in pixels.
- [var depth: Int](textureresource/depth.md)
  The depth of the texture image, in pixels.
- [var arrayLength: Int](textureresource/arraylength.md)
  The number of slices in the texture array.
- [var mipmapLevelCount: Int](textureresource/mipmaplevelcount.md)
  The number of mipmaps for the texture.
- [var semantic: TextureResource.Semantic?](textureresource/semantic-swift.property.md)
  The intended usage of the texture resource.
### Drawing the texture
- [var drawableQueue: TextureResource.DrawableQueue?](textureresource/drawablequeue-swift.property.md)
  The drawable queue that replaces the texture.
### Copying the texture
- [func copy(to: any MTLTexture) throws](textureresource/copy(to:)-jfbi.md)
  Copies texture data to another texture.
- [func copyAsync(to: any MTLTexture, completionHandler: ((any Error)?) -> Void)](textureresource/copyasync(to:completionhandler:).md)
  Asynchronously copies texture data to another texture.
### Modifying the texture
- [func replace(withDrawables: TextureResource.DrawableQueue)](textureresource/replace(withdrawables:).md)
  Dynamically replaces the texture with a drawable queue.
- [func replace(withImage: CGImage, options: TextureResource.CreateOptions) throws](textureresource/replace(withimage:options:).md)
  Dynamically replaces the texture with a Core Graphics image.
- [func replace(using: CGImage, options: TextureResource.CreateOptions) async throws](textureresource/replace(using:options:).md)
  Asynchronously replaces the texture with a Core Graphics image.
- [func replace(with: LowLevelTexture)](textureresource/replace(with:).md)
  Replaces a texture resource with a low-level texture.
### Deprecated
- [static func generate(from: CGImage, withName: String?, options: TextureResource.CreateOptions) throws -> TextureResource](textureresource/generate(from:withname:options:).md)
  Synchronously creates a texture resource from an in-memory Core Graphics image.
- [static func generateAsync(from: CGImage, withName: String?, options: TextureResource.CreateOptions) -> LoadRequest<TextureResource>](textureresource/generateasync(from:withname:options:).md)
  Asynchronously generates a texture resource from an in-memory Core Graphics image.
- [func replaceAsync(withImage: CGImage, options: TextureResource.CreateOptions) -> LoadRequest<TextureResource>](textureresource/replaceasync(withimage:options:).md)
  Asynchronously replaces the texture with a Core Graphics image.
- [static func generate(from: CGImage, named: String?, options: TextureResource.CreateOptions) async throws -> TextureResource](textureresource/generate(from:named:options:).md)
  Asynchronously generates a texture resource from an in-memory Core Graphics image.
- [static func loadAsync(contentsOf: URL, withName: String?, options: TextureResource.CreateOptions) -> LoadRequest<TextureResource>](textureresource/loadasync(contentsof:withname:options:).md)
  Asynchronously loads a texture resource from a URL with options.
### Classes
- [TextureResource.Drawable](textureresource/drawable.md)
  A drawable associated with a drawable queue
- [TextureResource.DrawableQueue](textureresource/drawablequeue-swift.class.md)
  A drawable queue that may be used to update a texture resource dynamically
### Structures
- [TextureResource.CreateOptions](textureresource/createoptions.md)
  An object that holds texture resource creation options.
### Initializers
- [convenience(cubeFromEquirectangular:named:quality:faceSize:options:)](textureresource/init(cubefromequirectangular:named:quality:facesize:options:).md)
  Asynchronously creates a cube texture resource from an equirectangular image.
- [convenience(cubeFromImage:named:options:)](textureresource/init(cubefromimage:named:options:).md)
  Asynchronously creates a cube texture resource from a 2D image of cube faces.
- [convenience(dimensions:format:contents:)](textureresource/init(dimensions:format:contents:).md)
  Asynchronously creates a 2D texture resource from a pixel Metal buffer, or data.
- [convenience(from:)](textureresource/init(from:).md)
  Asynchronously creates a texture resource from a low-level texture.
- [convenience(image:withName:options:)](textureresource/init(image:withname:options:).md)
  Asynchronously creates a texture resource from an in-memory Core Graphics image.
### Instance Methods
- [func copy(to:)](textureresource/copy(to:).md)
  Asynchronously copies texture data to another texture.
### Type Aliases
- [TextureResource.SamplingQuality](textureresource/samplingquality.md)
  An object for controlling the texture-sampling quality.
### Type Methods
- [static cube(slices:named:options:)](textureresource/cube(slices:named:options:).md)
  Asynchronously creates a cube texture resource from face images.
- [static texture2DArray(slices:named:options:)](textureresource/texture2darray(slices:named:options:).md)
  Asynchronously creates a 2D texture array by generating it from images.
- [static texture3D(slices:named:options:)](textureresource/texture3d(slices:named:options:).md)
  Asynchronously creates a 3D texture by generating it from images.
### Enumerations
- [TextureResource.MipmapsMode](textureresource/mipmapsmode.md)
  An enumeration for specifying how to allocate and generate mipmaps for a texture.
- [TextureResource.Semantic](textureresource/semantic-swift.enum.md)
  An object for specifying the intended use of a texture.
### Default Implementations
- [Equatable Implementations](textureresource/equatable-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Resource](resource.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [TextureResource.CreateOptions](textureresource/createoptions.md)
  An object that holds texture resource creation options.
- [TextureResource.SamplingQuality](textureresource/samplingquality.md)
  An object for controlling the texture-sampling quality.
- [TextureResource.MipmapsMode](textureresource/mipmapsmode.md)
  An enumeration for specifying how to allocate and generate mipmaps for a texture.
- [TextureResource.Semantic](textureresource/semantic-swift.enum.md)
  An object for specifying the intended use of a texture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/textureresource)*
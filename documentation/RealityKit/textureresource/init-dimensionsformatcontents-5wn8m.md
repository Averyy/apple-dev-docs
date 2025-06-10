# init(dimensions:format:contents:)

**Framework**: RealityKit  
**Kind**: init

Asynchronously creates a 2D texture resource from a pixel Metal buffer, or data.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+ (Beta)
- visionOS 1.0+

## Declaration

```swift
@MainActor
@preconcurrency convenience init(dimensions: TextureResource.Dimensions2D, format: TextureResource.Format, contents: TextureResource.Contents) async throws
```

#### Discussion

RealityKit efficiently creates a 2D texture from raw pixel bytes, with full control over the values and pixel format.

```swift
var mips: [TextureResource.Contents.MipmapLevel] = []

// Create the various mipmap levels.
// A `bufferMipsInfo` structure describes the mipmap packing in the source `MTLBuffer`.
for mipInfo in bufferMipsInfo {
    mips.append(.mip(
        unsafeBuffer: buffer,
        offset: mipInfo.offset,
        size: mipInfo.size,
        bytesPerRow: mipInfo.width * bytesPerPixel
    ))
}

let texture = try await TextureResource(
    dimensions: .dimensions(width: width, height: height),
    format: .color(.displayP3, pixelFormat: .rgba8Unorm),
    contents: TextureResource.Contents(mipmapLevels: mips)
)
```

See [`init(named:in:)`](textureresource/init(named:in:).md) for an example of optimally loading textures with other content.

## Parameters

- `dimensions`: The width and height of the texture to create.
- `format`: The semantic interpretation of the pixel data.
- `contents`: Pixel data the system copies into the created texture.

## See Also

- [convenience init(image: CGImage, withName: String?, options: TextureResource.CreateOptions) async throws](textureresource/init(image:withname:options:)-4qz9s.md)
  Asynchronously creates a texture resource from an in-memory Core Graphics image.
- [convenience init(image: CGImage, withName: String?, options: TextureResource.CreateOptions) throws](textureresource/init(image:withname:options:)-yt2w.md)
  Synchronously creates a texture resource from an in-memory Core Graphics image.
- [convenience init(dimensions: TextureResource.Dimensions2D, format: TextureResource.Format, contents: TextureResource.Contents) throws](textureresource/init(dimensions:format:contents:)-1g3ah.md)
  Synchronously creates a 2D texture resource from a pixel Metal buffer, or data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/textureresource/init(dimensions:format:contents:)-5wn8m)*
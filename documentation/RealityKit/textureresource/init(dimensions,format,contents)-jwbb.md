# init(dimensions:format:contents:)

**Framework**: RealityKit  
**Kind**: init  
**Role**: Initializer

Asynchronously creates a 2D array texture resource from a pixel Metal buffer, or data.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+
- visionOS 2.0+

## Declaration

```swift
@MainActor
@preconcurrency convenience init(dimensions: TextureResource.Dimensions2DArray, format: TextureResource.Format, contents: TextureResource.Contents) async throws
```

**Other overloads**:

```swift
@MainActor
@preconcurrency convenience init(dimensions: TextureResource.Dimensions2D, format: TextureResource.Format, contents: TextureResource.Contents) async throws
```

```swift
@MainActor
@preconcurrency convenience init(dimensions: TextureResource.Dimensions2D, format: TextureResource.Format, contents: TextureResource.Contents) throws
```

```swift
@MainActor
@preconcurrency convenience init(dimensions: TextureResource.Dimensions2DArray, format: TextureResource.Format, contents: TextureResource.Contents) throws
```

```swift
@MainActor
@preconcurrency convenience init(dimensions: TextureResource.Dimensions3D, format: TextureResource.Format, contents: TextureResource.Contents) async throws
```

```swift
@MainActor
@preconcurrency convenience init(dimensions: TextureResource.Dimensions3D, format: TextureResource.Format, contents: TextureResource.Contents) throws
```

```swift
@MainActor
@preconcurrency convenience init(dimensions: TextureResource.DimensionsCube, format: TextureResource.Format, contents: TextureResource.Contents) async throws
```

```swift
@MainActor
@preconcurrency convenience init(dimensions: TextureResource.DimensionsCube, format: TextureResource.Format, contents: TextureResource.Contents) throws
```

## Discussion

RealityKit efficiently creates a 2D array texture from raw pixel bytes, with full control over the values and pixel format. You can assign the resulting texture to a material you create in Reality Composer Pro that requires a 2D texture array.

```swift
var mips: [TextureResource.Contents.MipmapLevel] = []

// Create the various mipmap levels.
// A `bufferMipsInfo` structure describes the mipmap packing in the source `MTLBuffer`.
for mipInfo in bufferMipsInfo {
    var slices = [TextureResource.Contents.Slice]()
    for sliceInfo in mipInfo {
        slices.append(.slice(
            unsafeBuffer: buffer,
            offset: sliceInfo.offset,
            size: sliceInfo.size,
            bytesPerRow: sliceInfo.width * bytesPerPixel
        ))
    }
    mips.append(.mip(slices: slices))
}

let texture = try TextureResource(
    dimensions: .dimensions(width: width, height: height, length: arrayLength),
    format: .color(.displayP3, pixelFormat: .rgba8Unorm),
    contents: TextureResource.Contents(mipmapLevels: mips)
)
```

See [`init(named:in:)`](./init%28named,in%29.md) for an example of optimally loading textures with other content.

## Parameters

- `dimensions`: The dimensions of the 2D array texture to create.
- `format`: The semantic interpretation of the pixel data.
- `contents`: Pixel data the system copies into the created texture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/textureresource/init(dimensions:format:contents:)-jwbb)*
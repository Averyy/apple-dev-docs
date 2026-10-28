# init(dimensions:format:contents:)

**Framework**: RealityKit  
**Kind**: init  
**Role**: Initializer

Asynchronously creates a cube texture resource from a pixel Metal buffer, or data.

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
@preconcurrency convenience init(dimensions: TextureResource.DimensionsCube, format: TextureResource.Format, contents: TextureResource.Contents) async throws
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
@preconcurrency convenience init(dimensions: TextureResource.Dimensions2DArray, format: TextureResource.Format, contents: TextureResource.Contents) async throws
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
@preconcurrency convenience init(dimensions: TextureResource.DimensionsCube, format: TextureResource.Format, contents: TextureResource.Contents) throws
```

## Discussion

RealityKit efficiently creates a cube texture from raw pixel bytes, with full control over the values and pixel format. Use the resulting texture to create an [`EnvironmentResource`](../environmentresource.md), or assign it to a material in Reality Composer Pro that requires a cube texture type.

```swift
var mips: [TextureResource.Contents.MipmapLevel] = []

// Create the various mipmap levels.
// A `bufferMipsInfo` structure describes the mipmap packing in the source `MTLBuffer`.
for mipInfo in bufferMipsInfo {
    var faceSlices = [TextureResource.Contents.Slice]()
    for faceInfo in mipInfo {
        faceSlices.append(.slice(
            unsafeBuffer: buffer,
            offset: faceInfo.offset,
            size: faceInfo.size,
            bytesPerRow: faceInfo.width * bytesPerPixel
        ))
    }
    mips.append(.mip(slices: faceSlices))
}

let texture = try TextureResource(
    dimensions: .dimensions(faceSize: faceSize),
    format: .color(.displayP3, pixelFormat: .rgba8Unorm),
    contents: TextureResource.Contents(mipmapLevels: mips)
)
```

See [`init(named:in:)`](./init%28named,in%29.md) for an example of optimally loading textures with other content.

## Parameters

- `dimensions`: The dimensions of the cube texture to create.
- `format`: The semantic interpretation of the pixel data.
- `contents`: Pixel data the system copies into the created texture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/textureresource/init(dimensions:format:contents:)-2uhsw)*
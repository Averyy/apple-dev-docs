# init(dimensions:format:contents:)

**Framework**: RealityKit  
**Kind**: init  
**Role**: Initializer

Synchronously creates a cube texture resource from a pixel Metal buffer, or data.

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
@preconcurrency convenience init(dimensions: TextureResource.DimensionsCube, format: TextureResource.Format, contents: TextureResource.Contents) throws
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
@preconcurrency convenience init(dimensions: TextureResource.DimensionsCube, format: TextureResource.Format, contents: TextureResource.Contents) async throws
```

## Discussion

Loading a [`TextureResource`](../textureresource.md) with this method blocks the main actor because it’s synchronous, so only call it from a command-line application. The method can stall a regular app, which makes it visibly hitch, and the system terminates an app if its UI becomes unresponsive. See [`init(named:in:)`](./init%28named,in%29.md) for an example that demonstrates how to safely load content.

RealityKit efficiently creates a cube texture from raw pixel bytes, with full control over the values and pixel format. See `init(dimensions:format:contents:)-75en1` for more details.

## Parameters

- `dimensions`: The dimensions of the cube texture to create.
- `format`: The semantic interpretation of the pixel data.
- `contents`: Pixel data the system copies into the created texture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/textureresource/init(dimensions:format:contents:)-ritg)*
# copy(to:)

**Framework**: RealityKit  
**Kind**: method

Copies texture data to another texture.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- visionOS ?+

## Declaration

```swift
@MainActor
@preconcurrency func copy(to texture: any MTLTexture) throws
```

#### Discussion

This method blocks until it finishes copying the data. If you have an attached [`TextureResource.DrawableQueue`](textureresource/drawablequeue-swift.class.md) on this resource, this function detaches it. This method copies all available mipmap sizes to `texture`.

It’s recommended that you provide a value for [`semantic`](textureresource/createoptions/semantic.md) when creating this resource. Specifying a semantic enables RealityKit to select an appropriate pixel format for the target texture.

Here’s an example using [`copy(to:)`](textureresource/copy(to:)-jfbi.md) to get a texture resource’s raw pixel data:

```swift
let device: MTLDevice = ...
let resource: TextureResource = ...
let descriptor = MTLTextureDescriptor.texture2DDescriptor(
    pixelFormat: .rgba8Unorm,
    width: resource.width, // Needs to match the texture resource.
    height: resource.height, // Needs to match the texture resource.
    mipmapped: false)
descriptor.usage = .shaderWrite // This is required for copying.

guard let texture = device.makeTexture(descriptor: descriptor)
else { throw ... }
try resource.copy(to: texture)

#if os(OSX) // The managed mode exists only in OSX.
if texture.storageMode == .managed {
    // You need to synchronize the managed textures before accessing their data.
    guard let commandBuffer = device.makeCommandQueue()?.makeCommandBuffer(),
          let blitEncoder = commandBuffer.makeBlitCommandEncoder()
    else { throw ... }

    blitEncoder.synchronize(resource: texture)
    blitEncoder.endEncoding()
    commandBuffer.commit()
    commandBuffer.waitUntilCompleted()
}
#endif

// Getting the raw pixel bytes.
let bytesPerRow = 4 * texture.width
var bytes = [UInt8](repeating: 0, count: texture.height * bytesPerRow)
bytes.withUnsafeMutableBytes { bytesPtr in
    texture.getBytes(
        bytesPtr.baseAddress!,
        bytesPerRow: bytesPerRow,
        from: .init(origin: .init(), size: .init(width: texture.width, height: texture.height, depth: 1)),
        mipmapLevel: 0
    )
}
```

## Parameters

- `texture`: The target texture for copying the data. It needs to have the same width and height as  , and    usage.

## See Also

- [func copy(to: any MTLTexture) async throws](textureresource/copy(to:)-3lfen.md)
  Asynchronously copies texture data to another texture.
- [func copyAsync(to: any MTLTexture, completionHandler: ((any Error)?) -> Void)](textureresource/copyasync(to:completionhandler:).md)
  Asynchronously copies texture data to another texture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/textureresource/copy(to:)-jfbi)*
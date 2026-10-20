# nextDrawable()

**Framework**: RealityKit  
**Kind**: method  
**Role**: Instance Method

Returns drawable when one is available, blocking the caller in the meantime.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 26.0+
- visionOS

## Declaration

```swift
func nextDrawable() throws -> TextureResource.Drawable
```

#### Discussion

The method can block the caller for a duration up to the [`timeout`](./descriptor/timeout.md) period.

> **Note**: The method returns `nil` without blocking when the drawable queue isn’t bound to a material in the scene, or when the render server is currently loading and initializing it.

## See Also

### Working with queues
- [var allowsNextDrawableTimeout: Bool](./allowsnextdrawabletimeout.md)
  A Boolean value that determines whether requests for a new drawable expire if the system can’t satisfy them.
- [var height: Int](./height.md)
  The height of each drawable’s texture in pixels.
- [var mipmapsMode: TextureResource.MipmapsMode](./mipmapsmode.md)
  Options that determine how mipmaps are handled for each drawable’s textures.
- [var pixelFormat: MTLPixelFormat](./pixelformat.md)
  The size and bit layout of all pixels in each drawable’s texture.
- [var usage: MTLTextureUsage](./usage.md)
  Options that determine how you can use each drawable’s textures.
- [var width: Int](./width.md)
  The width of each drawable’s texture in pixels.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/textureresource/drawablequeue-swift.class/nextdrawable())*
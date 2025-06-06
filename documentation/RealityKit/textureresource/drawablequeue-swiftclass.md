# TextureResource.DrawableQueue

**Framework**: RealityKit  
**Kind**: class

A drawable queue that may be used to update a texture resource dynamically

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- visionOS ?+

## Declaration

```swift
class DrawableQueue
```

#### Overview

Each drawable queue can work with at most one consumer, such as a [`RealityRenderer`](realityrenderer.md) instance or a render server.

## Topics

### Creating a queue
- [init(TextureResource.DrawableQueue.Descriptor) throws](textureresource/drawablequeue-swift.class/init(_:).md)
  Create a new drawable queue.
### Working with queues
- [var allowsNextDrawableTimeout: Bool](textureresource/drawablequeue-swift.class/allowsnextdrawabletimeout.md)
  A Boolean value that determines whether requests for a new drawable expire if the system can’t satisfy them.
- [var height: Int](textureresource/drawablequeue-swift.class/height.md)
  The height of each drawable’s texture in pixels.
- [var mipmapsMode: TextureResource.MipmapsMode](textureresource/drawablequeue-swift.class/mipmapsmode.md)
  Options that determine how mipmaps are handled for each drawable’s textures.
- [var pixelFormat: MTLPixelFormat](textureresource/drawablequeue-swift.class/pixelformat.md)
  The size and bit layout of all pixels in each drawable’s texture.
- [var usage: MTLTextureUsage](textureresource/drawablequeue-swift.class/usage.md)
  Options that determine how you can use each drawable’s textures.
- [var width: Int](textureresource/drawablequeue-swift.class/width.md)
  The width of each drawable’s texture in pixels.
- [func nextDrawable() throws -> TextureResource.Drawable](textureresource/drawablequeue-swift.class/nextdrawable.md)
  Returns drawable when one is available, blocking the caller in the meantime.
### Structures
- [TextureResource.DrawableQueue.Descriptor](textureresource/drawablequeue-swift.class/descriptor.md)
  Describes the texture managed by the drawable queue

## See Also

- [Rendering a windowed game in stereo](rendering-a-windowed-game-in-stereo.md)
  Bring an iOS or iPadOS game to visionOS and enhance it.
- [Creating a dynamic height and normal map with low-level texture](creating-a-dynamic-height-map-with-low-level-texture.md)
  Create a low-level texture and update its pixel data on the GPU to form a dynamic height and normal map.
- [class LowLevelTexture](lowleveltexture.md)
  A container for texture data allowing you to create and update textures using your own format.
- [LowLevelTexture.Descriptor](lowleveltexture/descriptor-swift.struct.md)
  An object that you use to configure new `LowLevelTexture` objects.
- [TextureResource.Drawable](textureresource/drawable.md)
  A drawable associated with a drawable queue
- [TextureResource.DrawableQueue.Descriptor](textureresource/drawablequeue-swift.class/descriptor.md)
  Describes the texture managed by the drawable queue


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/textureresource/drawablequeue-swift.class)*
# TextureResource.DrawableQueue.Descriptor

**Framework**: RealityKit  
**Kind**: struct

Describes the texture managed by the drawable queue

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 26.0+ (Beta)
- visionOS ?+

## Declaration

```swift
struct Descriptor
```

## Topics

### Initializers
- [init(pixelFormat: MTLPixelFormat, width: Int, height: Int, usage: MTLTextureUsage, mipmapsMode: TextureResource.MipmapsMode)](textureresource/drawablequeue-swift.class/descriptor/init(pixelformat:width:height:usage:mipmapsmode:).md)
- [init(pixelFormat:width:height:usage:mipmapsMode:timeout:)](textureresource/drawablequeue-swift.class/descriptor/init(pixelformat:width:height:usage:mipmapsmode:timeout:).md)
### Instance Properties
- [var height: Int](textureresource/drawablequeue-swift.class/descriptor/height.md)
  The height of each drawable’s texture in pixels.
- [var mipmapsMode: TextureResource.MipmapsMode](textureresource/drawablequeue-swift.class/descriptor/mipmapsmode.md)
  A Boolean value that determines whether the resource should generate mipmaps for each drawable’s texture after it was updated.
- [var pixelFormat: MTLPixelFormat](textureresource/drawablequeue-swift.class/descriptor/pixelformat.md)
  The size and bit layout of all pixels in each drawable’s texture.
- [var timeout: Duration](textureresource/drawablequeue-swift.class/descriptor/timeout-1hh22.md)
  Specifies a timeout value in seconds when querying nextDrawable(). nextDrawable() will be blocked for up to the specified timeout period for a drawable to become available else throws `NextDrawableError.timeoutReached`. By default this is set to 1 second. Note that if `allowsNextDrawableTimeout` is false, then the timeout parameter will be ignored.
- [var timeout: Duration](textureresource/drawablequeue-swift.class/descriptor/timeout-8xq88.md)
  Specifies a timeout value in seconds when querying nextDrawable(). nextDrawable() will be blocked for up to the specified timeout period for a drawable to become available else throws `NextDrawableError.timeoutReached`. By default this is set to 1 second. Note that if `allowsNextDrawableTimeout` is false, then the timeout parameter will be ignored.
- [var usage: MTLTextureUsage](textureresource/drawablequeue-swift.class/descriptor/usage.md)
  Options that determine how you can use each drawable’s textures.
- [var width: Int](textureresource/drawablequeue-swift.class/descriptor/width.md)
  The width of each drawable’s texture in pixels.

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
- [TextureResource.DrawableQueue](textureresource/drawablequeue-swift.class.md)
  A drawable queue that may be used to update a texture resource dynamically


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/textureresource/drawablequeue-swift.class/descriptor)*
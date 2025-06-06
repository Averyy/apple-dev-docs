# outputImageProviderFromTexture(withPixelFormat:pixelsWide:pixelsHigh:name:flipped:releaseCallback:releaseContext:colorSpace:shouldColorMatch:)

**Framework**: Quartz  
**Kind**: method  
**Required**: Yes

Returns an image provider from an OpenGL texture.

**Availability**:
- macOS 10.5+

## Declaration

```swift
func outputImageProviderFromTexture(withPixelFormat format: String!, pixelsWide width: Int, pixelsHigh height: Int, name: GLuint, flipped: Bool, releaseCallback callback: QCPlugInTextureReleaseCallback!, releaseContext context: UnsafeMutableRawPointer!, colorSpace: CGColorSpace!, shouldColorMatch colorMatch: Bool) -> Any!
```

#### Return Value

An image provider.

#### Discussion

You must not modify the texture until the release callback is invoked.

## Parameters

- `format`: The pixel format of the texture. This must be compatible with the color space.
- `width`: The width, in bytes, of the texture.
- `height`: The height, in bytes, of the texture.
- `name`: An OpenGL texture of type   that is valid on the Quartz Composer OpenGL context. Your application must make sure that the texture exists for the life cycle of the image provider.
- `flipped`:   to have Quartz Composer flip the contents of the texture vertically.
- `callback`: Quartz Composer invokes your callback when the memory buffer is no longer needed. The callback can be called from any thread at any time
- `context`: The context to pass to the release callback.
- `colorSpace`: The color space of the texture. This must be compatible with the pixel format.
- `colorMatch`: A Boolean that specifies whether Quartz Composer should color match the texture. Pass    if the texture is a mask or gradient or should not be color matched for some other reason. Otherwise, pass  .

## See Also

- [func outputImageProviderFromBuffer(withPixelFormat: String!, pixelsWide: Int, pixelsHigh: Int, baseAddress: UnsafeRawPointer!, bytesPerRow: Int, releaseCallback: QCPlugInBufferReleaseCallback!, releaseContext: UnsafeMutableRawPointer!, colorSpace: CGColorSpace!, shouldColorMatch: Bool) -> Any!](qcplugincontext/outputimageproviderfrombuffer(withpixelformat:pixelswide:pixelshigh:baseaddress:bytesperrow:releasecallback:releasecontext:colorspace:shouldcolormatch:).md)
  Returns an image provider from a single memory buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/qcplugincontext/outputimageproviderfromtexture(withpixelformat:pixelswide:pixelshigh:name:flipped:releasecallback:releasecontext:colorspace:shouldcolormatch:))*
# outputImageProviderFromBuffer(withPixelFormat:pixelsWide:pixelsHigh:baseAddress:bytesPerRow:releaseCallback:releaseContext:colorSpace:shouldColorMatch:)

**Framework**: Quartz  
**Kind**: method  
**Required**: Yes

Returns an image provider from a single memory buffer.

**Availability**:
- macOS 10.4+

## Declaration

```swift
func outputImageProviderFromBuffer(withPixelFormat format: String!, pixelsWide width: Int, pixelsHigh height: Int, baseAddress: UnsafeRawPointer!, bytesPerRow rowBytes: Int, releaseCallback callback: QCPlugInBufferReleaseCallback!, releaseContext context: UnsafeMutableRawPointer!, colorSpace: CGColorSpace!, shouldColorMatch colorMatch: Bool) -> Any!
```

#### Return Value

An image provider.

#### Discussion

You must not modify the image until the release callback is invoked.

## Parameters

- `format`: The pixel format of the memory buffer. This must be compatible with the color space.
- `width`: The width, in bytes, of the memory buffer.
- `height`: The height, in bytes, of the memory buffer.
- `baseAddress`: The base address of the memory buffer, which must be multiple of 16.
- `rowBytes`: The number of bytes per row of the memory buffer, which must be multiple of 16.
- `callback`: Quartz Composer invokes your callback when the memory buffer is no longer needed. The callback can be called from any thread at any time
- `context`: The context to pass to the release callback.
- `colorSpace`: The color space of the memory buffer. This must be compatible with the pixel format.
- `colorMatch`: A Boolean that specifies whether Quartz Composer should color match the image. Pass    if the image is a mask or gradient or should not be color matched for some other reason. Otherwise, pass  .

## See Also

- [func outputImageProviderFromTexture(withPixelFormat: String!, pixelsWide: Int, pixelsHigh: Int, name: GLuint, flipped: Bool, releaseCallback: QCPlugInTextureReleaseCallback!, releaseContext: UnsafeMutableRawPointer!, colorSpace: CGColorSpace!, shouldColorMatch: Bool) -> Any!](qcplugincontext/outputimageproviderfromtexture(withpixelformat:pixelswide:pixelshigh:name:flipped:releasecallback:releasecontext:colorspace:shouldcolormatch:).md)
  Returns an image provider from an OpenGL texture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/qcplugincontext/outputimageproviderfrombuffer(withpixelformat:pixelswide:pixelshigh:baseaddress:bytesperrow:releasecallback:releasecontext:colorspace:shouldcolormatch:))*
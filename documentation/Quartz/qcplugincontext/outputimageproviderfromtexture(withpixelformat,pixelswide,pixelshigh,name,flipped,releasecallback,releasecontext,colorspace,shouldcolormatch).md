# outputImageProviderFromTexture(withPixelFormat:pixelsWide:pixelsHigh:name:flipped:releaseCallback:releaseContext:colorSpace:shouldColorMatch:)

**Framework**: Quartz  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Returns an image provider from an OpenGL texture.

**Availability**:
- macOS 10.5+ - Deprecated in 10.14

> **Deprecated**: Quartz Composer OpenGL API deprecated. (Define QC_SILENCE_GL_DEPRECATION to silence these warnings)

## Declaration

```swift
func outputImageProviderFromTexture(withPixelFormat format: String!, pixelsWide width: Int, pixelsHigh height: Int, name: GLuint, flipped: Bool, releaseCallback callback: QCPlugInTextureReleaseCallback!, releaseContext context: UnsafeMutableRawPointer!, colorSpace: CGColorSpace!, shouldColorMatch colorMatch: Bool) -> Any!
```

```objc
- (id) outputImageProviderFromTextureWithPixelFormat:(NSString *) format pixelsWide:(NSUInteger) width pixelsHigh:(NSUInteger) height name:(GLuint) name flipped:(BOOL) flipped releaseCallback:(QCPlugInTextureReleaseCallback) callback releaseContext:(void *) context colorSpace:(CGColorSpaceRef) colorSpace shouldColorMatch:(BOOL) colorMatch;
```

## Return Value

An image provider.

## Discussion

You must not modify the texture until the release callback is invoked.

## Parameters

- `format`: The pixel format of the texture. This must be compatible with the color space.
- `width`: The width, in bytes, of the texture.
- `height`: The height, in bytes, of the texture.
- `name`: An OpenGL texture of type `GL_TEXTURE_RECTANGLE_EXT` that is valid on the Quartz Composer OpenGL context. Your application must make sure that the texture exists for the life cycle of the image provider.
- `flipped`: [`true`](../../Swift/true.md) to have Quartz Composer flip the contents of the texture vertically.
- `callback`: The release callback.  Your callback must use this type definition:

  ```objc
  typedef void (*QCPlugInTextureReleaseCallback)(CGLContextObj cgl_ctx, GLuint name, void* context);
  ```

  If you name your callback function `MyQCPlugInTextureReleaseCallback`, you would declare it like this:

  ```objc
  void MyQCPlugInTextureReleaseCallback (CGLContextObj cgl_ctx,
                GLuint name,
                void* context);
  ```

  Quartz Composer invokes your callback when the memory buffer is no longer needed. The callback can be called from any thread at any time
- `context`: The context to pass to the release callback.
- `colorSpace`: The color space of the texture. This must be compatible with the pixel format.
- `colorMatch`: A Boolean that specifies whether Quartz Composer should color match the texture. Pass  [`false`](../../Swift/false.md) if the texture is a mask or gradient or should not be color matched for some other reason. Otherwise, pass [`true`](../../Swift/true.md).

## See Also

### Getting an Image Provider
- [func outputImageProviderFromBuffer(withPixelFormat: String!, pixelsWide: Int, pixelsHigh: Int, baseAddress: UnsafeRawPointer!, bytesPerRow: Int, releaseCallback: QCPlugInBufferReleaseCallback!, releaseContext: UnsafeMutableRawPointer!, colorSpace: CGColorSpace!, shouldColorMatch: Bool) -> Any!](./outputimageproviderfrombuffer%28withpixelformat,pixelswide,pixelshigh,baseaddress,bytesperrow,releasecallback,releasecontext,colorspace,shouldcolormatch%29.md)
  Returns an image provider from a single memory buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/qcplugincontext/outputimageproviderfromtexture(withpixelformat:pixelswide:pixelshigh:name:flipped:releasecallback:releasecontext:colorspace:shouldcolormatch:))*
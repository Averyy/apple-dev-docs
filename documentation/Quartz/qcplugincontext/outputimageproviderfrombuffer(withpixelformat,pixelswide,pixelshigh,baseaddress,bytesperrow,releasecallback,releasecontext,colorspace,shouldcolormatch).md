# outputImageProviderFromBuffer(withPixelFormat:pixelsWide:pixelsHigh:baseAddress:bytesPerRow:releaseCallback:releaseContext:colorSpace:shouldColorMatch:)

**Framework**: Quartz  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Returns an image provider from a single memory buffer.

**Availability**:
- macOS 10.4+ - Deprecated in 10.15

> **Deprecated**: QuartzComposer API deprecated. (Define QC_SILENCE_DEPRECATION to silence these warnings)

## Declaration

```swift
func outputImageProviderFromBuffer(withPixelFormat format: String!, pixelsWide width: Int, pixelsHigh height: Int, baseAddress: UnsafeRawPointer!, bytesPerRow rowBytes: Int, releaseCallback callback: QCPlugInBufferReleaseCallback!, releaseContext context: UnsafeMutableRawPointer!, colorSpace: CGColorSpace!, shouldColorMatch colorMatch: Bool) -> Any!
```

```objc
- (id) outputImageProviderFromBufferWithPixelFormat:(NSString *) format pixelsWide:(NSUInteger) width pixelsHigh:(NSUInteger) height baseAddress:(const void *) baseAddress bytesPerRow:(NSUInteger) rowBytes releaseCallback:(QCPlugInBufferReleaseCallback) callback releaseContext:(void *) context colorSpace:(CGColorSpaceRef) colorSpace shouldColorMatch:(BOOL) colorMatch;
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
- `callback`: The release callback. Your callback must use this type definition:

  ```objc
  typedef void (*QCPlugInBufferReleaseCallback)(const void* address, void* context);
  ```

  If you name your callback function `MyQCPlugInBufferReleaseCallback`, you would declare it like this:

  ```objc
  void MyQCPlugInBufferReleaseCallback (const void address,
                void * context);
  ```

  Quartz Composer invokes your callback when the memory buffer is no longer needed. The callback can be called from any thread at any time
- `context`: The context to pass to the release callback.
- `colorSpace`: The color space of the memory buffer. This must be compatible with the pixel format.
- `colorMatch`: A Boolean that specifies whether Quartz Composer should color match the image. Pass  [`false`](../../Swift/false.md) if the image is a mask or gradient or should not be color matched for some other reason. Otherwise, pass [`true`](../../Swift/true.md).

## See Also

### Getting an Image Provider
- [func outputImageProviderFromTexture(withPixelFormat: String!, pixelsWide: Int, pixelsHigh: Int, name: GLuint, flipped: Bool, releaseCallback: QCPlugInTextureReleaseCallback!, releaseContext: UnsafeMutableRawPointer!, colorSpace: CGColorSpace!, shouldColorMatch: Bool) -> Any!](./outputimageproviderfromtexture%28withpixelformat,pixelswide,pixelshigh,name,flipped,releasecallback,releasecontext,colorspace,shouldcolormatch%29.md)
  Returns an image provider from an OpenGL texture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/qcplugincontext/outputimageproviderfrombuffer(withpixelformat:pixelswide:pixelshigh:baseaddress:bytesperrow:releasecallback:releasecontext:colorspace:shouldcolormatch:))*
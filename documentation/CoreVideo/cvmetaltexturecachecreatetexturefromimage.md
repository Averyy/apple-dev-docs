# CVMetalTextureCacheCreateTextureFromImage(_:_:_:_:_:_:_:_:_:)

**Framework**: Core Video  
**Kind**: func

Creates a Core Video Metal texture buffer from an existing image buffer.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func CVMetalTextureCacheCreateTextureFromImage(_ allocator: CFAllocator?, _ textureCache: CVMetalTextureCache, _ sourceImage: CVImageBuffer, _ textureAttributes: CFDictionary?, _ pixelFormat: MTLPixelFormat, _ width: Int, _ height: Int, _ planeIndex: Int, _ textureOut: UnsafeMutablePointer<CVMetalTexture?>) -> CVReturn
```

#### Return Value

Upon successful creation of the texture, this function returns [`kCVReturnSuccess`](kcvreturnsuccess.md).

#### Discussion

This function creates a cached Core Video Metal texture object mapped to an image buffer, and a live binding to the underlying [`MTLTexture`](https://developer.apple.com/documentation/Metal/MTLTexture) object.

> ❗ **Important**:  You need to maintain a strong reference to `textureOut` until the GPU finishes execution of commands accessing the texture, because the system doesn’t automatically retain it. Developers typically release these references in a block passed to [`addCompletedHandler(_:)`](https://developer.apple.com/documentation/Metal/MTLCommandBuffer/addCompletedHandler(_:)).

 You need to maintain a strong reference to `textureOut` until the GPU finishes execution of commands accessing the texture, because the system doesn’t automatically retain it. Developers typically release these references in a block passed to [`addCompletedHandler(_:)`](https://developer.apple.com/documentation/Metal/MTLCommandBuffer/addCompletedHandler(_:)).

Note that Core Video doesn’t explicitly declare any pixel format types as Metal compatible. Specify [`true`](https://developer.apple.com/documentation/swift/true) for the [`kCVPixelBufferMetalCompatibilityKey`](kcvpixelbuffermetalcompatibilitykey.md) option to create Metal-compatible buffers when creating or requesting Core Video pixel buffers. You’re responsible for ensuring the pixel format is appropriate to the buffer.

The following code snippet demonstrates some example mappings:

```objc
// Mapping a BGRA buffer:
CVMetalTextureCacheCreateTextureFromImage(kCFAllocatorDefault, textureCache, pixelBuffer, NULL, MTLPixelFormatBGRA8Unorm, width, height, 0, &outTexture);
 
// Mapping the luma plane of a 420v buffer:
CVMetalTextureCacheCreateTextureFromImage(kCFAllocatorDefault, textureCache, pixelBuffer, NULL, MTLPixelFormatR8Unorm, width, height, 0, &outTexture);
 
// Mapping the chroma plane of a 420v buffer as a source texture:
CVMetalTextureCacheCreateTextureFromImage(kCFAllocatorDefault, textureCache, pixelBuffer, NULL, MTLPixelFormatRG8Unorm width/2, height/2, 1, &outTexture);
 
// Mapping a yuvs buffer as a source texture (note: yuvs/f and 2vuy are unpacked and resampled -- not colorspace converted)
CVMetalTextureCacheCreateTextureFromImage(kCFAllocatorDefault, textureCache, pixelBuffer, NULL, MTLPixelFormatGBGR422, width, height, 1, &outTexture);
```

## Parameters

- `allocator`: The memory allocator for the texture.
- `textureCache`: The texture cache used to create and manage the texture.
- `sourceImage`: The Core Video image buffer from which to create a Metal texture.
- `textureAttributes`: A dictionary specifying options for creating the texture from the cache, or   to use default options.
- `pixelFormat`: The Metal pixel format constant describing the image buffer’s data.
- `width`: The width, in pixels, of the texture image.
- `height`: The height, in pixels, of the texture image.
- `planeIndex`: If the image buffer is planar, the index of the plane from which to map texture data. Ignored for non-planar image buffers.
- `textureOut`: Upon return, contains the newly created Metal texture buffer. When this value is  , an error occurred in texture creation.

## See Also

- [func CVMetalTextureCacheCreate(CFAllocator?, CFDictionary?, any MTLDevice, CFDictionary?, UnsafeMutablePointer<CVMetalTextureCache?>) -> CVReturn](cvmetaltexturecachecreate(_:_:_:_:_:).md)
  Creates a new texture cache.
- [func CVMetalTextureCacheFlush(CVMetalTextureCache, CVOptionFlags)](cvmetaltexturecacheflush(_:_:).md)
  Manually flushes the contents of the provided texture cache.
- [func CVMetalTextureCacheGetTypeID() -> CFTypeID](cvmetaltexturecachegettypeid().md)
  Returns the Core Foundation type identifier for a Core Video Metal texture cache.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/cvmetaltexturecachecreatetexturefromimage(_:_:_:_:_:_:_:_:_:))*
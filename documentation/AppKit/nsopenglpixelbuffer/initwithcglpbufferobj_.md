# initWithCGLPBufferObj:

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Initializes and returns an OpenGL pixel buffer object that encapsulates an existing CGL pixel buffer object.

**Availability**:
- macOS 10.6+ - Deprecated in 10.7

## Declaration

```objc
- (NSOpenGLPixelBuffer *) initWithCGLPBufferObj:(CGLPBufferObj) pbuffer;
```

#### Return Value

An initialized [`NSOpenGLPixelBuffer`](../nsopenglpixelbuffer.md) object.

#### Discussion

If your application already has a CGL pixel buffer object, you can wrap it inside an [`NSOpenGLPixelBuffer`](../nsopenglpixelbuffer.md) object by using this initializer. This method retains the CGL pixel buffer object by calling the `CGLRetainPBuffer` function.

Your application should not call `CGLDestroyPBuffer` to dispose of the CGL pixel buffer object. Instead, your application should call `CGLReleasePBuffer` to decrement its reference count.

## Parameters

- `pbuffer`: The CGL pixel buffer object to wrap.

## See Also

### Initializing an OpenGL Pixel Buffer
- [- initWithTextureTarget:textureInternalFormat:textureMaxMipMapLevel:pixelsWide:pixelsHigh:](./initwithtexturetarget_textureinternalformat_texturemaxmipmaplevel_pixelswide_pixelshigh_.md)
  Returns an `NSOpenGLPixelBuffer` object initialized with the specified parameters.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsopenglpixelbuffer/initwithcglpbufferobj:)*
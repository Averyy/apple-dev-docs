# supportedRenderedTexturePixelFormats()

**Framework**: Quartz  
**Kind**: method  
**Role**: Instance Method

Returns a list of pixel formats that are supported for rendering to an onscreen OpenGL context.

**Availability**:
- macOS 10.5+ - Deprecated in 10.14

> **Deprecated**: Quartz Composer OpenGL API deprecated. (Define QC_SILENCE_GL_DEPRECATION to silence these warnings)

## Declaration

```swift
optional func supportedRenderedTexturePixelFormats() -> [Any]!
```

```objc
- (NSArray *) supportedRenderedTexturePixelFormats;
```

## Return Value

Returns the list of texture pixel formats supported by [`copyRenderedTexture(forCGLContext:pixelFormat:bounds:isFlipped:)`](./copyrenderedtexture%28forcglcontext,pixelformat,bounds,isflipped%29.md) or `nil` if not supported.

## Discussion

If this method returns nil, then Quartz Composer calls [`canRender(withCGLContext:)`](./canrender%28withcglcontext%29.md) /[`render(withCGLContext:forBounds:)`](./render%28withcglcontext,forbounds%29.md).

## See Also

### Providing Information About the Rendering Destination
- [func supportedBufferPixelFormats() -> [Any]!](./supportedbufferpixelformats%28%29.md)
  Returns a list of pixel formats that are supported for rendering to a memory buffer.
- [func canRender(withCGLContext: CGLContextObj!) -> Bool](./canrender%28withcglcontext%29.md)
  Returns whether the image data can be rendered into the provided CGL context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/qcpluginoutputimageprovider/supportedrenderedtexturepixelformats())*
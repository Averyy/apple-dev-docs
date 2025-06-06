# supportedRenderedTexturePixelFormats()

**Framework**: Quartz  
**Kind**: method

Returns a list of pixel formats that are supported for rendering to an onscreen OpenGL context.

**Availability**:
- macOS 10.5+

## Declaration

```swift
optional func supportedRenderedTexturePixelFormats() -> [Any]!
```

#### Return Value

Returns the list of texture pixel formats supported by [`copyRenderedTexture(forCGLContext:pixelFormat:bounds:isFlipped:)`](qcpluginoutputimageprovider/copyrenderedtexture(forcglcontext:pixelformat:bounds:isflipped:).md) or `nil` if not supported.

#### Discussion

If this method returns nil, then Quartz Composer calls [`canRender(withCGLContext:)`](qcpluginoutputimageprovider/canrender(withcglcontext:).md) /[`render(withCGLContext:forBounds:)`](qcpluginoutputimageprovider/render(withcglcontext:forbounds:).md).

## See Also

- [func supportedBufferPixelFormats() -> [Any]!](qcpluginoutputimageprovider/supportedbufferpixelformats.md)
  Returns a list of pixel formats that are supported for rendering to a memory buffer.
- [func canRender(withCGLContext: CGLContextObj!) -> Bool](qcpluginoutputimageprovider/canrender(withcglcontext:).md)
  Returns whether the image data can be rendered into the provided CGL context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/qcpluginoutputimageprovider/supportedrenderedtexturepixelformats())*
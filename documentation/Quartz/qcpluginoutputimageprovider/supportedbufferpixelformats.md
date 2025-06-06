# supportedBufferPixelFormats()

**Framework**: Quartz  
**Kind**: method

Returns a list of pixel formats that are supported for rendering to a memory buffer.

**Availability**:
- macOS 10.4+

## Declaration

```swift
optional func supportedBufferPixelFormats() -> [Any]!
```

#### Return Value

A list of pixel formats, in order of preference, that the image can be rendered to in memory, or `nil` if the image provider does not support rendering to the CPU.

## See Also

- [func supportedRenderedTexturePixelFormats() -> [Any]!](qcpluginoutputimageprovider/supportedrenderedtexturepixelformats.md)
  Returns a list of pixel formats that are supported for rendering to an onscreen OpenGL context.
- [func canRender(withCGLContext: CGLContextObj!) -> Bool](qcpluginoutputimageprovider/canrender(withcglcontext:).md)
  Returns whether the image data can be rendered into the provided CGL context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/qcpluginoutputimageprovider/supportedbufferpixelformats())*
# supportedBufferPixelFormats()

**Framework**: Quartz  
**Kind**: method  
**Role**: Instance Method

Returns a list of pixel formats that are supported for rendering to a memory buffer.

**Availability**:
- macOS 10.4+ - Deprecated in 10.15

> **Deprecated**: QuartzComposer API deprecated. (Define QC_SILENCE_DEPRECATION to silence these warnings)

## Declaration

```swift
optional func supportedBufferPixelFormats() -> [Any]!
```

```objc
- (NSArray *) supportedBufferPixelFormats;
```

## Return Value

A list of pixel formats, in order of preference, that the image can be rendered to in memory, or `nil` if the image provider does not support rendering to the CPU.

## See Also

### Providing Information About the Rendering Destination
- [func supportedRenderedTexturePixelFormats() -> [Any]!](./supportedrenderedtexturepixelformats%28%29.md)
  Returns a list of pixel formats that are supported for rendering to an onscreen OpenGL context.
- [func canRender(withCGLContext: CGLContextObj!) -> Bool](./canrender%28withcglcontext%29.md)
  Returns whether the image data can be rendered into the provided CGL context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/qcpluginoutputimageprovider/supportedbufferpixelformats())*
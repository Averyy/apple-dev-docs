# CVDisplayLinkSetOutputHandler(_:_:)

**Framework**: Core Video  
**Kind**: func

**Availability**:
- Mac Catalyst 13.1+
- macOS 10.4+

## Declaration

```swift
func CVDisplayLinkSetOutputHandler(_ displayLink: CVDisplayLink, _ handler: @escaping CVDisplayLinkOutputHandler) -> CVReturn
```

## See Also

- [func CVDisplayLinkSetCurrentCGDisplay(CVDisplayLink, CGDirectDisplayID) -> CVReturn](cvdisplaylinksetcurrentcgdisplay(_:_:).md)
  Sets the current display of a display link.
- [func CVDisplayLinkSetCurrentCGDisplayFromOpenGLContext(CVDisplayLink, CGLContextObj, CGLPixelFormatObj) -> CVReturn](cvdisplaylinksetcurrentcgdisplayfromopenglcontext(_:_:_:).md)
  Selects the display link most optimal for the current renderer of an OpenGL context.
- [func CVDisplayLinkSetOutputCallback(CVDisplayLink, CVDisplayLinkOutputCallback?, UnsafeMutableRawPointer?) -> CVReturn](cvdisplaylinksetoutputcallback(_:_:_:).md)
  Sets the renderer output callback function.
- [typealias CVDisplayLinkOutputHandler](cvdisplaylinkoutputhandler.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/cvdisplaylinksetoutputhandler(_:_:))*
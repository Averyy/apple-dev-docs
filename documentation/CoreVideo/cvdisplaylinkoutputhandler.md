# CVDisplayLinkOutputHandler

**Framework**: Core Video  
**Kind**: typealias

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.4+

## Declaration

```swift
typealias CVDisplayLinkOutputHandler = (CVDisplayLink, UnsafePointer<CVTimeStamp>, UnsafePointer<CVTimeStamp>, CVOptionFlags, UnsafeMutablePointer<CVOptionFlags>) -> CVReturn
```

## See Also

- [func CVDisplayLinkSetCurrentCGDisplay(CVDisplayLink, CGDirectDisplayID) -> CVReturn](cvdisplaylinksetcurrentcgdisplay(_:_:).md)
  Sets the current display of a display link.
- [func CVDisplayLinkSetCurrentCGDisplayFromOpenGLContext(CVDisplayLink, CGLContextObj, CGLPixelFormatObj) -> CVReturn](cvdisplaylinksetcurrentcgdisplayfromopenglcontext(_:_:_:).md)
  Selects the display link most optimal for the current renderer of an OpenGL context.
- [func CVDisplayLinkSetOutputCallback(CVDisplayLink, CVDisplayLinkOutputCallback?, UnsafeMutableRawPointer?) -> CVReturn](cvdisplaylinksetoutputcallback(_:_:_:).md)
  Sets the renderer output callback function.
- [func CVDisplayLinkSetOutputHandler(CVDisplayLink, CVDisplayLinkOutputHandler) -> CVReturn](cvdisplaylinksetoutputhandler(_:_:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/cvdisplaylinkoutputhandler)*
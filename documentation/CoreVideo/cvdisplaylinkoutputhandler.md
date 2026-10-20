# CVDisplayLinkOutputHandler

**Framework**: Core Video  
**Kind**: typealias  
**Role**: Type Alias

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.4+

## Declaration

```swift
typealias CVDisplayLinkOutputHandler = @Sendable (CVDisplayLink, UnsafePointer<CVTimeStamp>, UnsafePointer<CVTimeStamp>, CVOptionFlags, UnsafeMutablePointer<CVOptionFlags>) -> CVReturn
```

```c
typedef int (^)(struct __CVDisplayLink *, const CVTimeStamp *, const CVTimeStamp *, unsigned long long, unsigned long long *) CVDisplayLinkOutputHandler;
```

## See Also

### Configuring Display Links
- [func CVDisplayLinkSetCurrentCGDisplay(CVDisplayLink, CGDirectDisplayID) -> CVReturn](./cvdisplaylinksetcurrentcgdisplay%28_,_%29.md)
  Sets the current display of a display link.
- [func CVDisplayLinkSetCurrentCGDisplayFromOpenGLContext(CVDisplayLink, CGLContextObj, CGLPixelFormatObj) -> CVReturn](./cvdisplaylinksetcurrentcgdisplayfromopenglcontext%28_,_,_%29.md)
  Selects the display link most optimal for the current renderer of an OpenGL context.
- [func CVDisplayLinkSetOutputCallback(CVDisplayLink, CVDisplayLinkOutputCallback?, UnsafeMutableRawPointer?) -> CVReturn](./cvdisplaylinksetoutputcallback%28_,_,_%29.md)
  Sets the renderer output callback function.
- [func CVDisplayLinkSetOutputHandler(CVDisplayLink, CVDisplayLinkOutputHandler) -> CVReturn](./cvdisplaylinksetoutputhandler%28_,_%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/cvdisplaylinkoutputhandler)*
# CVDisplayLinkSetOutputHandler(_:_:)

**Framework**: Core Video  
**Kind**: func  
**Role**: Function

**Availability**:
- Mac Catalyst 13.1+ - Deprecated in 18.0
- macOS 10.4+ - Deprecated in 15.0

> **Deprecated**: use NSView.displayLink(target:selector:), NSWindow.displayLink(target:selector:), or NSScreen.displayLink(target:selector:) 

## Declaration

```swift
func CVDisplayLinkSetOutputHandler(_ displayLink: CVDisplayLink, _ handler: @escaping CVDisplayLinkOutputHandler) -> CVReturn
```

```c
extern CVReturn CVDisplayLinkSetOutputHandler(CVDisplayLinkRef displayLink, CVDisplayLinkOutputHandler handler);
```

## See Also

### Configuring Display Links
- [func CVDisplayLinkSetCurrentCGDisplay(CVDisplayLink, CGDirectDisplayID) -> CVReturn](./cvdisplaylinksetcurrentcgdisplay%28_,_%29.md)
  Sets the current display of a display link.
- [func CVDisplayLinkSetCurrentCGDisplayFromOpenGLContext(CVDisplayLink, CGLContextObj, CGLPixelFormatObj) -> CVReturn](./cvdisplaylinksetcurrentcgdisplayfromopenglcontext%28_,_,_%29.md)
  Selects the display link most optimal for the current renderer of an OpenGL context.
- [func CVDisplayLinkSetOutputCallback(CVDisplayLink, CVDisplayLinkOutputCallback?, UnsafeMutableRawPointer?) -> CVReturn](./cvdisplaylinksetoutputcallback%28_,_,_%29.md)
  Sets the renderer output callback function.
- [typealias CVDisplayLinkOutputHandler](./cvdisplaylinkoutputhandler.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/cvdisplaylinksetoutputhandler(_:_:))*
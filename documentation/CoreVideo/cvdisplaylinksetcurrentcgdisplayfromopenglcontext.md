# CVDisplayLinkSetCurrentCGDisplayFromOpenGLContext(_:_:_:)

**Framework**: Core Video  
**Kind**: func

Selects the display link most optimal for the current renderer of an OpenGL context.

**Availability**:
- Mac Catalyst 13.1+
- macOS 10.4+

## Declaration

```swift
func CVDisplayLinkSetCurrentCGDisplayFromOpenGLContext(_ displayLink: CVDisplayLink, _ cglContext: CGLContextObj, _ cglPixelFormat: CGLPixelFormatObj) -> CVReturn
```

#### Return Value

A Core Video result code. See [`Core Video Constants`](core-video-constants.md) for possible values.

#### Discussion

This function chooses the display with the lowest refresh rate.

## Parameters

- `displayLink`: The display link whose current display is to be set.
- `cglContext`: The OpenGL context to retrieve the current renderer from.
- `cglPixelFormat`: The OpenGL pixel format used to create the passed-in OpenGL context.

## See Also

- [func CVDisplayLinkSetCurrentCGDisplay(CVDisplayLink, CGDirectDisplayID) -> CVReturn](cvdisplaylinksetcurrentcgdisplay(_:_:).md)
  Sets the current display of a display link.
- [func CVDisplayLinkSetOutputCallback(CVDisplayLink, CVDisplayLinkOutputCallback?, UnsafeMutableRawPointer?) -> CVReturn](cvdisplaylinksetoutputcallback(_:_:_:).md)
  Sets the renderer output callback function.
- [func CVDisplayLinkSetOutputHandler(CVDisplayLink, CVDisplayLinkOutputHandler) -> CVReturn](cvdisplaylinksetoutputhandler(_:_:).md)
- [typealias CVDisplayLinkOutputHandler](cvdisplaylinkoutputhandler.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/cvdisplaylinksetcurrentcgdisplayfromopenglcontext(_:_:_:))*
# CVDisplayLinkSetCurrentCGDisplay(_:_:)

**Framework**: Core Video  
**Kind**: func

Sets the current display of a display link.

**Availability**:
- Mac Catalyst 13.1+
- macOS 10.4+

## Declaration

```swift
func CVDisplayLinkSetCurrentCGDisplay(_ displayLink: CVDisplayLink, _ displayID: CGDirectDisplayID) -> CVReturn
```

#### Return Value

A Core Video result code. See [`Core Video Constants`](core-video-constants.md) for possible values.

#### Discussion

Although it is safe to call this function on a running display link, a discontinuity may appear in the video timestamp.

## Parameters

- `displayLink`: The display link whose display you want to set.
- `displayID`: The ID of the display to be set.

## See Also

- [func CVDisplayLinkSetCurrentCGDisplayFromOpenGLContext(CVDisplayLink, CGLContextObj, CGLPixelFormatObj) -> CVReturn](cvdisplaylinksetcurrentcgdisplayfromopenglcontext(_:_:_:).md)
  Selects the display link most optimal for the current renderer of an OpenGL context.
- [func CVDisplayLinkSetOutputCallback(CVDisplayLink, CVDisplayLinkOutputCallback?, UnsafeMutableRawPointer?) -> CVReturn](cvdisplaylinksetoutputcallback(_:_:_:).md)
  Sets the renderer output callback function.
- [func CVDisplayLinkSetOutputHandler(CVDisplayLink, CVDisplayLinkOutputHandler) -> CVReturn](cvdisplaylinksetoutputhandler(_:_:).md)
- [typealias CVDisplayLinkOutputHandler](cvdisplaylinkoutputhandler.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/cvdisplaylinksetcurrentcgdisplay(_:_:))*
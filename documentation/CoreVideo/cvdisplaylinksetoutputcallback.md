# CVDisplayLinkSetOutputCallback(_:_:_:)

**Framework**: Core Video  
**Kind**: func

Sets the renderer output callback function.

**Availability**:
- Mac Catalyst 13.1+
- macOS 10.4+

## Declaration

```swift
func CVDisplayLinkSetOutputCallback(_ displayLink: CVDisplayLink, _ callback: CVDisplayLinkOutputCallback?, _ userInfo: UnsafeMutableRawPointer?) -> CVReturn
```

#### Return Value

A Core Video result code. See [`Core Video Constants`](core-video-constants.md) for possible values.

#### Discussion

The display link invokes this callback whenever it wants you to output a frame.

## Parameters

- `displayLink`: The display link whose output callback you want to set.
- `callback`: The callback function to set for this display link. See   for more information about implementing this function.
- `userInfo`: A pointer to user data.

## See Also

- [func CVDisplayLinkSetCurrentCGDisplay(CVDisplayLink, CGDirectDisplayID) -> CVReturn](cvdisplaylinksetcurrentcgdisplay(_:_:).md)
  Sets the current display of a display link.
- [func CVDisplayLinkSetCurrentCGDisplayFromOpenGLContext(CVDisplayLink, CGLContextObj, CGLPixelFormatObj) -> CVReturn](cvdisplaylinksetcurrentcgdisplayfromopenglcontext(_:_:_:).md)
  Selects the display link most optimal for the current renderer of an OpenGL context.
- [func CVDisplayLinkSetOutputHandler(CVDisplayLink, CVDisplayLinkOutputHandler) -> CVReturn](cvdisplaylinksetoutputhandler(_:_:).md)
- [typealias CVDisplayLinkOutputHandler](cvdisplaylinkoutputhandler.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/cvdisplaylinksetoutputcallback(_:_:_:))*
# CVDisplayLinkSetCurrentCGDisplay(_:_:)

**Framework**: Core Video  
**Kind**: func  
**Role**: Function

Sets the current display of a display link.

**Availability**:
- Mac Catalyst 13.1+ - Deprecated in 18.0
- macOS 10.4+ - Deprecated in 15.0

> **Deprecated**: use NSView.displayLink(target:selector:), NSWindow.displayLink(target:selector:), or NSScreen.displayLink(target:selector:) 

## Declaration

```swift
func CVDisplayLinkSetCurrentCGDisplay(_ displayLink: CVDisplayLink, _ displayID: CGDirectDisplayID) -> CVReturn
```

```c
extern CVReturn CVDisplayLinkSetCurrentCGDisplay(CVDisplayLinkRef displayLink, CGDirectDisplayID displayID);
```

#### Return Value

A Core Video result code. See [Core Video Constants](./core-video-constants.md) for possible values.

#### Discussion

Although it is safe to call this function on a running display link, a discontinuity may appear in the video timestamp.

## Parameters

- `displayLink`: The display link whose display you want to set.
- `displayID`: The ID of the display to be set.

## See Also

### Configuring Display Links
- [func CVDisplayLinkSetCurrentCGDisplayFromOpenGLContext(CVDisplayLink, CGLContextObj, CGLPixelFormatObj) -> CVReturn](./cvdisplaylinksetcurrentcgdisplayfromopenglcontext%28_,_,_%29.md)
  Selects the display link most optimal for the current renderer of an OpenGL context.
- [func CVDisplayLinkSetOutputCallback(CVDisplayLink, CVDisplayLinkOutputCallback?, UnsafeMutableRawPointer?) -> CVReturn](./cvdisplaylinksetoutputcallback%28_,_,_%29.md)
  Sets the renderer output callback function.
- [func CVDisplayLinkSetOutputHandler(CVDisplayLink, CVDisplayLinkOutputHandler) -> CVReturn](./cvdisplaylinksetoutputhandler%28_,_%29.md)
- [typealias CVDisplayLinkOutputHandler](./cvdisplaylinkoutputhandler.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/cvdisplaylinksetcurrentcgdisplay(_:_:))*
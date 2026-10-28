# CVDisplayLinkSetOutputCallback(_:_:_:)

**Framework**: Core Video  
**Kind**: func  
**Role**: Function

Sets the renderer output callback function.

**Availability**:
- Mac Catalyst 13.1+ - Deprecated in 18.0
- macOS 10.4+ - Deprecated in 15.0

> **Deprecated**: use NSView.displayLink(target:selector:), NSWindow.displayLink(target:selector:), or NSScreen.displayLink(target:selector:) 

## Declaration

```swift
func CVDisplayLinkSetOutputCallback(_ displayLink: CVDisplayLink, _ callback: CVDisplayLinkOutputCallback?, _ userInfo: UnsafeMutableRawPointer?) -> CVReturn
```

```c
extern CVReturn CVDisplayLinkSetOutputCallback(CVDisplayLinkRef displayLink, CVDisplayLinkOutputCallback callback, void *userInfo);
```

## Return Value

A Core Video result code. See [Core Video Constants](./core-video-constants.md) for possible values.

## Discussion

The display link invokes this callback whenever it wants you to output a frame.

## Parameters

- `displayLink`: The display link whose output callback you want to set.
- `callback`: The callback function to set for this display link. See [`CVDisplayLinkOutputCallback`](./cvdisplaylinkoutputcallback.md) for more information about implementing this function.
- `userInfo`: A pointer to user data.

## See Also

### Configuring Display Links
- [func CVDisplayLinkSetCurrentCGDisplay(CVDisplayLink, CGDirectDisplayID) -> CVReturn](./cvdisplaylinksetcurrentcgdisplay%28_,_%29.md)
  Sets the current display of a display link.
- [func CVDisplayLinkSetCurrentCGDisplayFromOpenGLContext(CVDisplayLink, CGLContextObj, CGLPixelFormatObj) -> CVReturn](./cvdisplaylinksetcurrentcgdisplayfromopenglcontext%28_,_,_%29.md)
  Selects the display link most optimal for the current renderer of an OpenGL context.
- [func CVDisplayLinkSetOutputHandler(CVDisplayLink, CVDisplayLinkOutputHandler) -> CVReturn](./cvdisplaylinksetoutputhandler%28_,_%29.md)
- [typealias CVDisplayLinkOutputHandler](./cvdisplaylinkoutputhandler.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/cvdisplaylinksetoutputcallback(_:_:_:))*
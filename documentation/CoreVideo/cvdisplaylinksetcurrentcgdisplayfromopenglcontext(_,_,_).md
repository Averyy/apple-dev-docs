# CVDisplayLinkSetCurrentCGDisplayFromOpenGLContext(_:_:_:)

**Framework**: Core Video  
**Kind**: func  
**Role**: Function

Selects the display link most optimal for the current renderer of an OpenGL context.

**Availability**:
- Mac Catalyst 13.1+ - Deprecated in 18.0
- macOS 10.4+ - Deprecated in 15.0

> **Deprecated**: use NSView.displayLink(target:selector:), NSWindow.displayLink(target:selector:), or NSScreen.displayLink(target:selector:) 

## Declaration

```swift
func CVDisplayLinkSetCurrentCGDisplayFromOpenGLContext(_ displayLink: CVDisplayLink, _ cglContext: CGLContextObj, _ cglPixelFormat: CGLPixelFormatObj) -> CVReturn
```

```c
extern CVReturn CVDisplayLinkSetCurrentCGDisplayFromOpenGLContext(CVDisplayLinkRef displayLink, CGLContextObj cglContext, CGLPixelFormatObj cglPixelFormat);
```

## Return Value

A Core Video result code. See [Core Video Constants](./core-video-constants.md) for possible values.

## Discussion

This function chooses the display with the lowest refresh rate.

## Parameters

- `displayLink`: The display link whose current display is to be set.
- `cglContext`: The OpenGL context to retrieve the current renderer from.
- `cglPixelFormat`: The OpenGL pixel format used to create the passed-in OpenGL context.

## See Also

### Configuring Display Links
- [func CVDisplayLinkSetCurrentCGDisplay(CVDisplayLink, CGDirectDisplayID) -> CVReturn](./cvdisplaylinksetcurrentcgdisplay%28_,_%29.md)
  Sets the current display of a display link.
- [func CVDisplayLinkSetOutputCallback(CVDisplayLink, CVDisplayLinkOutputCallback?, UnsafeMutableRawPointer?) -> CVReturn](./cvdisplaylinksetoutputcallback%28_,_,_%29.md)
  Sets the renderer output callback function.
- [func CVDisplayLinkSetOutputHandler(CVDisplayLink, CVDisplayLinkOutputHandler) -> CVReturn](./cvdisplaylinksetoutputhandler%28_,_%29.md)
- [typealias CVDisplayLinkOutputHandler](./cvdisplaylinkoutputhandler.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/cvdisplaylinksetcurrentcgdisplayfromopenglcontext(_:_:_:))*
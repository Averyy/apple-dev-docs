# CVDisplayLinkCreateWithOpenGLDisplayMask(_:_:)

**Framework**: Core Video  
**Kind**: func  
**Role**: Function

Creates a display link from an OpenGL display mask.

**Availability**:
- Mac Catalyst 13.1+ - Deprecated in 18.0
- macOS 10.4+ - Deprecated in 15.0

> **Deprecated**: use NSView.displayLink(target:selector:), NSWindow.displayLink(target:selector:), or NSScreen.displayLink(target:selector:) 

## Declaration

```swift
func CVDisplayLinkCreateWithOpenGLDisplayMask(_ mask: CGOpenGLDisplayMask, _ displayLinkOut: UnsafeMutablePointer<CVDisplayLink?>) -> CVReturn
```

```c
extern CVReturn CVDisplayLinkCreateWithOpenGLDisplayMask(CGOpenGLDisplayMask mask, CVDisplayLinkRef*displayLinkOut);
```

#### Return Value

A Core Video result code. See [Core Video Constants](./core-video-constants.md) for possible values.

#### Discussion

Using this function avoids having to call the Core Graphics function `CGOpenGLDisplayMaskToDisplayID`.

## Parameters

- `mask`: The OpenGL display mask describing the available displays.
- `displayLinkOut`: On output, `displayLinkOut` points to the newly created display link.

## See Also

### Creating Display Links
- [func CVDisplayLinkCreateWithCGDisplay(CGDirectDisplayID, UnsafeMutablePointer<CVDisplayLink?>) -> CVReturn](./cvdisplaylinkcreatewithcgdisplay%28_,_%29.md)
  Creates a display link for a single display.
- [func CVDisplayLinkCreateWithCGDisplays(UnsafeMutablePointer<CGDirectDisplayID>, CFIndex, UnsafeMutablePointer<CVDisplayLink?>) -> CVReturn](./cvdisplaylinkcreatewithcgdisplays%28_,_,_%29.md)
  Creates a display link for an array of displays.
- [func CVDisplayLinkCreateWithActiveCGDisplays(UnsafeMutablePointer<CVDisplayLink?>) -> CVReturn](./cvdisplaylinkcreatewithactivecgdisplays%28_%29.md)
  Creates a display link capable of being used with all active displays.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/cvdisplaylinkcreatewithopengldisplaymask(_:_:))*
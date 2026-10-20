# CVDisplayLinkCreateWithCGDisplay(_:_:)

**Framework**: Core Video  
**Kind**: func  
**Role**: Function

Creates a display link for a single display.

**Availability**:
- Mac Catalyst 13.1+ - Deprecated in 18.0
- macOS 10.4+ - Deprecated in 15.0

> **Deprecated**: use NSView.displayLink(target:selector:), NSWindow.displayLink(target:selector:), or NSScreen.displayLink(target:selector:) 

## Declaration

```swift
func CVDisplayLinkCreateWithCGDisplay(_ displayID: CGDirectDisplayID, _ displayLinkOut: UnsafeMutablePointer<CVDisplayLink?>) -> CVReturn
```

```c
extern CVReturn CVDisplayLinkCreateWithCGDisplay(CGDirectDisplayID displayID, CVDisplayLinkRef*displayLinkOut);
```

#### Return Value

A Core Video result code. See [Core Video Constants](./core-video-constants.md) for possible values.

#### Discussion

Use this call to create a display link for a single display. For more information on the display identifier type, see [`CGDirectDisplayID`](../CoreGraphics/cgdirectdisplayid.md).

## Parameters

- `displayID`: The Core Graphics ID of the target display.
- `displayLinkOut`: On output, `displayLinkOut` points to the newly created display link.

## See Also

### Creating Display Links
- [func CVDisplayLinkCreateWithCGDisplays(UnsafeMutablePointer<CGDirectDisplayID>, CFIndex, UnsafeMutablePointer<CVDisplayLink?>) -> CVReturn](./cvdisplaylinkcreatewithcgdisplays%28_,_,_%29.md)
  Creates a display link for an array of displays.
- [func CVDisplayLinkCreateWithActiveCGDisplays(UnsafeMutablePointer<CVDisplayLink?>) -> CVReturn](./cvdisplaylinkcreatewithactivecgdisplays%28_%29.md)
  Creates a display link capable of being used with all active displays.
- [func CVDisplayLinkCreateWithOpenGLDisplayMask(CGOpenGLDisplayMask, UnsafeMutablePointer<CVDisplayLink?>) -> CVReturn](./cvdisplaylinkcreatewithopengldisplaymask%28_,_%29.md)
  Creates a display link from an OpenGL display mask.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/cvdisplaylinkcreatewithcgdisplay(_:_:))*
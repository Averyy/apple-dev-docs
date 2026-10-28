# CVDisplayLinkCreateWithActiveCGDisplays(_:)

**Framework**: Core Video  
**Kind**: func  
**Role**: Function

Creates a display link capable of being used with all active displays.

**Availability**:
- Mac Catalyst 13.1+ - Deprecated in 18.0
- macOS 10.4+ - Deprecated in 15.0

> **Deprecated**: use NSView.displayLink(target:selector:), NSWindow.displayLink(target:selector:), or NSScreen.displayLink(target:selector:) 

## Declaration

```swift
func CVDisplayLinkCreateWithActiveCGDisplays(_ displayLinkOut: UnsafeMutablePointer<CVDisplayLink?>) -> CVReturn
```

```c
extern CVReturn CVDisplayLinkCreateWithActiveCGDisplays(CVDisplayLinkRef*displayLinkOut);
```

## Return Value

A Core Video result code. See [Core Video Constants](./core-video-constants.md) for possible values.

## Discussion

`CVDisplayLinkCreateWithActiveCGDisplays` determines the displays actively used by the host computer and creates a display link compatible with all of them. For most applications, calling this function is the most convenient way to create a display link. After creation, you can assign the display link to any active display by calling the [`CVDisplayLinkSetCurrentCGDisplay(_:_:)`](./cvdisplaylinksetcurrentcgdisplay%28_,_%29.md) function.

## Parameters

- `displayLinkOut`: On output, `displayLinkOut` points to the newly created display link.

## See Also

### Creating Display Links
- [func CVDisplayLinkCreateWithCGDisplay(CGDirectDisplayID, UnsafeMutablePointer<CVDisplayLink?>) -> CVReturn](./cvdisplaylinkcreatewithcgdisplay%28_,_%29.md)
  Creates a display link for a single display.
- [func CVDisplayLinkCreateWithCGDisplays(UnsafeMutablePointer<CGDirectDisplayID>, CFIndex, UnsafeMutablePointer<CVDisplayLink?>) -> CVReturn](./cvdisplaylinkcreatewithcgdisplays%28_,_,_%29.md)
  Creates a display link for an array of displays.
- [func CVDisplayLinkCreateWithOpenGLDisplayMask(CGOpenGLDisplayMask, UnsafeMutablePointer<CVDisplayLink?>) -> CVReturn](./cvdisplaylinkcreatewithopengldisplaymask%28_,_%29.md)
  Creates a display link from an OpenGL display mask.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/cvdisplaylinkcreatewithactivecgdisplays(_:))*
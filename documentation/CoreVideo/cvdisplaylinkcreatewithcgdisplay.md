# CVDisplayLinkCreateWithCGDisplay(_:_:)

**Framework**: Core Video  
**Kind**: func

Creates a display link for a single display.

**Availability**:
- Mac Catalyst 13.1+
- macOS 10.4+

## Declaration

```swift
func CVDisplayLinkCreateWithCGDisplay(_ displayID: CGDirectDisplayID, _ displayLinkOut: UnsafeMutablePointer<CVDisplayLink?>) -> CVReturn
```

#### Return Value

A Core Video result code. See [`Core Video Constants`](core-video-constants.md) for possible values.

#### Discussion

Use this call to create a display link for a single display. For more information on the display identifier type, see [`CGDirectDisplayID`](https://developer.apple.com/documentation/CoreGraphics/CGDirectDisplayID).

## Parameters

- `displayID`: The Core Graphics ID of the target display.
- `displayLinkOut`: On output,   points to the newly created display link.

## See Also

- [func CVDisplayLinkCreateWithCGDisplays(UnsafeMutablePointer<CGDirectDisplayID>, CFIndex, UnsafeMutablePointer<CVDisplayLink?>) -> CVReturn](cvdisplaylinkcreatewithcgdisplays(_:_:_:).md)
  Creates a display link for an array of displays.
- [func CVDisplayLinkCreateWithActiveCGDisplays(UnsafeMutablePointer<CVDisplayLink?>) -> CVReturn](cvdisplaylinkcreatewithactivecgdisplays(_:).md)
  Creates a display link capable of being used with all active displays.
- [func CVDisplayLinkCreateWithOpenGLDisplayMask(CGOpenGLDisplayMask, UnsafeMutablePointer<CVDisplayLink?>) -> CVReturn](cvdisplaylinkcreatewithopengldisplaymask(_:_:).md)
  Creates a display link from an OpenGL display mask.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/cvdisplaylinkcreatewithcgdisplay(_:_:))*
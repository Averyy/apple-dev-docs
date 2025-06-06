# CVDisplayLinkCreateWithOpenGLDisplayMask(_:_:)

**Framework**: Core Video  
**Kind**: func

Creates a display link from an OpenGL display mask.

**Availability**:
- Mac Catalyst 13.1+
- macOS 10.4+

## Declaration

```swift
func CVDisplayLinkCreateWithOpenGLDisplayMask(_ mask: CGOpenGLDisplayMask, _ displayLinkOut: UnsafeMutablePointer<CVDisplayLink?>) -> CVReturn
```

#### Return Value

A Core Video result code. See [`Core Video Constants`](core-video-constants.md) for possible values.

#### Discussion

Using this function avoids having to call the Core Graphics function `CGOpenGLDisplayMaskToDisplayID`.

## Parameters

- `mask`: The OpenGL display mask describing the available displays.
- `displayLinkOut`: On output,   points to the newly created display link.

## See Also

- [func CVDisplayLinkCreateWithCGDisplay(CGDirectDisplayID, UnsafeMutablePointer<CVDisplayLink?>) -> CVReturn](cvdisplaylinkcreatewithcgdisplay(_:_:).md)
  Creates a display link for a single display.
- [func CVDisplayLinkCreateWithCGDisplays(UnsafeMutablePointer<CGDirectDisplayID>, CFIndex, UnsafeMutablePointer<CVDisplayLink?>) -> CVReturn](cvdisplaylinkcreatewithcgdisplays(_:_:_:).md)
  Creates a display link for an array of displays.
- [func CVDisplayLinkCreateWithActiveCGDisplays(UnsafeMutablePointer<CVDisplayLink?>) -> CVReturn](cvdisplaylinkcreatewithactivecgdisplays(_:).md)
  Creates a display link capable of being used with all active displays.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/cvdisplaylinkcreatewithopengldisplaymask(_:_:))*
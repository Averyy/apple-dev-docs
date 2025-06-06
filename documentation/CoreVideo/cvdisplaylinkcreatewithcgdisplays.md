# CVDisplayLinkCreateWithCGDisplays(_:_:_:)

**Framework**: Core Video  
**Kind**: func

Creates a display link for an array of displays.

**Availability**:
- Mac Catalyst 13.1+
- macOS 10.4+

## Declaration

```swift
func CVDisplayLinkCreateWithCGDisplays(_ displayArray: UnsafeMutablePointer<CGDirectDisplayID>, _ count: CFIndex, _ displayLinkOut: UnsafeMutablePointer<CVDisplayLink?>) -> CVReturn
```

#### Return Value

A Core Video result code. See [`Core Video Constants`](core-video-constants.md) for possible values.

#### Discussion

Use this call to create a display link for a set of displays identified by the Core Graphics display IDs. For more information on the display identifier type, see [`CGDirectDisplayID`](https://developer.apple.com/documentation/CoreGraphics/CGDirectDisplayID).

## Parameters

- `displayArray`: A pointer to an array of Core Graphics display IDs representing all the active monitors you want to use with this display link.
- `count`: The number of displays in the display array.
- `displayLinkOut`: On output,   points to the newly created display link.

## See Also

- [func CVDisplayLinkCreateWithCGDisplay(CGDirectDisplayID, UnsafeMutablePointer<CVDisplayLink?>) -> CVReturn](cvdisplaylinkcreatewithcgdisplay(_:_:).md)
  Creates a display link for a single display.
- [func CVDisplayLinkCreateWithActiveCGDisplays(UnsafeMutablePointer<CVDisplayLink?>) -> CVReturn](cvdisplaylinkcreatewithactivecgdisplays(_:).md)
  Creates a display link capable of being used with all active displays.
- [func CVDisplayLinkCreateWithOpenGLDisplayMask(CGOpenGLDisplayMask, UnsafeMutablePointer<CVDisplayLink?>) -> CVReturn](cvdisplaylinkcreatewithopengldisplaymask(_:_:).md)
  Creates a display link from an OpenGL display mask.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/cvdisplaylinkcreatewithcgdisplays(_:_:_:))*
# CVDisplayLinkCreateWithActiveCGDisplays(_:)

**Framework**: Core Video  
**Kind**: func

Creates a display link capable of being used with all active displays.

**Availability**:
- Mac Catalyst 13.1+
- macOS 10.4+

## Declaration

```swift
func CVDisplayLinkCreateWithActiveCGDisplays(_ displayLinkOut: UnsafeMutablePointer<CVDisplayLink?>) -> CVReturn
```

#### Return Value

A Core Video result code. See [`Core Video Constants`](core-video-constants.md) for possible values.

#### Discussion

`CVDisplayLinkCreateWithActiveCGDisplays` determines the displays actively used by the host computer and creates a display link compatible with all of them. For most applications, calling this function is the most convenient way to create a display link. After creation, you can assign the display link to any active display by calling the [`CVDisplayLinkSetCurrentCGDisplay(_:_:)`](cvdisplaylinksetcurrentcgdisplay(_:_:).md) function.

## Parameters

- `displayLinkOut`: On output,   points to the newly created display link.

## See Also

- [func CVDisplayLinkCreateWithCGDisplay(CGDirectDisplayID, UnsafeMutablePointer<CVDisplayLink?>) -> CVReturn](cvdisplaylinkcreatewithcgdisplay(_:_:).md)
  Creates a display link for a single display.
- [func CVDisplayLinkCreateWithCGDisplays(UnsafeMutablePointer<CGDirectDisplayID>, CFIndex, UnsafeMutablePointer<CVDisplayLink?>) -> CVReturn](cvdisplaylinkcreatewithcgdisplays(_:_:_:).md)
  Creates a display link for an array of displays.
- [func CVDisplayLinkCreateWithOpenGLDisplayMask(CGOpenGLDisplayMask, UnsafeMutablePointer<CVDisplayLink?>) -> CVReturn](cvdisplaylinkcreatewithopengldisplaymask(_:_:).md)
  Creates a display link from an OpenGL display mask.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/cvdisplaylinkcreatewithactivecgdisplays(_:))*
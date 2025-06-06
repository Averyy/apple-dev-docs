# contentRect(forFrameRect:)

**Framework**: AppKit  
**Kind**: method

Returns the window’s content rectangle with a given frame rectangle.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func contentRect(forFrameRect frameRect: NSRect) -> NSRect
```

#### Return Value

The window’s content rectangle, expressed in screen coordinates, with f`rameRect`.

#### Discussion

The window uses its current style mask in computing the content rectangle. See [`NSWindow.StyleMask`](nswindow/stylemask-swift.struct.md) for a list of style mask values. The main advantage of this instance-method counterpart to [`contentRect(forFrameRect:styleMask:)`](nswindow/contentrect(forframerect:stylemask:).md) is that it allows you to take toolbars into account when converting between content and frame rectangles. (The toolbar is not included in the content rectangle.)

## Parameters

- `frameRect`: The frame rectangle for the window expressed in screen coordinates.

## See Also

- [class func contentRect(forFrameRect: NSRect, styleMask: NSWindow.StyleMask) -> NSRect](nswindow/contentrect(forframerect:stylemask:).md)
  Returns the content rectangle used by a window with a given frame rectangle and window style.
- [class func frameRect(forContentRect: NSRect, styleMask: NSWindow.StyleMask) -> NSRect](nswindow/framerect(forcontentrect:stylemask:).md)
  Returns the frame rectangle used by a window with a given content rectangle and window style.
- [class func minFrameWidth(withTitle: String, styleMask: NSWindow.StyleMask) -> CGFloat](nswindow/minframewidth(withtitle:stylemask:).md)
  Returns the minimum width a window’s frame rectangle must have for it to display a title, with a given window style.
- [func frameRect(forContentRect: NSRect) -> NSRect](nswindow/framerect(forcontentrect:).md)
  Returns the window’s frame rectangle with a given content rectangle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindow/contentrect(forframerect:))*
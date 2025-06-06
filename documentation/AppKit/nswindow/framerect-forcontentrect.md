# frameRect(forContentRect:)

**Framework**: AppKit  
**Kind**: method

Returns the window’s frame rectangle with a given content rectangle.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func frameRect(forContentRect contentRect: NSRect) -> NSRect
```

#### Return Value

The window’s frame rectangle, expressed in screen coordinates, with `contentRect`.

#### Discussion

The window uses its current style mask in computing the frame rectangle. See [`NSWindow.StyleMask`](nswindow/stylemask-swift.struct.md) for a list of style mask values. The major advantage of this instance-method counterpart to [`frameRect(forContentRect:styleMask:)`](nswindow/framerect(forcontentrect:stylemask:).md) is that it allows you to take toolbars into account when converting between content and frame rectangles. (The toolbar is included in the frame rectangle but not the content rectangle.)

## Parameters

- `contentRect`: The content rectangle for the window expressed in screen coordinates.

## See Also

- [class func contentRect(forFrameRect: NSRect, styleMask: NSWindow.StyleMask) -> NSRect](nswindow/contentrect(forframerect:stylemask:).md)
  Returns the content rectangle used by a window with a given frame rectangle and window style.
- [class func frameRect(forContentRect: NSRect, styleMask: NSWindow.StyleMask) -> NSRect](nswindow/framerect(forcontentrect:stylemask:).md)
  Returns the frame rectangle used by a window with a given content rectangle and window style.
- [class func minFrameWidth(withTitle: String, styleMask: NSWindow.StyleMask) -> CGFloat](nswindow/minframewidth(withtitle:stylemask:).md)
  Returns the minimum width a window’s frame rectangle must have for it to display a title, with a given window style.
- [func contentRect(forFrameRect: NSRect) -> NSRect](nswindow/contentrect(forframerect:).md)
  Returns the window’s content rectangle with a given frame rectangle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindow/framerect(forcontentrect:))*
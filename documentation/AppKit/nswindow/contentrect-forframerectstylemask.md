# contentRect(forFrameRect:styleMask:)

**Framework**: AppKit  
**Kind**: method

Returns the content rectangle used by a window with a given frame rectangle and window style.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
class func contentRect(forFrameRect fRect: NSRect, styleMask style: NSWindow.StyleMask) -> NSRect
```

#### Return Value

The content rectangle, expressed in screen coordinates, used by the window with `fRect` and `style`.

#### Discussion

When a `NSWindow` instance is available, you should use [`contentRect(forFrameRect:)`](nswindow/contentrect(forframerect:).md) instead of this method.

## Parameters

- `fRect`: The frame rectangle for the window expressed in screen coordinates.
- `style`: The window style for the window. See   for a list of style mask values.

## See Also

- [class func frameRect(forContentRect: NSRect, styleMask: NSWindow.StyleMask) -> NSRect](nswindow/framerect(forcontentrect:stylemask:).md)
  Returns the frame rectangle used by a window with a given content rectangle and window style.
- [class func minFrameWidth(withTitle: String, styleMask: NSWindow.StyleMask) -> CGFloat](nswindow/minframewidth(withtitle:stylemask:).md)
  Returns the minimum width a window’s frame rectangle must have for it to display a title, with a given window style.
- [func contentRect(forFrameRect: NSRect) -> NSRect](nswindow/contentrect(forframerect:).md)
  Returns the window’s content rectangle with a given frame rectangle.
- [func frameRect(forContentRect: NSRect) -> NSRect](nswindow/framerect(forcontentrect:).md)
  Returns the window’s frame rectangle with a given content rectangle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindow/contentrect(forframerect:stylemask:))*
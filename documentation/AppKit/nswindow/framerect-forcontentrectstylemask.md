# frameRect(forContentRect:styleMask:)

**Framework**: AppKit  
**Kind**: method

Returns the frame rectangle used by a window with a given content rectangle and window style.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
class func frameRect(forContentRect cRect: NSRect, styleMask style: NSWindow.StyleMask) -> NSRect
```

#### Return Value

The frame rectangle, expressed in screen coordinates, used by the window with `cRect` and `style`.

#### Discussion

When a `NSWindow` instance is available, you should use [`frameRect(forContentRect:)`](nswindow/framerect(forcontentrect:).md) instead of this method.

## Parameters

- `cRect`: The content rectangle for a window expressed in screen coordinates.
- `style`: The window style for the window. See   for a list of style mask values.

## See Also

- [class func contentRect(forFrameRect: NSRect, styleMask: NSWindow.StyleMask) -> NSRect](nswindow/contentrect(forframerect:stylemask:).md)
  Returns the content rectangle used by a window with a given frame rectangle and window style.
- [class func minFrameWidth(withTitle: String, styleMask: NSWindow.StyleMask) -> CGFloat](nswindow/minframewidth(withtitle:stylemask:).md)
  Returns the minimum width a window’s frame rectangle must have for it to display a title, with a given window style.
- [func contentRect(forFrameRect: NSRect) -> NSRect](nswindow/contentrect(forframerect:).md)
  Returns the window’s content rectangle with a given frame rectangle.
- [func frameRect(forContentRect: NSRect) -> NSRect](nswindow/framerect(forcontentrect:).md)
  Returns the window’s frame rectangle with a given content rectangle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindow/framerect(forcontentrect:stylemask:))*
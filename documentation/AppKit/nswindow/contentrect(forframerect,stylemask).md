# contentRect(forFrameRect:styleMask:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Type Method

Returns the content rectangle used by a window with a given frame rectangle and window style.

**Availability**:
- macOS

## Declaration

```swift
class func contentRect(forFrameRect fRect: NSRect, styleMask style: NSWindow.StyleMask) -> NSRect
```

```objc
+ (NSRect) contentRectForFrameRect:(NSRect) fRect styleMask:(NSWindowStyleMask) style;
```

#### Return Value

The content rectangle, expressed in screen coordinates, used by the window with `fRect` and `style`.

#### Discussion

When a `NSWindow` instance is available, you should use [`contentRect(forFrameRect:)`](./contentrect%28forframerect%29.md) instead of this method.

## Parameters

- `fRect`: The frame rectangle for the window expressed in screen coordinates.
- `style`: The window style for the window. See [`NSWindow.StyleMask`](./stylemask-swift.struct.md) for a list of style mask values.

## See Also

### Getting Layout Information
- [class func frameRect(forContentRect: NSRect, styleMask: NSWindow.StyleMask) -> NSRect](./framerect%28forcontentrect,stylemask%29.md)
  Returns the frame rectangle used by a window with a given content rectangle and window style.
- [class func minFrameWidth(withTitle: String, styleMask: NSWindow.StyleMask) -> CGFloat](./minframewidth%28withtitle,stylemask%29.md)
  Returns the minimum width a window’s frame rectangle must have for it to display a title, with a given window style.
- [func contentRect(forFrameRect: NSRect) -> NSRect](./contentrect%28forframerect%29.md)
  Returns the window’s content rectangle with a given frame rectangle.
- [func frameRect(forContentRect: NSRect) -> NSRect](./framerect%28forcontentrect%29.md)
  Returns the window’s frame rectangle with a given content rectangle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindow/contentrect(forframerect:stylemask:))*
# frameRect(forContentRect:styleMask:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Type Method

Returns the frame rectangle used by a window with a given content rectangle and window style.

**Availability**:
- macOS

## Declaration

```swift
class func frameRect(forContentRect cRect: NSRect, styleMask style: NSWindow.StyleMask) -> NSRect
```

```objc
+ (NSRect) frameRectForContentRect:(NSRect) cRect styleMask:(NSWindowStyleMask) style;
```

#### Return Value

The frame rectangle, expressed in screen coordinates, used by the window with `cRect` and `style`.

#### Discussion

When a `NSWindow` instance is available, you should use [`frameRect(forContentRect:)`](./framerect%28forcontentrect%29.md) instead of this method.

## Parameters

- `cRect`: The content rectangle for a window expressed in screen coordinates.
- `style`: The window style for the window. See [`NSWindow.StyleMask`](./stylemask-swift.struct.md) for a list of style mask values.

## See Also

### Getting Layout Information
- [class func contentRect(forFrameRect: NSRect, styleMask: NSWindow.StyleMask) -> NSRect](./contentrect%28forframerect,stylemask%29.md)
  Returns the content rectangle used by a window with a given frame rectangle and window style.
- [class func minFrameWidth(withTitle: String, styleMask: NSWindow.StyleMask) -> CGFloat](./minframewidth%28withtitle,stylemask%29.md)
  Returns the minimum width a window’s frame rectangle must have for it to display a title, with a given window style.
- [func contentRect(forFrameRect: NSRect) -> NSRect](./contentrect%28forframerect%29.md)
  Returns the window’s content rectangle with a given frame rectangle.
- [func frameRect(forContentRect: NSRect) -> NSRect](./framerect%28forcontentrect%29.md)
  Returns the window’s frame rectangle with a given content rectangle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindow/framerect(forcontentrect:stylemask:))*
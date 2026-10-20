# minFrameWidth(withTitle:styleMask:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Type Method

Returns the minimum width a window’s frame rectangle must have for it to display a title, with a given window style.

**Availability**:
- macOS

## Declaration

```swift
class func minFrameWidth(withTitle title: String, styleMask style: NSWindow.StyleMask) -> CGFloat
```

```objc
+ (CGFloat) minFrameWidthWithTitle:(NSString *) title styleMask:(NSWindowStyleMask) style;
```

#### Return Value

The minimum width of the window’s frame, using `style`, in order to display `title`.

## Parameters

- `title`: The title for the window.
- `style`: The window style for the window. See [`NSWindow.StyleMask`](./stylemask-swift.struct.md) for a list of style mask values.

## See Also

### Getting Layout Information
- [class func contentRect(forFrameRect: NSRect, styleMask: NSWindow.StyleMask) -> NSRect](./contentrect%28forframerect,stylemask%29.md)
  Returns the content rectangle used by a window with a given frame rectangle and window style.
- [class func frameRect(forContentRect: NSRect, styleMask: NSWindow.StyleMask) -> NSRect](./framerect%28forcontentrect,stylemask%29.md)
  Returns the frame rectangle used by a window with a given content rectangle and window style.
- [func contentRect(forFrameRect: NSRect) -> NSRect](./contentrect%28forframerect%29.md)
  Returns the window’s content rectangle with a given frame rectangle.
- [func frameRect(forContentRect: NSRect) -> NSRect](./framerect%28forcontentrect%29.md)
  Returns the window’s frame rectangle with a given content rectangle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindow/minframewidth(withtitle:stylemask:))*
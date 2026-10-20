# frameRect(forContentRect:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns the window’s frame rectangle with a given content rectangle.

**Availability**:
- macOS

## Declaration

```swift
func frameRect(forContentRect contentRect: NSRect) -> NSRect
```

```objc
- (NSRect) frameRectForContentRect:(NSRect) contentRect;
```

#### Return Value

The window’s frame rectangle, expressed in screen coordinates, with `contentRect`.

#### Discussion

The window uses its current style mask in computing the frame rectangle. See [`NSWindow.StyleMask`](./stylemask-swift.struct.md) for a list of style mask values. The major advantage of this instance-method counterpart to [`frameRect(forContentRect:styleMask:)`](./framerect%28forcontentrect,stylemask%29.md) is that it allows you to take toolbars into account when converting between content and frame rectangles. (The toolbar is included in the frame rectangle but not the content rectangle.)

## Parameters

- `contentRect`: The content rectangle for the window expressed in screen coordinates.

## See Also

### Getting Layout Information
- [class func contentRect(forFrameRect: NSRect, styleMask: NSWindow.StyleMask) -> NSRect](./contentrect%28forframerect,stylemask%29.md)
  Returns the content rectangle used by a window with a given frame rectangle and window style.
- [class func frameRect(forContentRect: NSRect, styleMask: NSWindow.StyleMask) -> NSRect](./framerect%28forcontentrect,stylemask%29.md)
  Returns the frame rectangle used by a window with a given content rectangle and window style.
- [class func minFrameWidth(withTitle: String, styleMask: NSWindow.StyleMask) -> CGFloat](./minframewidth%28withtitle,stylemask%29.md)
  Returns the minimum width a window’s frame rectangle must have for it to display a title, with a given window style.
- [func contentRect(forFrameRect: NSRect) -> NSRect](./contentrect%28forframerect%29.md)
  Returns the window’s content rectangle with a given frame rectangle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindow/framerect(forcontentrect:))*
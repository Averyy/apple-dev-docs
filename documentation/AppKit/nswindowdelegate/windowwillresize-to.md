# windowWillResize(_:to:)

**Framework**: AppKit  
**Kind**: method

Tells the delegate that the window is being resized (whether by the user or through one of the `setFrame...` methods other than [`setFrame(_:display:)`](nswindow/setframe(_:display:).md)).

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
optional func windowWillResize(_ sender: NSWindow, to frameSize: NSSize) -> NSSize
```

#### Return Value

A custom size to which the specified window will be resized.

#### Discussion

The  `frameSize` contains the size (in screen coordinates) `sender` will be resized to. To resize to a different size, simply return the desired size from this method; to avoid resizing, return the current size. `sender`’s minimum and maximum size constraints have already been applied when this method is called.

While the user is resizing a window, the delegate is sent a series of [`windowWillResize(_:to:)`](nswindowdelegate/windowwillresize(_:to:).md) messages as the window’s frame continues to change size.

## Parameters

- `sender`: The window being resized.
- `frameSize`: The size to which the specified window is being resized.

## See Also

- [func windowDidResize(Notification)](nswindowdelegate/windowdidresize(_:).md)
  Tells the delegate that the window has been resized.
- [func windowWillStartLiveResize(Notification)](nswindowdelegate/windowwillstartliveresize(_:).md)
  Tells the delegate that the window is about to be live resized.
- [func windowDidEndLiveResize(Notification)](nswindowdelegate/windowdidendliveresize(_:).md)
  Tells the delegate that a live resize operation on the window has ended.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindowdelegate/windowwillresize(_:to:))*
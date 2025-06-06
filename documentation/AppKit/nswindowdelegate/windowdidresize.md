# windowDidResize(_:)

**Framework**: AppKit  
**Kind**: method

Tells the delegate that the window has been resized.

**Availability**:
- macOS 10.10+

## Declaration

```swift
@MainActor
optional func windowDidResize(_ notification: Notification)
```

#### Discussion

You can retrieve the window object in question by sending [`object`](https://developer.apple.com/documentation/foundation/nsnotification/1414469-object) to `notification`.

## Parameters

- `notification`: A notification named  .

## See Also

- [func windowWillResize(NSWindow, to: NSSize) -> NSSize](nswindowdelegate/windowwillresize(_:to:).md)
  Tells the delegate that the window is being resized (whether by the user or through one of the `setFrame...` methods other than [`setFrame(_:display:)`](nswindow/setframe(_:display:).md)).
- [func windowWillStartLiveResize(Notification)](nswindowdelegate/windowwillstartliveresize(_:).md)
  Tells the delegate that the window is about to be live resized.
- [func windowDidEndLiveResize(Notification)](nswindowdelegate/windowdidendliveresize(_:).md)
  Tells the delegate that a live resize operation on the window has ended.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindowdelegate/windowdidresize(_:))*
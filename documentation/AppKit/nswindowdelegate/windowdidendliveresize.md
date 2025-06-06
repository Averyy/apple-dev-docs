# windowDidEndLiveResize(_:)

**Framework**: AppKit  
**Kind**: method

Tells the delegate that a live resize operation on the window has ended.

**Availability**:
- macOS 10.6+

## Declaration

```swift
@MainActor
optional func windowDidEndLiveResize(_ notification: Notification)
```

#### Discussion

You can retrieve the window object in question by sending [`object`](https://developer.apple.com/documentation/foundation/nsnotification/1414469-object) to `notification`.

## Parameters

- `notification`: A notification named  .

## See Also

- [func windowWillResize(NSWindow, to: NSSize) -> NSSize](nswindowdelegate/windowwillresize(_:to:).md)
  Tells the delegate that the window is being resized (whether by the user or through one of the `setFrame...` methods other than [`setFrame(_:display:)`](nswindow/setframe(_:display:).md)).
- [func windowDidResize(Notification)](nswindowdelegate/windowdidresize(_:).md)
  Tells the delegate that the window has been resized.
- [func windowWillStartLiveResize(Notification)](nswindowdelegate/windowwillstartliveresize(_:).md)
  Tells the delegate that the window is about to be live resized.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindowdelegate/windowdidendliveresize(_:))*
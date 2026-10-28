# windowDidEndLiveResize(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Tells the delegate that a live resize operation on the window has ended.

**Availability**:
- macOS 10.6+

## Declaration

```swift
@MainActor
optional func windowDidEndLiveResize(_ notification: Notification)
```

```objc
- (void) windowDidEndLiveResize:(NSNotification *) notification;
```

## Discussion

You can retrieve the window object in question by sending [`object`](../../Foundation/nsnotification/object.md) to `notification`.

## Parameters

- `notification`: A notification named [`didEndLiveResizeNotification`](../nswindow/didendliveresizenotification.md).

## See Also

### Sizing Windows
- [func windowWillResize(NSWindow, to: NSSize) -> NSSize](./windowwillresize%28_,to%29.md)
  Tells the delegate that the window is being resized (whether by the user or through one of the `setFrame...` methods other than [`setFrame(_:display:)`](../nswindow/setframe%28_,display%29.md)).
- [func windowDidResize(Notification)](./windowdidresize%28_%29.md)
  Tells the delegate that the window has been resized.
- [func windowWillStartLiveResize(Notification)](./windowwillstartliveresize%28_%29.md)
  Tells the delegate that the window is about to be live resized.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindowdelegate/windowdidendliveresize(_:))*
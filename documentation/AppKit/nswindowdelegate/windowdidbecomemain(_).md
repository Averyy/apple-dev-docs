# windowDidBecomeMain(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Tells the delegate that the window has become main.

**Availability**:
- macOS 10.10+

## Declaration

```swift
@MainActor
optional func windowDidBecomeMain(_ notification: Notification)
```

```objc
- (void) windowDidBecomeMain:(NSNotification *) notification;
```

## Discussion

You can retrieve the window object in question by sending [`object`](../../Foundation/nsnotification/object.md) to `notification`.

## Parameters

- `notification`: A notification named [`didBecomeMainNotification`](../nswindow/didbecomemainnotification.md).

## See Also

### Managing Main Status
- [func windowDidResignMain(Notification)](./windowdidresignmain%28_%29.md)
  Tells the delegate that the window has resigned main window status.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindowdelegate/windowdidbecomemain(_:))*
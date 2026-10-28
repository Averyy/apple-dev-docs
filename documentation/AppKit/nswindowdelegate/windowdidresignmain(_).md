# windowDidResignMain(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Tells the delegate that the window has resigned main window status.

**Availability**:
- macOS 10.10+

## Declaration

```swift
@MainActor
optional func windowDidResignMain(_ notification: Notification)
```

```objc
- (void) windowDidResignMain:(NSNotification *) notification;
```

## Discussion

You can retrieve the window object in question by sending [`object`](../../Foundation/nsnotification/object.md) to `notification`.

## Parameters

- `notification`: A notification named [`didResignMainNotification`](../nswindow/didresignmainnotification.md).

## See Also

### Managing Main Status
- [func windowDidBecomeMain(Notification)](./windowdidbecomemain%28_%29.md)
  Tells the delegate that the window has become main.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindowdelegate/windowdidresignmain(_:))*
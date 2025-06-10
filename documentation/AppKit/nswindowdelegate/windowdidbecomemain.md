# windowDidBecomeMain(_:)

**Framework**: AppKit  
**Kind**: method

Tells the delegate that the window has become main.

**Availability**:
- macOS 10.10+

## Declaration

```swift
@MainActor
optional func windowDidBecomeMain(_ notification: Notification)
```

#### Discussion

You can retrieve the window object in question by sending [`object`](https://developer.apple.com/documentation/Foundation/NSNotification/object) to `notification`.

## Parameters

- `notification`: A notification named  .

## See Also

- [func windowDidResignMain(Notification)](nswindowdelegate/windowdidresignmain(_:).md)
  Tells the delegate that the window has resigned main window status.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindowdelegate/windowdidbecomemain(_:))*
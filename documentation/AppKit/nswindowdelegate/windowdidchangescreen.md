# windowDidChangeScreen(_:)

**Framework**: AppKit  
**Kind**: method

Tells the delegate that the window has changed screens.

**Availability**:
- macOS 10.10+

## Declaration

```swift
@MainActor
optional func windowDidChangeScreen(_ notification: Notification)
```

#### Discussion

You can retrieve the `NSWindow` object in question by sending [`object`](https://developer.apple.com/documentation/foundation/nsnotification/object) to `notification`.

## Parameters

- `notification`: A notification named [`didChangeScreenNotification`](nswindow/didchangescreennotification.md).

## See Also

- [func windowWillMove(Notification)](nswindowdelegate/windowwillmove(_:).md)
  Tells the delegate that the window is about to move.
- [func windowDidMove(Notification)](nswindowdelegate/windowdidmove(_:).md)
  Tells the delegate that the window has moved.
- [func windowDidChangeScreenProfile(Notification)](nswindowdelegate/windowdidchangescreenprofile(_:).md)
  Tells the delegate that the window has changed screen display profiles.
- [func windowDidChangeBackingProperties(Notification)](nswindowdelegate/windowdidchangebackingproperties(_:).md)
  Tells the delegate that the window backing properties changed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindowdelegate/windowdidchangescreen(_:))*
# windowDidMove(_:)

**Framework**: AppKit  
**Kind**: method

Tells the delegate that the window has moved.

**Availability**:
- macOS 10.10+

## Declaration

```swift
@MainActor
optional func windowDidMove(_ notification: Notification)
```

#### Discussion

You can retrieve the `NSWindow` object in question by sending [`object`](https://developer.apple.com/documentation/foundation/nsnotification/1414469-object) to `notification`.

## Parameters

- `notification`: A notification named  .

## See Also

- [func windowWillMove(Notification)](nswindowdelegate/windowwillmove(_:).md)
  Tells the delegate that the window is about to move.
- [func windowDidChangeScreen(Notification)](nswindowdelegate/windowdidchangescreen(_:).md)
  Tells the delegate that the window has changed screens.
- [func windowDidChangeScreenProfile(Notification)](nswindowdelegate/windowdidchangescreenprofile(_:).md)
  Tells the delegate that the window has changed screen display profiles.
- [func windowDidChangeBackingProperties(Notification)](nswindowdelegate/windowdidchangebackingproperties(_:).md)
  Tells the delegate that the window backing properties changed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindowdelegate/windowdidmove(_:))*
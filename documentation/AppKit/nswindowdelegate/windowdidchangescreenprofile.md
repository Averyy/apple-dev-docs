# windowDidChangeScreenProfile(_:)

**Framework**: AppKit  
**Kind**: method

Tells the delegate that the window has changed screen display profiles.

**Availability**:
- macOS 10.10+

## Declaration

```swift
@MainActor
optional func windowDidChangeScreenProfile(_ notification: Notification)
```

#### Discussion

You can retrieve the `NSWindow` object in question by sending [`object`](https://developer.apple.com/documentation/foundation/nsnotification/1414469-object) to `notification`.

If your app runs in macOS 10.7.3 or later, you should instead watch for the notification `NSWindowDidChangeBackingPropertiesNotification`.

## Parameters

- `notification`: A notification named  .

## See Also

- [func windowWillMove(Notification)](nswindowdelegate/windowwillmove(_:).md)
  Tells the delegate that the window is about to move.
- [func windowDidMove(Notification)](nswindowdelegate/windowdidmove(_:).md)
  Tells the delegate that the window has moved.
- [func windowDidChangeScreen(Notification)](nswindowdelegate/windowdidchangescreen(_:).md)
  Tells the delegate that the window has changed screens.
- [func windowDidChangeBackingProperties(Notification)](nswindowdelegate/windowdidchangebackingproperties(_:).md)
  Tells the delegate that the window backing properties changed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindowdelegate/windowdidchangescreenprofile(_:))*
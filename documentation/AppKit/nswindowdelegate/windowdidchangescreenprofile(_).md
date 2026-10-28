# windowDidChangeScreenProfile(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Tells the delegate that the window has changed screen display profiles.

**Availability**:
- macOS 10.10+

## Declaration

```swift
@MainActor
optional func windowDidChangeScreenProfile(_ notification: Notification)
```

```objc
- (void) windowDidChangeScreenProfile:(NSNotification *) notification;
```

## Discussion

You can retrieve the `NSWindow` object in question by sending [`object`](../../Foundation/nsnotification/object.md) to `notification`.

If your app runs in macOS 10.7.3 or later, you should instead watch for the notification `NSWindowDidChangeBackingPropertiesNotification`.

## Parameters

- `notification`: A notification named [`didChangeScreenProfileNotification`](../nswindow/didchangescreenprofilenotification.md).

## See Also

### Moving Windows
- [func windowWillMove(Notification)](./windowwillmove%28_%29.md)
  Tells the delegate that the window is about to move.
- [func windowDidMove(Notification)](./windowdidmove%28_%29.md)
  Tells the delegate that the window has moved.
- [func windowDidChangeScreen(Notification)](./windowdidchangescreen%28_%29.md)
  Tells the delegate that the window has changed screens.
- [func windowDidChangeBackingProperties(Notification)](./windowdidchangebackingproperties%28_%29.md)
  Tells the delegate that the window backing properties changed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindowdelegate/windowdidchangescreenprofile(_:))*
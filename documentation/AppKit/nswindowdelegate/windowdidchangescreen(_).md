# windowDidChangeScreen(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Tells the delegate that the window has changed screens.

**Availability**:
- macOS 10.10+

## Declaration

```swift
@MainActor
optional func windowDidChangeScreen(_ notification: Notification)
```

```objc
- (void) windowDidChangeScreen:(NSNotification *) notification;
```

#### Discussion

You can retrieve the `NSWindow` object in question by sending [`object`](../../Foundation/nsnotification/object.md) to `notification`.

## Parameters

- `notification`: A notification named [`didChangeScreenNotification`](../nswindow/didchangescreennotification.md).

## See Also

### Moving Windows
- [func windowWillMove(Notification)](./windowwillmove%28_%29.md)
  Tells the delegate that the window is about to move.
- [func windowDidMove(Notification)](./windowdidmove%28_%29.md)
  Tells the delegate that the window has moved.
- [func windowDidChangeScreenProfile(Notification)](./windowdidchangescreenprofile%28_%29.md)
  Tells the delegate that the window has changed screen display profiles.
- [func windowDidChangeBackingProperties(Notification)](./windowdidchangebackingproperties%28_%29.md)
  Tells the delegate that the window backing properties changed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindowdelegate/windowdidchangescreen(_:))*
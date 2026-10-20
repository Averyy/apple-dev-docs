# windowWillMove(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Tells the delegate that the window is about to move.

**Availability**:
- macOS 10.10+

## Declaration

```swift
@MainActor
optional func windowWillMove(_ notification: Notification)
```

```objc
- (void) windowWillMove:(NSNotification *) notification;
```

#### Discussion

You can retrieve the `NSWindow` object in question by sending [`object`](../../Foundation/nsnotification/object.md) to `notification`.

## Parameters

- `notification`: A notification named [`willMoveNotification`](../nswindow/willmovenotification.md).

## See Also

### Moving Windows
- [func windowDidMove(Notification)](./windowdidmove%28_%29.md)
  Tells the delegate that the window has moved.
- [func windowDidChangeScreen(Notification)](./windowdidchangescreen%28_%29.md)
  Tells the delegate that the window has changed screens.
- [func windowDidChangeScreenProfile(Notification)](./windowdidchangescreenprofile%28_%29.md)
  Tells the delegate that the window has changed screen display profiles.
- [func windowDidChangeBackingProperties(Notification)](./windowdidchangebackingproperties%28_%29.md)
  Tells the delegate that the window backing properties changed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindowdelegate/windowwillmove(_:))*
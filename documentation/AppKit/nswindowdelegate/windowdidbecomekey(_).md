# windowDidBecomeKey(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Tells the delegate that the window has become the key window.

**Availability**:
- macOS 10.10+

## Declaration

```swift
@MainActor
optional func windowDidBecomeKey(_ notification: Notification)
```

```objc
- (void) windowDidBecomeKey:(NSNotification *) notification;
```

## Discussion

You can retrieve the window object in question by sending [`object`](../../Foundation/nsnotification/object.md) to `notification`.

## Parameters

- `notification`: A notification named [`didBecomeKeyNotification`](../nswindow/didbecomekeynotification.md).

## See Also

### Managing Key Status
- [func windowDidResignKey(Notification)](./windowdidresignkey%28_%29.md)
  Tells the delegate that the window has resigned key window status.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindowdelegate/windowdidbecomekey(_:))*
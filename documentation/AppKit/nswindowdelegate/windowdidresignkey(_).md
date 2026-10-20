# windowDidResignKey(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Tells the delegate that the window has resigned key window status.

**Availability**:
- macOS 10.10+

## Declaration

```swift
@MainActor
optional func windowDidResignKey(_ notification: Notification)
```

```objc
- (void) windowDidResignKey:(NSNotification *) notification;
```

#### Discussion

You can retrieve the window object in question by sending [`object`](../../Foundation/nsnotification/object.md) to `notification`.

## Parameters

- `notification`: A notification named [`didResignKeyNotification`](../nswindow/didresignkeynotification.md).

## See Also

### Managing Key Status
- [func windowDidBecomeKey(Notification)](./windowdidbecomekey%28_%29.md)
  Tells the delegate that the window has become the key window.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindowdelegate/windowdidresignkey(_:))*
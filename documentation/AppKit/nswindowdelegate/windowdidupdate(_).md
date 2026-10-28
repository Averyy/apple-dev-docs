# windowDidUpdate(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Tells the delegate that the window received an [`update()`](../nswindow/update%28%29.md) message.

**Availability**:
- macOS 10.10+

## Declaration

```swift
@MainActor
optional func windowDidUpdate(_ notification: Notification)
```

```objc
- (void) windowDidUpdate:(NSNotification *) notification;
```

## Discussion

You can retrieve the window object in question by sending [`object`](../../Foundation/nsnotification/object.md) to `notification`.

## Parameters

- `notification`: A notification named [`didUpdateNotification`](../nswindow/didupdatenotification.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindowdelegate/windowdidupdate(_:))*
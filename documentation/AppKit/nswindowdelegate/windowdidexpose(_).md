# windowDidExpose(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Tells the delegate that the window has been exposed.

**Availability**:
- macOS 10.10+

## Declaration

```swift
@MainActor
optional func windowDidExpose(_ notification: Notification)
```

```objc
- (void) windowDidExpose:(NSNotification *) notification;
```

#### Discussion

You can retrieve the window object in question by sending [`object`](../../Foundation/nsnotification/object.md) to `notification`.

## Parameters

- `notification`: A notification named [`didExposeNotification`](../nswindow/didexposenotification.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindowdelegate/windowdidexpose(_:))*
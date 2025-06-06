# windowDidUpdate(_:)

**Framework**: AppKit  
**Kind**: method

Tells the delegate that the window received an [`update()`](nswindow/update().md) message.

**Availability**:
- macOS 10.10+

## Declaration

```swift
@MainActor
optional func windowDidUpdate(_ notification: Notification)
```

#### Discussion

You can retrieve the window object in question by sending [`object`](https://developer.apple.com/documentation/foundation/nsnotification/1414469-object) to `notification`.

## Parameters

- `notification`: A notification named 


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindowdelegate/windowdidupdate(_:))*
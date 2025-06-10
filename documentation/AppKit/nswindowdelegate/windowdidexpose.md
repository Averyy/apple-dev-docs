# windowDidExpose(_:)

**Framework**: AppKit  
**Kind**: method

Tells the delegate that the window has been exposed.

**Availability**:
- macOS 10.10+

## Declaration

```swift
@MainActor
optional func windowDidExpose(_ notification: Notification)
```

#### Discussion

You can retrieve the window object in question by sending [`object`](https://developer.apple.com/documentation/Foundation/NSNotification/object) to `notification`.

## Parameters

- `notification`: A notification named  .


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindowdelegate/windowdidexpose(_:))*
# windowDidChangeOcclusionState(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Tells the delegate that the window changed its occlusion state.

**Availability**:
- macOS 10.9+

## Declaration

```swift
@MainActor
optional func windowDidChangeOcclusionState(_ notification: Notification)
```

```objc
- (void) windowDidChangeOcclusionState:(NSNotification *) notification;
```

## Parameters

- `notification`: An [`didChangeOcclusionStateNotification`](../nswindow/didchangeocclusionstatenotification.md) notification.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindowdelegate/windowdidchangeocclusionstate(_:))*
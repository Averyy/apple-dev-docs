# windowDidBecomeKey(_:)

**Framework**: AppKit  
**Kind**: method

Tells the delegate that the window has become the key window.

**Availability**:
- macOS 10.10+

## Declaration

```swift
@MainActor
optional func windowDidBecomeKey(_ notification: Notification)
```

#### Discussion

You can retrieve the window object in question by sending [`object`](https://developer.apple.com/documentation/foundation/nsnotification/1414469-object) to `notification`.

## Parameters

- `notification`: A notification named  .

## See Also

- [func windowDidResignKey(Notification)](nswindowdelegate/windowdidresignkey(_:).md)
  Tells the delegate that the window has resigned key window status.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindowdelegate/windowdidbecomekey(_:))*
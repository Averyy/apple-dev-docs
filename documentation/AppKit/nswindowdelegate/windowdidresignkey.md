# windowDidResignKey(_:)

**Framework**: AppKit  
**Kind**: method

Tells the delegate that the window has resigned key window status.

**Availability**:
- macOS 10.10+

## Declaration

```swift
@MainActor
optional func windowDidResignKey(_ notification: Notification)
```

#### Discussion

You can retrieve the window object in question by sending [`object`](https://developer.apple.com/documentation/foundation/nsnotification/1414469-object) to `notification`.

## Parameters

- `notification`: A notification named  .

## See Also

- [func windowDidBecomeKey(Notification)](nswindowdelegate/windowdidbecomekey(_:).md)
  Tells the delegate that the window has become the key window.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindowdelegate/windowdidresignkey(_:))*
# windowDidDeminiaturize(_:)

**Framework**: AppKit  
**Kind**: method

Tells the delegate that the window has been deminimized.

**Availability**:
- macOS 10.10+

## Declaration

```swift
@MainActor
optional func windowDidDeminiaturize(_ notification: Notification)
```

#### Discussion

You can retrieve the `NSWindow` object in question by sending [`object`](https://developer.apple.com/documentation/foundation/nsnotification/1414469-object) to `notification`.

## Parameters

- `notification`: A notification named 

## See Also

- [func windowWillMiniaturize(Notification)](nswindowdelegate/windowwillminiaturize(_:).md)
  Tells the delegate that the window is about to be minimized.
- [func windowDidMiniaturize(Notification)](nswindowdelegate/windowdidminiaturize(_:).md)
  Tells the delegate that the window has been minimized.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindowdelegate/windowdiddeminiaturize(_:))*
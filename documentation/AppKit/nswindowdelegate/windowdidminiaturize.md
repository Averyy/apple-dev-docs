# windowDidMiniaturize(_:)

**Framework**: AppKit  
**Kind**: method

Tells the delegate that the window has been minimized.

**Availability**:
- macOS 10.10+

## Declaration

```swift
@MainActor
optional func windowDidMiniaturize(_ notification: Notification)
```

#### Discussion

You can retrieve the `NSWindow` object in question by sending [`object`](https://developer.apple.com/documentation/Foundation/NSNotification/object) to `notification`.

## Parameters

- `notification`: A notification named  .

## See Also

- [func windowWillMiniaturize(Notification)](nswindowdelegate/windowwillminiaturize(_:).md)
  Tells the delegate that the window is about to be minimized.
- [func windowDidDeminiaturize(Notification)](nswindowdelegate/windowdiddeminiaturize(_:).md)
  Tells the delegate that the window has been deminimized.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindowdelegate/windowdidminiaturize(_:))*
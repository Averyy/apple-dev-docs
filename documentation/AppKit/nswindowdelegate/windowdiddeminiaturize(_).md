# windowDidDeminiaturize(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Tells the delegate that the window has been deminimized.

**Availability**:
- macOS 10.10+

## Declaration

```swift
@MainActor
optional func windowDidDeminiaturize(_ notification: Notification)
```

```objc
- (void) windowDidDeminiaturize:(NSNotification *) notification;
```

## Discussion

You can retrieve the `NSWindow` object in question by sending [`object`](../../Foundation/nsnotification/object.md) to `notification`.

## Parameters

- `notification`: A notification named [`didDeminiaturizeNotification`](../nswindow/diddeminiaturizenotification.md)

## See Also

### Minimizing Windows
- [func windowWillMiniaturize(Notification)](./windowwillminiaturize%28_%29.md)
  Tells the delegate that the window is about to be minimized.
- [func windowDidMiniaturize(Notification)](./windowdidminiaturize%28_%29.md)
  Tells the delegate that the window has been minimized.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindowdelegate/windowdiddeminiaturize(_:))*
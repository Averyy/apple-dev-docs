# windowDidMiniaturize(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Tells the delegate that the window has been minimized.

**Availability**:
- macOS 10.10+

## Declaration

```swift
@MainActor
optional func windowDidMiniaturize(_ notification: Notification)
```

```objc
- (void) windowDidMiniaturize:(NSNotification *) notification;
```

## Discussion

You can retrieve the `NSWindow` object in question by sending [`object`](../../Foundation/nsnotification/object.md) to `notification`.

## Parameters

- `notification`: A notification named [`didMiniaturizeNotification`](../nswindow/didminiaturizenotification.md).

## See Also

### Minimizing Windows
- [func windowWillMiniaturize(Notification)](./windowwillminiaturize%28_%29.md)
  Tells the delegate that the window is about to be minimized.
- [func windowDidDeminiaturize(Notification)](./windowdiddeminiaturize%28_%29.md)
  Tells the delegate that the window has been deminimized.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindowdelegate/windowdidminiaturize(_:))*
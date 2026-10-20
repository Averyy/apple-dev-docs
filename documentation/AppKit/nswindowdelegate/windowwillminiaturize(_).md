# windowWillMiniaturize(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Tells the delegate that the window is about to be minimized.

**Availability**:
- macOS 10.10+

## Declaration

```swift
@MainActor
optional func windowWillMiniaturize(_ notification: Notification)
```

```objc
- (void) windowWillMiniaturize:(NSNotification *) notification;
```

#### Discussion

You can retrieve the `NSWindow` object in question by sending [`object`](../../Foundation/nsnotification/object.md) to `notification`.

## Parameters

- `notification`: A notification named [`willMiniaturizeNotification`](../nswindow/willminiaturizenotification.md).

## See Also

### Minimizing Windows
- [func windowDidMiniaturize(Notification)](./windowdidminiaturize%28_%29.md)
  Tells the delegate that the window has been minimized.
- [func windowDidDeminiaturize(Notification)](./windowdiddeminiaturize%28_%29.md)
  Tells the delegate that the window has been deminimized.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindowdelegate/windowwillminiaturize(_:))*
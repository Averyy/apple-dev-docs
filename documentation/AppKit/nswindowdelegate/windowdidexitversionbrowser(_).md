# windowDidExitVersionBrowser(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Tells the delegate that the window has left version browsing.

**Availability**:
- macOS 10.7+

## Declaration

```swift
@MainActor
optional func windowDidExitVersionBrowser(_ notification: Notification)
```

```objc
- (void) windowDidExitVersionBrowser:(NSNotification *) notification;
```

## Parameters

- `notification`: An [`didExitVersionBrowserNotification`](../nswindow/didexitversionbrowsernotification.md) notification.

## See Also

### Managing Presentation in Version Browsers
- [func window(NSWindow, willResizeForVersionBrowserWithMaxPreferredSize: NSSize, maxAllowedSize: NSSize) -> NSSize](./window%28_,willresizeforversionbrowserwithmaxpreferredsize,maxallowedsize%29.md)
  Tells the delegate the window will resize for presentation during version browsing.
- [func windowWillEnterVersionBrowser(Notification)](./windowwillenterversionbrowser%28_%29.md)
  Tells the delegate the window is about to enter version browsing.
- [func windowDidEnterVersionBrowser(Notification)](./windowdidenterversionbrowser%28_%29.md)
  Tells the delegate that the window has entered version browsing.
- [func windowWillExitVersionBrowser(Notification)](./windowwillexitversionbrowser%28_%29.md)
  Tells the delegate that the window is about to leave version browsing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindowdelegate/windowdidexitversionbrowser(_:))*
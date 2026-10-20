# windowDidEnterVersionBrowser(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Tells the delegate that the window has entered version browsing.

**Availability**:
- macOS 10.7+

## Declaration

```swift
@MainActor
optional func windowDidEnterVersionBrowser(_ notification: Notification)
```

```objc
- (void) windowDidEnterVersionBrowser:(NSNotification *) notification;
```

## Parameters

- `notification`: An [`didEnterVersionBrowserNotification`](../nswindow/didenterversionbrowsernotification.md) notification.

## See Also

### Managing Presentation in Version Browsers
- [func window(NSWindow, willResizeForVersionBrowserWithMaxPreferredSize: NSSize, maxAllowedSize: NSSize) -> NSSize](./window%28_,willresizeforversionbrowserwithmaxpreferredsize,maxallowedsize%29.md)
  Tells the delegate the window will resize for presentation during version browsing.
- [func windowWillEnterVersionBrowser(Notification)](./windowwillenterversionbrowser%28_%29.md)
  Tells the delegate the window is about to enter version browsing.
- [func windowWillExitVersionBrowser(Notification)](./windowwillexitversionbrowser%28_%29.md)
  Tells the delegate that the window is about to leave version browsing.
- [func windowDidExitVersionBrowser(Notification)](./windowdidexitversionbrowser%28_%29.md)
  Tells the delegate that the window has left version browsing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindowdelegate/windowdidenterversionbrowser(_:))*
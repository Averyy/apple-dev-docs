# windowWillExitVersionBrowser(_:)

**Framework**: AppKit  
**Kind**: method

Tells the delegate that the window is about to leave version browsing.

**Availability**:
- macOS 10.7+

## Declaration

```swift
@MainActor
optional func windowWillExitVersionBrowser(_ notification: Notification)
```

## Parameters

- `notification`: An   notification.

## See Also

- [func window(NSWindow, willResizeForVersionBrowserWithMaxPreferredSize: NSSize, maxAllowedSize: NSSize) -> NSSize](nswindowdelegate/window(_:willresizeforversionbrowserwithmaxpreferredsize:maxallowedsize:).md)
  Tells the delegate the window will resize for presentation during version browsing.
- [func windowWillEnterVersionBrowser(Notification)](nswindowdelegate/windowwillenterversionbrowser(_:).md)
  Tells the delegate the window is about to enter version browsing.
- [func windowDidEnterVersionBrowser(Notification)](nswindowdelegate/windowdidenterversionbrowser(_:).md)
  Tells the delegate that the window has entered version browsing.
- [func windowDidExitVersionBrowser(Notification)](nswindowdelegate/windowdidexitversionbrowser(_:).md)
  Tells the delegate that the window has left version browsing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindowdelegate/windowwillexitversionbrowser(_:))*
# windowWillExitFullScreen(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

The window is about to exit full-screen mode.

**Availability**:
- macOS 10.7+

## Declaration

```swift
@MainActor
optional func windowWillExitFullScreen(_ notification: Notification)
```

```objc
- (void) windowWillExitFullScreen:(NSNotification *) notification;
```

## Parameters

- `notification`: A notification named [`willExitFullScreenNotification`](../nswindow/willexitfullscreennotification.md).

## See Also

### Managing Full-Screen Presentation
- [func window(NSWindow, willUseFullScreenContentSize: NSSize) -> NSSize](./window%28_,willusefullscreencontentsize%29.md)
  Called to allow the delegate to modify the full-screen content size.
- [func window(NSWindow, willUseFullScreenPresentationOptions: NSApplication.PresentationOptions) -> NSApplication.PresentationOptions](./window%28_,willusefullscreenpresentationoptions%29.md)
  Returns the presentation options the window uses when transitioning to full-screen mode.
- [func windowWillEnterFullScreen(Notification)](./windowwillenterfullscreen%28_%29.md)
  The window is about to enter full-screen mode.
- [func windowDidEnterFullScreen(Notification)](./windowdidenterfullscreen%28_%29.md)
  The window has entered full-screen mode.
- [func windowDidExitFullScreen(Notification)](./windowdidexitfullscreen%28_%29.md)
  The window has left full-screen mode.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindowdelegate/windowwillexitfullscreen(_:))*
# windowWillExitFullScreen(_:)

**Framework**: AppKit  
**Kind**: method

The window is about to exit full-screen mode.

**Availability**:
- macOS 10.7+

## Declaration

```swift
@MainActor
optional func windowWillExitFullScreen(_ notification: Notification)
```

## Parameters

- `notification`: A notification named  .

## See Also

- [func window(NSWindow, willUseFullScreenContentSize: NSSize) -> NSSize](nswindowdelegate/window(_:willusefullscreencontentsize:).md)
  Called to allow the delegate to modify the full-screen content size.
- [func window(NSWindow, willUseFullScreenPresentationOptions: NSApplication.PresentationOptions) -> NSApplication.PresentationOptions](nswindowdelegate/window(_:willusefullscreenpresentationoptions:).md)
  Returns the presentation options the window uses when transitioning to full-screen mode.
- [func windowWillEnterFullScreen(Notification)](nswindowdelegate/windowwillenterfullscreen(_:).md)
  The window is about to enter full-screen mode.
- [func windowDidEnterFullScreen(Notification)](nswindowdelegate/windowdidenterfullscreen(_:).md)
  The window has entered full-screen mode.
- [func windowDidExitFullScreen(Notification)](nswindowdelegate/windowdidexitfullscreen(_:).md)
  The window has left full-screen mode.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindowdelegate/windowwillexitfullscreen(_:))*
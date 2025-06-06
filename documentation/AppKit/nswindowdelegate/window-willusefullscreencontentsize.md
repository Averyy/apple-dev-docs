# window(_:willUseFullScreenContentSize:)

**Framework**: AppKit  
**Kind**: method

Called to allow the delegate to modify the full-screen content size.

**Availability**:
- macOS 10.7+

## Declaration

```swift
@MainActor
optional func window(_ window: NSWindow, willUseFullScreenContentSize proposedSize: NSSize) -> NSSize
```

#### Return Value

The window size to use when displaying content size.

## Parameters

- `window`: The window to enter to full-screen mode.
- `proposedSize`: The proposed window size.

## See Also

- [func window(NSWindow, willUseFullScreenPresentationOptions: NSApplication.PresentationOptions) -> NSApplication.PresentationOptions](nswindowdelegate/window(_:willusefullscreenpresentationoptions:).md)
  Returns the presentation options the window uses when transitioning to full-screen mode.
- [func windowWillEnterFullScreen(Notification)](nswindowdelegate/windowwillenterfullscreen(_:).md)
  The window is about to enter full-screen mode.
- [func windowDidEnterFullScreen(Notification)](nswindowdelegate/windowdidenterfullscreen(_:).md)
  The window has entered full-screen mode.
- [func windowWillExitFullScreen(Notification)](nswindowdelegate/windowwillexitfullscreen(_:).md)
  The window is about to exit full-screen mode.
- [func windowDidExitFullScreen(Notification)](nswindowdelegate/windowdidexitfullscreen(_:).md)
  The window has left full-screen mode.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindowdelegate/window(_:willusefullscreencontentsize:))*
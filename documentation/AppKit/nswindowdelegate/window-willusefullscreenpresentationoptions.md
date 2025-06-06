# window(_:willUseFullScreenPresentationOptions:)

**Framework**: AppKit  
**Kind**: method

Returns the presentation options the window uses when transitioning to full-screen mode.

**Availability**:
- macOS 10.7+

## Declaration

```swift
@MainActor
optional func window(_ window: NSWindow, willUseFullScreenPresentationOptions proposedOptions: NSApplication.PresentationOptions = []) -> NSApplication.PresentationOptions
```

#### Return Value

The options the window should use when transitioning to full-screen mode. These may be the same as the `proposedOptions` or may be modified.

## Parameters

- `window`: The window to enter to full-screen mode.
- `proposedOptions`: The proposed options. See   for the possible values.

## See Also

- [func window(NSWindow, willUseFullScreenContentSize: NSSize) -> NSSize](nswindowdelegate/window(_:willusefullscreencontentsize:).md)
  Called to allow the delegate to modify the full-screen content size.
- [func windowWillEnterFullScreen(Notification)](nswindowdelegate/windowwillenterfullscreen(_:).md)
  The window is about to enter full-screen mode.
- [func windowDidEnterFullScreen(Notification)](nswindowdelegate/windowdidenterfullscreen(_:).md)
  The window has entered full-screen mode.
- [func windowWillExitFullScreen(Notification)](nswindowdelegate/windowwillexitfullscreen(_:).md)
  The window is about to exit full-screen mode.
- [func windowDidExitFullScreen(Notification)](nswindowdelegate/windowdidexitfullscreen(_:).md)
  The window has left full-screen mode.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindowdelegate/window(_:willusefullscreenpresentationoptions:))*
# window(_:willUseFullScreenContentSize:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Called to allow the delegate to modify the full-screen content size.

**Availability**:
- macOS 10.7+

## Declaration

```swift
@MainActor
optional func window(_ window: NSWindow, willUseFullScreenContentSize proposedSize: NSSize) -> NSSize
```

```objc
- (NSSize) window:(NSWindow *) window willUseFullScreenContentSize:(NSSize) proposedSize;
```

## Return Value

The window size to use when displaying content size.

## Parameters

- `window`: The window to enter to full-screen mode.
- `proposedSize`: The proposed window size.

## See Also

### Managing Full-Screen Presentation
- [func window(NSWindow, willUseFullScreenPresentationOptions: NSApplication.PresentationOptions) -> NSApplication.PresentationOptions](./window%28_,willusefullscreenpresentationoptions%29.md)
  Returns the presentation options the window uses when transitioning to full-screen mode.
- [func windowWillEnterFullScreen(Notification)](./windowwillenterfullscreen%28_%29.md)
  The window is about to enter full-screen mode.
- [func windowDidEnterFullScreen(Notification)](./windowdidenterfullscreen%28_%29.md)
  The window has entered full-screen mode.
- [func windowWillExitFullScreen(Notification)](./windowwillexitfullscreen%28_%29.md)
  The window is about to exit full-screen mode.
- [func windowDidExitFullScreen(Notification)](./windowdidexitfullscreen%28_%29.md)
  The window has left full-screen mode.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindowdelegate/window(_:willusefullscreencontentsize:))*
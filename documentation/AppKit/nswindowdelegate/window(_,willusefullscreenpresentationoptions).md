# window(_:willUseFullScreenPresentationOptions:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns the presentation options the window uses when transitioning to full-screen mode.

**Availability**:
- macOS 10.7+

## Declaration

```swift
@MainActor
optional func window(_ window: NSWindow, willUseFullScreenPresentationOptions proposedOptions: NSApplication.PresentationOptions = []) -> NSApplication.PresentationOptions
```

```objc
- (NSApplicationPresentationOptions) window:(NSWindow *) window willUseFullScreenPresentationOptions:(NSApplicationPresentationOptions) proposedOptions;
```

## Return Value

The options the window should use when transitioning to full-screen mode. These may be the same as the `proposedOptions` or may be modified.

## Parameters

- `window`: The window to enter to full-screen mode.
- `proposedOptions`: The proposed options. See [`NSApplication.PresentationOptions`](../nsapplication/presentationoptions-swift.struct.md) for the possible values.

## See Also

### Managing Full-Screen Presentation
- [func window(NSWindow, willUseFullScreenContentSize: NSSize) -> NSSize](./window%28_,willusefullscreencontentsize%29.md)
  Called to allow the delegate to modify the full-screen content size.
- [func windowWillEnterFullScreen(Notification)](./windowwillenterfullscreen%28_%29.md)
  The window is about to enter full-screen mode.
- [func windowDidEnterFullScreen(Notification)](./windowdidenterfullscreen%28_%29.md)
  The window has entered full-screen mode.
- [func windowWillExitFullScreen(Notification)](./windowwillexitfullscreen%28_%29.md)
  The window is about to exit full-screen mode.
- [func windowDidExitFullScreen(Notification)](./windowdidexitfullscreen%28_%29.md)
  The window has left full-screen mode.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindowdelegate/window(_:willusefullscreenpresentationoptions:))*
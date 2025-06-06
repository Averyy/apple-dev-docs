# windowDidFailToEnterFullScreen(_:)

**Framework**: AppKit  
**Kind**: method

Called if the window failed to enter full-screen mode.

**Availability**:
- macOS 10.7+

## Declaration

```swift
@MainActor
optional func windowDidFailToEnterFullScreen(_ window: NSWindow)
```

#### Discussion

In some cases, the transition to enter full-screen mode can fail, due to being in the midst of handling some other animation or user gesture. This method indicates that there was an error, and you should clean up any work you may have done to prepare to enter full-screen mode.

This message is sent whether or not the delegate indicated a custom animation by returning non-`nil` from  [`customWindowsToEnterFullScreen(for:)`](nswindowdelegate/customwindowstoenterfullscreen(for:).md).

## Parameters

- `window`: The window that failed to enter to full-screen mode.

## See Also

- [func customWindowsToEnterFullScreen(for: NSWindow) -> [NSWindow]?](nswindowdelegate/customwindowstoenterfullscreen(for:).md)
  Called when the window is about to enter full-screen mode.
- [func customWindowsToEnterFullScreen(for: NSWindow, on: NSScreen) -> [NSWindow]?](nswindowdelegate/customwindowstoenterfullscreen(for:on:).md)
  Called when the window is about to enter full-screen mode.
- [func window(NSWindow, startCustomAnimationToEnterFullScreenWithDuration: TimeInterval)](nswindowdelegate/window(_:startcustomanimationtoenterfullscreenwithduration:).md)
  This method is called to start the window animation into full-screen mode, including transitioning to a new space.
- [func window(NSWindow, startCustomAnimationToEnterFullScreenOn: NSScreen, withDuration: TimeInterval)](nswindowdelegate/window(_:startcustomanimationtoenterfullscreenon:withduration:).md)
  This method is called to start the window animation into full-screen mode, including transitioning to a new space.
- [func customWindowsToExitFullScreen(for: NSWindow) -> [NSWindow]?](nswindowdelegate/customwindowstoexitfullscreen(for:).md)
  Called when the window is about to exit full-screen mode.
- [func window(NSWindow, startCustomAnimationToExitFullScreenWithDuration: TimeInterval)](nswindowdelegate/window(_:startcustomanimationtoexitfullscreenwithduration:).md)
  This method is called to start the window animation out of full-screen mode, including transitioning back to the desktop space.
- [func windowDidFailToExitFullScreen(NSWindow)](nswindowdelegate/windowdidfailtoexitfullscreen(_:).md)
  Called if the window failed to exit full-screen mode.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindowdelegate/windowdidfailtoenterfullscreen(_:))*
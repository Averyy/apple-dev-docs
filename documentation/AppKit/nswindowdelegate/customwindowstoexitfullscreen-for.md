# customWindowsToExitFullScreen(for:)

**Framework**: AppKit  
**Kind**: method

Called when the window is about to exit full-screen mode.

**Availability**:
- macOS 10.7+

## Declaration

```swift
@MainActor
optional func customWindowsToExitFullScreen(for window: NSWindow) -> [NSWindow]?
```

#### Return Value

An array of windows involved in the animation out of full-screen mode for `window`; otherwise `nil`.

#### Discussion

This method lets the window delegate customize the animation when the window is about to exit full-screen mode by providing a custom window or windows containing layers or other effects. If an you do not want to perform custom animation, you can omit the implementation of this method, or it can return `nil`.

## Parameters

- `window`: The window to exit full-screen mode.

## See Also

- [func customWindowsToEnterFullScreen(for: NSWindow) -> [NSWindow]?](nswindowdelegate/customwindowstoenterfullscreen(for:).md)
  Called when the window is about to enter full-screen mode.
- [func customWindowsToEnterFullScreen(for: NSWindow, on: NSScreen) -> [NSWindow]?](nswindowdelegate/customwindowstoenterfullscreen(for:on:).md)
  Called when the window is about to enter full-screen mode.
- [func window(NSWindow, startCustomAnimationToEnterFullScreenWithDuration: TimeInterval)](nswindowdelegate/window(_:startcustomanimationtoenterfullscreenwithduration:).md)
  This method is called to start the window animation into full-screen mode, including transitioning to a new space.
- [func window(NSWindow, startCustomAnimationToEnterFullScreenOn: NSScreen, withDuration: TimeInterval)](nswindowdelegate/window(_:startcustomanimationtoenterfullscreenon:withduration:).md)
  This method is called to start the window animation into full-screen mode, including transitioning to a new space.
- [func windowDidFailToEnterFullScreen(NSWindow)](nswindowdelegate/windowdidfailtoenterfullscreen(_:).md)
  Called if the window failed to enter full-screen mode.
- [func window(NSWindow, startCustomAnimationToExitFullScreenWithDuration: TimeInterval)](nswindowdelegate/window(_:startcustomanimationtoexitfullscreenwithduration:).md)
  This method is called to start the window animation out of full-screen mode, including transitioning back to the desktop space.
- [func windowDidFailToExitFullScreen(NSWindow)](nswindowdelegate/windowdidfailtoexitfullscreen(_:).md)
  Called if the window failed to exit full-screen mode.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindowdelegate/customwindowstoexitfullscreen(for:))*
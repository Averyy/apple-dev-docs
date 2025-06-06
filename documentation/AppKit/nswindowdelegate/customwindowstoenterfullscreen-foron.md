# customWindowsToEnterFullScreen(for:on:)

**Framework**: AppKit  
**Kind**: method

Called when the window is about to enter full-screen mode.

**Availability**:
- macOS 10.9+

## Declaration

```swift
@MainActor
optional func customWindowsToEnterFullScreen(for window: NSWindow, on screen: NSScreen) -> [NSWindow]?
```

#### Return Value

An array of windows to use for the animation to full-screen mode for `window`; otherwise `nil`.

#### Discussion

This method lets a window delegate customize the animation when the window is about to enter full-screen mode by providing a custom window or windows containing layers or other effects. If you don’t want to perform custom animation, you can omit the implementation of this method, or it can return `nil`.

##### Special Considerations

If this method and [`customWindowsToEnterFullScreen(for:)`](nswindowdelegate/customwindowstoenterfullscreen(for:).md) are both implemented, this method is called.

## Parameters

- `window`: The window to enter full-screen mode.
- `screen`: The display screen on which the window will enter full-screen mode.

## See Also

- [func customWindowsToEnterFullScreen(for: NSWindow) -> [NSWindow]?](nswindowdelegate/customwindowstoenterfullscreen(for:).md)
  Called when the window is about to enter full-screen mode.
- [func window(NSWindow, startCustomAnimationToEnterFullScreenWithDuration: TimeInterval)](nswindowdelegate/window(_:startcustomanimationtoenterfullscreenwithduration:).md)
  This method is called to start the window animation into full-screen mode, including transitioning to a new space.
- [func window(NSWindow, startCustomAnimationToEnterFullScreenOn: NSScreen, withDuration: TimeInterval)](nswindowdelegate/window(_:startcustomanimationtoenterfullscreenon:withduration:).md)
  This method is called to start the window animation into full-screen mode, including transitioning to a new space.
- [func windowDidFailToEnterFullScreen(NSWindow)](nswindowdelegate/windowdidfailtoenterfullscreen(_:).md)
  Called if the window failed to enter full-screen mode.
- [func customWindowsToExitFullScreen(for: NSWindow) -> [NSWindow]?](nswindowdelegate/customwindowstoexitfullscreen(for:).md)
  Called when the window is about to exit full-screen mode.
- [func window(NSWindow, startCustomAnimationToExitFullScreenWithDuration: TimeInterval)](nswindowdelegate/window(_:startcustomanimationtoexitfullscreenwithduration:).md)
  This method is called to start the window animation out of full-screen mode, including transitioning back to the desktop space.
- [func windowDidFailToExitFullScreen(NSWindow)](nswindowdelegate/windowdidfailtoexitfullscreen(_:).md)
  Called if the window failed to exit full-screen mode.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindowdelegate/customwindowstoenterfullscreen(for:on:))*
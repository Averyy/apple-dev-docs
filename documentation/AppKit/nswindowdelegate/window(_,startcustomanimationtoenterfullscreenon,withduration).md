# window(_:startCustomAnimationToEnterFullScreenOn:withDuration:)

**Framework**: AppKit  
**Kind**: method

This method is called to start the window animation into full-screen mode, including transitioning to a new space.

**Availability**:
- macOS 10.9+

## Declaration

```swift
@MainActor
optional func window(_ window: NSWindow, startCustomAnimationToEnterFullScreenOn screen: NSScreen, withDuration duration: TimeInterval)
```

#### Discussion

You can implement this method to perform custom animation with the given duration to be in sync with the system animation.

##### Special Considerations

This method is called only if [`customWindowsToEnterFullScreen(for:)`](nswindowdelegate/customwindowstoenterfullscreen(for:).md) returns non-`nil`. If [`window(_:startCustomAnimationToEnterFullScreenWithDuration:)`](nswindowdelegate/window(_:startcustomanimationtoenterfullscreenwithduration:).md) and this method are both implemented, this method is called.

## Parameters

- `window`: The window to enter full-screen mode.
- `screen`: The display screen on which the window will enter full-screen mode.
- `duration`: The duration of the presentation change.

## See Also

- [func customWindowsToEnterFullScreen(for: NSWindow) -> [NSWindow]?](nswindowdelegate/customwindowstoenterfullscreen(for:).md)
  Called when the window is about to enter full-screen mode.
- [func customWindowsToEnterFullScreen(for: NSWindow, on: NSScreen) -> [NSWindow]?](nswindowdelegate/customwindowstoenterfullscreen(for:on:).md)
  Called when the window is about to enter full-screen mode.
- [func window(NSWindow, startCustomAnimationToEnterFullScreenWithDuration: TimeInterval)](nswindowdelegate/window(_:startcustomanimationtoenterfullscreenwithduration:).md)
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

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindowdelegate/window(_:startcustomanimationtoenterfullscreenon:withduration:))*
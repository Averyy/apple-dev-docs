# windowDidFailToEnterFullScreen(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Called if the window failed to enter full-screen mode.

**Availability**:
- macOS 10.7+

## Declaration

```swift
@MainActor
optional func windowDidFailToEnterFullScreen(_ window: NSWindow)
```

```objc
- (void) windowDidFailToEnterFullScreen:(NSWindow *) window;
```

#### Discussion

In some cases, the transition to enter full-screen mode can fail, due to being in the midst of handling some other animation or user gesture. This method indicates that there was an error, and you should clean up any work you may have done to prepare to enter full-screen mode.

This message is sent whether or not the delegate indicated a custom animation by returning non-`nil` from  [`customWindowsToEnterFullScreen(for:)`](./customwindowstoenterfullscreen%28for%29.md).

## Parameters

- `window`: The window that failed to enter to full-screen mode.

## See Also

### Custom Full-Screen Presentation Animations
- [func customWindowsToEnterFullScreen(for: NSWindow) -> [NSWindow]?](./customwindowstoenterfullscreen%28for%29.md)
  Called when the window is about to enter full-screen mode.
- [func customWindowsToEnterFullScreen(for: NSWindow, on: NSScreen) -> [NSWindow]?](./customwindowstoenterfullscreen%28for,on%29.md)
  Called when the window is about to enter full-screen mode.
- [func window(NSWindow, startCustomAnimationToEnterFullScreenWithDuration: TimeInterval)](./window%28_,startcustomanimationtoenterfullscreenwithduration%29.md)
  This method is called to start the window animation into full-screen mode, including transitioning to a new space.
- [func window(NSWindow, startCustomAnimationToEnterFullScreenOn: NSScreen, withDuration: TimeInterval)](./window%28_,startcustomanimationtoenterfullscreenon,withduration%29.md)
  This method is called to start the window animation into full-screen mode, including transitioning to a new space.
- [func customWindowsToExitFullScreen(for: NSWindow) -> [NSWindow]?](./customwindowstoexitfullscreen%28for%29.md)
  Called when the window is about to exit full-screen mode.
- [func window(NSWindow, startCustomAnimationToExitFullScreenWithDuration: TimeInterval)](./window%28_,startcustomanimationtoexitfullscreenwithduration%29.md)
  This method is called to start the window animation out of full-screen mode, including transitioning back to the desktop space.
- [func windowDidFailToExitFullScreen(NSWindow)](./windowdidfailtoexitfullscreen%28_%29.md)
  Called if the window failed to exit full-screen mode.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindowdelegate/windowdidfailtoenterfullscreen(_:))*
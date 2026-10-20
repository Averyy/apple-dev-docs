# window(_:startCustomAnimationToEnterFullScreenWithDuration:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

This method is called to start the window animation into full-screen mode, including transitioning to a new space.

**Availability**:
- macOS 10.7+

## Declaration

```swift
@MainActor
optional func window(_ window: NSWindow, startCustomAnimationToEnterFullScreenWithDuration duration: TimeInterval)
```

```objc
- (void) window:(NSWindow *) window startCustomAnimationToEnterFullScreenWithDuration:(NSTimeInterval) duration;
```

#### Discussion

You can implement this method to perform custom animation with the given duration to be in sync with the system animation.

##### Special Considerations

This method is called only if [`customWindowsToEnterFullScreen(for:)`](./customwindowstoenterfullscreen%28for%29.md) returns non-`nil`.

## Parameters

- `window`: The window to enter full-screen mode.
- `duration`: The duration of the presentation change.

## See Also

### Custom Full-Screen Presentation Animations
- [func customWindowsToEnterFullScreen(for: NSWindow) -> [NSWindow]?](./customwindowstoenterfullscreen%28for%29.md)
  Called when the window is about to enter full-screen mode.
- [func customWindowsToEnterFullScreen(for: NSWindow, on: NSScreen) -> [NSWindow]?](./customwindowstoenterfullscreen%28for,on%29.md)
  Called when the window is about to enter full-screen mode.
- [func window(NSWindow, startCustomAnimationToEnterFullScreenOn: NSScreen, withDuration: TimeInterval)](./window%28_,startcustomanimationtoenterfullscreenon,withduration%29.md)
  This method is called to start the window animation into full-screen mode, including transitioning to a new space.
- [func windowDidFailToEnterFullScreen(NSWindow)](./windowdidfailtoenterfullscreen%28_%29.md)
  Called if the window failed to enter full-screen mode.
- [func customWindowsToExitFullScreen(for: NSWindow) -> [NSWindow]?](./customwindowstoexitfullscreen%28for%29.md)
  Called when the window is about to exit full-screen mode.
- [func window(NSWindow, startCustomAnimationToExitFullScreenWithDuration: TimeInterval)](./window%28_,startcustomanimationtoexitfullscreenwithduration%29.md)
  This method is called to start the window animation out of full-screen mode, including transitioning back to the desktop space.
- [func windowDidFailToExitFullScreen(NSWindow)](./windowdidfailtoexitfullscreen%28_%29.md)
  Called if the window failed to exit full-screen mode.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindowdelegate/window(_:startcustomanimationtoenterfullscreenwithduration:))*
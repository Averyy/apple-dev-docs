# customWindowsToEnterFullScreen(for:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Called when the window is about to enter full-screen mode.

**Availability**:
- macOS 10.7+

## Declaration

```swift
@MainActor
optional func customWindowsToEnterFullScreen(for window: NSWindow) -> [NSWindow]?
```

```objc
- (NSArray<NSWindow *> *) customWindowsToEnterFullScreenForWindow:(NSWindow *) window;
```

## Return Value

An array of windows to use for the animation to full-screen mode for `window`; otherwise `nil`.

## Discussion

This method lets a window delegate customize the animation when the window is about to enter full-screen mode by providing a custom window or windows containing layers or other effects. If you don’t want to perform custom animation, you can omit the implementation of this method, or it can return `nil`.

## Parameters

- `window`: The window to enter full-screen mode.

## See Also

### Custom Full-Screen Presentation Animations
- [func customWindowsToEnterFullScreen(for: NSWindow, on: NSScreen) -> [NSWindow]?](./customwindowstoenterfullscreen%28for,on%29.md)
  Called when the window is about to enter full-screen mode.
- [func window(NSWindow, startCustomAnimationToEnterFullScreenWithDuration: TimeInterval)](./window%28_,startcustomanimationtoenterfullscreenwithduration%29.md)
  This method is called to start the window animation into full-screen mode, including transitioning to a new space.
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

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindowdelegate/customwindowstoenterfullscreen(for:))*
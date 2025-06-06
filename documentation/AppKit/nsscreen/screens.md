# screens

**Framework**: AppKit  
**Kind**: property

Returns an array of screen objects representing all of the screens available on the system.

**Availability**:
- macOS ?+

## Declaration

```swift
class var screens: [NSScreen] { get }
```

#### Return Value

An array of the [`NSScreen`](nsscreen.md) objects available on the current system.

#### Discussion

The screen at index `0` in the returned array corresponds to the primary screen of the user’s system. This is the screen that contains the menu bar and whose origin is at the point `(0, 0)`. In the case of mirroring, the first screen is the largest drawable display; if all screens are the same size, it is the screen with the highest pixel depth. This primary screen may not be the same as the one returned by the [`main`](nsscreen/main.md) method, which returns the screen with the active window.

The array should not be cached. Screens can be added, removed, or dynamically reconfigured at any time. When the display configuration is changed, the default notification center sends a [`didChangeScreenParametersNotification`](nsapplication/didchangescreenparametersnotification.md) notification.

## See Also

- [class var main: NSScreen?](nsscreen/main.md)
  Returns the screen object containing the window with the keyboard focus.
- [class var deepest: NSScreen?](nsscreen/deepest.md)
  Returns a screen object representing the screen that can best represent color.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsscreen/screens)*
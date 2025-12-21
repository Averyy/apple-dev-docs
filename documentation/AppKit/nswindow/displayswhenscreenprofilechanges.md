# displaysWhenScreenProfileChanges

**Framework**: AppKit  
**Kind**: property

A Boolean value that indicates whether the window context should be updated when the screen profile changes or when the window moves to a different screen.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var displaysWhenScreenProfileChanges: Bool { get set }
```

#### Discussion

The value of this property is [`true`](https://developer.apple.com/documentation/Swift/true) when the window context should be updated when the ColorSync profile of the current screen changes or when a majority of the window is moved to a different screen whose profile is different than the previous screen; otherwise, [`false`](https://developer.apple.com/documentation/Swift/false). The default value is [`false`](https://developer.apple.com/documentation/Swift/false).

After the window context is updated, the window is told to display itself. If you need to update offscreen caches for the window, you should register to receive the [`didChangeScreenProfileNotification`](nswindow/didchangescreenprofilenotification.md) notification.

## See Also

- [var screen: NSScreen?](nswindow/screen.md)
  The screen the window is on.
- [var deepestScreen: NSScreen?](nswindow/deepestscreen.md)
  The deepest screen the window is on (it may be split over several screens).


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindow/displayswhenscreenprofilechanges)*
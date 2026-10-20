# displaysWhenScreenProfileChanges

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the window context should be updated when the screen profile changes or when the window moves to a different screen.

**Availability**:
- macOS

## Declaration

```swift
var displaysWhenScreenProfileChanges: Bool { get set }
```

```objc
@property BOOL displaysWhenScreenProfileChanges;
```

#### Discussion

The value of this property is [`true`](../../Swift/true.md) when the window context should be updated when the ColorSync profile of the current screen changes or when a majority of the window is moved to a different screen whose profile is different than the previous screen; otherwise, [`false`](../../Swift/false.md). The default value is [`false`](../../Swift/false.md).

After the window context is updated, the window is told to display itself. If you need to update offscreen caches for the window, you should register to receive the [`didChangeScreenProfileNotification`](./didchangescreenprofilenotification.md) notification.

## See Also

### Accessing Screen Information
- [var screen: NSScreen?](./screen.md)
  The screen the window is on.
- [var deepestScreen: NSScreen?](./deepestscreen.md)
  The deepest screen the window is on (it may be split over several screens).


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindow/displayswhenscreenprofilechanges)*
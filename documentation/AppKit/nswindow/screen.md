# screen

**Framework**: AppKit  
**Kind**: property

The screen the window is on.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var screen: NSScreen? { get }
```

#### Discussion

The value of this property is the screen where most of the window is on; it is `nil` when the window is offscreen.

## See Also

- [var deepestScreen: NSScreen?](nswindow/deepestscreen.md)
  The deepest screen the window is on (it may be split over several screens).
- [var displaysWhenScreenProfileChanges: Bool](nswindow/displayswhenscreenprofilechanges.md)
  A Boolean value that indicates whether the window context should be updated when the screen profile changes or when the window moves to a different screen.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindow/screen)*
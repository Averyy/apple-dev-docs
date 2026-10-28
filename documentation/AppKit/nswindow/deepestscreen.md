# deepestScreen

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The deepest screen the window is on (it may be split over several screens).

**Availability**:
- macOS

## Declaration

```swift
var deepestScreen: NSScreen? { get }
```

```objc
@property (strong, readonly, nullable) NSScreen * deepestScreen;
```

## Discussion

The value of this property is `nil` when the window is offscreen.

## See Also

### Accessing Screen Information
- [var screen: NSScreen?](./screen.md)
  The screen the window is on.
- [var displaysWhenScreenProfileChanges: Bool](./displayswhenscreenprofilechanges.md)
  A Boolean value that indicates whether the window context should be updated when the screen profile changes or when the window moves to a different screen.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindow/deepestscreen)*
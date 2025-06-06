# isMovableByWindowBackground

**Framework**: AppKit  
**Kind**: property

A Boolean value that indicates whether the window is movable by clicking and dragging anywhere in its background.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var isMovableByWindowBackground: Bool { get set }
```

#### Discussion

The value of this property is [`true`](https://developer.apple.com/documentation/swift/true) when the window is movable by clicking and dragging anywhere in its background; otherwise, [`false`](https://developer.apple.com/documentation/swift/false).

A window with a style mask of `NSTexturedBackgroundWindowMask` is movable by background by default. Sheets and drawers cannot be movable by window background.

## See Also

- [var isMovable: Bool](nswindow/ismovable.md)
  A Boolean value that indicates whether the window can be dragged by clicking in its title bar or background.
- [func center()](nswindow/center.md)
  Sets the window’s location to the center of the screen.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindow/ismovablebywindowbackground)*
# isMovableByWindowBackground

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the window is movable by clicking and dragging anywhere in its background.

**Availability**:
- macOS

## Declaration

```swift
var isMovableByWindowBackground: Bool { get set }
```

```objc
@property (getter=isMovableByWindowBackground) BOOL movableByWindowBackground;
```

#### Discussion

The value of this property is [`true`](../../Swift/true.md) when the window is movable by clicking and dragging anywhere in its background; otherwise, [`false`](../../Swift/false.md).

A window with a style mask of `NSTexturedBackgroundWindowMask` is movable by background by default. Sheets and drawers cannot be movable by window background.

## See Also

### Moving Windows
- [var isMovable: Bool](./ismovable.md)
  A Boolean value that indicates whether the window can be dragged by clicking in its title bar or background.
- [func center()](./center%28%29.md)
  Sets the window’s location to the center of the screen.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindow/ismovablebywindowbackground)*
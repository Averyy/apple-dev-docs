# isMousePoint(_:in:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns whether a region of the view contains a specified point, accounting for whether the view is flipped or not.

**Availability**:
- macOS

## Declaration

```swift
func isMousePoint(_ point: NSPoint, in rect: NSRect) -> Bool
```

```objc
- (BOOL) mouse:(NSPoint) point inRect:(NSRect) rect;
```

#### Return Value

[`true`](../../Swift/true.md) if `aRect` contains `aPoint`, [`false`](../../Swift/false.md) otherwise.

#### Discussion

Point-in-rectangle functions generally assume that the bottom edge of a rectangle is outside of the rectangle boundaries, while the upper edge is inside the boundaries. This method views `aRect` from the point of view of the user—that is, this method always treats the bottom edge of the rectangle as the one closest to the bottom edge of the user’s screen. By making this adjustment, this function ensures consistent mouse-detection behavior from the user’s perspective.

Never use the Foundation’s [`NSPointInRect(_:_:)`](../../Foundation/nspointinrect%28_,_%29.md) function as a substitute for this method. It doesn’t account for flipped coordinate systems.

## Parameters

- `point`: A point that is expressed in the view’s coordinate system. This point generally represents the hot spot of the mouse cursor.
- `rect`: A rectangle that is expressed in the view’s coordinate system.

## See Also

### Related Documentation
- [func convert(NSPoint, from: NSView?) -> NSPoint](./convert%28_,from%29-1dq9l.md)
  Converts a point from the coordinate system of a given view to that of the view.
- [func NSMouseInRect(NSPoint, NSRect, Bool) -> Bool](../../Foundation/nsmouseinrect%28_,_,_%29.md)
  Returns a Boolean value that indicates whether the point is in the specified rectangle.
- [var isFlipped: Bool](./isflipped.md)
  A Boolean value indicating whether the view uses a flipped coordinate system.
### Handling Events in the View
- [func acceptsFirstMouse(for: NSEvent?) -> Bool](./acceptsfirstmouse%28for%29.md)
  Returns a Boolean value that indicates whether the view accepts the initial mouse-down event.
- [func hitTest(NSPoint) -> NSView?](./hittest%28_%29.md)
  Returns the farthest descendant of the view in the view hierarchy (including itself) that contains a specified point, or `nil` if that point lies completely outside the view.
- [func performKeyEquivalent(with: NSEvent) -> Bool](./performkeyequivalent%28with%29.md)
  Implemented by subclasses to respond to key equivalents (also known as keyboard shortcuts).
- [func rightMouseDown(with: NSEvent)](../nsresponder/rightmousedown%28with%29.md)
  Informs the receiver that the user has pressed the right mouse button.
- [var mouseDownCanMoveWindow: Bool](./mousedowncanmovewindow.md)
  A Boolean value indicating whether the view can pass mouse down events through to its superviews.
- [var inputContext: NSTextInputContext?](./inputcontext.md)
  The text input context object for the view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsview/ismousepoint(_:in:))*
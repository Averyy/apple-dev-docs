# trackMouse(with:in:of:untilMouseUp:)

**Framework**: AppKit  
**Kind**: method

Initiates the mouse tracking behavior in a cell.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func trackMouse(with event: NSEvent, in cellFrame: NSRect, of controlView: NSView, untilMouseUp flag: Bool) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if the mouse tracking conditions are met, otherwise [`false`](https://developer.apple.com/documentation/swift/false).

#### Discussion

This method is generally not overridden because the default implementation invokes other `NSCell` methods that can be overridden to handle specific events in a dragging session. This method’s return value depends on the `untilMouseUp` flag. If `untilMouseUp` is set to [`true`](https://developer.apple.com/documentation/swift/true), this method returns [`true`](https://developer.apple.com/documentation/swift/true) if the mouse button goes up while the cursor is anywhere; [`false`](https://developer.apple.com/documentation/swift/false), otherwise. If `untilMouseUp` is set to [`false`](https://developer.apple.com/documentation/swift/false), this method returns [`true`](https://developer.apple.com/documentation/swift/true) if the mouse button goes up while the cursor is within `cellFrame`; [`false`](https://developer.apple.com/documentation/swift/false), otherwise.

This method first invokes [`startTracking(at:in:)`](nscell/starttracking(at:in:).md). If that method returns [`true`](https://developer.apple.com/documentation/swift/true), then as mouse-dragged events are intercepted, [`continueTracking(last:current:in:)`](nscell/continuetracking(last:current:in:).md) is invoked until either the method returns [`false`](https://developer.apple.com/documentation/swift/false) or the mouse is released. Finally, [`stopTracking(last:current:in:mouseIsUp:)`](nscell/stoptracking(last:current:in:mouseisup:).md) is invoked if the mouse is released. If `untilMouseUp` is [`true`](https://developer.apple.com/documentation/swift/true), it’s invoked when the mouse button goes up while the cursor is anywhere. If `untilMouseUp` is [`false`](https://developer.apple.com/documentation/swift/false), it’s invoked when the mouse button goes up while the cursor is within `cellFrame`. You usually override one or more of these methods to respond to specific mouse events.

## Parameters

- `event`: The event that caused the mouse tracking to occur.
- `cellFrame`: The receiver’s frame rectangle.
- `controlView`: The view containing the receiver. This is usually an   object.
- `flag`: If  , mouse tracking continues until the user releases the mouse button. If  , tracking continues until the cursor leaves the tracking rectangle, specified by the   parameter, regardless of the mouse button state. See the discussion for more information.

## See Also

- [func startTracking(at: NSPoint, in: NSView) -> Bool](nscell/starttracking(at:in:).md)
  Begins tracking mouse events within the receiver.
- [func continueTracking(last: NSPoint, current: NSPoint, in: NSView) -> Bool](nscell/continuetracking(last:current:in:).md)
  Returns a Boolean value that indicates whether mouse tracking should continue in the receiving cell.
- [func stopTracking(last: NSPoint, current: NSPoint, in: NSView, mouseIsUp: Bool)](nscell/stoptracking(last:current:in:mouseisup:).md)
  Stops tracking mouse events within the receiver.
- [var mouseDownFlags: Int](nscell/mousedownflags.md)
  The modifier flags for the last (left) mouse-down event.
- [class var prefersTrackingUntilMouseUp: Bool](nscell/preferstrackinguntilmouseup.md)
  Returns a Boolean value that indicates whether tracking stops when the cursor leaves the cell.
- [func getPeriodicDelay(UnsafeMutablePointer<Float>, interval: UnsafeMutablePointer<Float>)](nscell/getperiodicdelay(_:interval:).md)
  Returns the initial delay and repeat values for continuous sending of action messages to target objects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscell/trackmouse(with:in:of:untilmouseup:))*
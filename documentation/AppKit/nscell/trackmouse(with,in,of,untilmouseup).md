# trackMouse(with:in:of:untilMouseUp:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Initiates the mouse tracking behavior in a cell.

**Availability**:
- macOS

## Declaration

```swift
func trackMouse(with event: NSEvent, in cellFrame: NSRect, of controlView: NSView, untilMouseUp flag: Bool) -> Bool
```

```objc
- (BOOL) trackMouse:(NSEvent *) event inRect:(NSRect) cellFrame ofView:(NSView *) controlView untilMouseUp:(BOOL) flag;
```

## Return Value

[`true`](../../Swift/true.md) if the mouse tracking conditions are met, otherwise [`false`](../../Swift/false.md).

## Discussion

This method is generally not overridden because the default implementation invokes other `NSCell` methods that can be overridden to handle specific events in a dragging session. This method’s return value depends on the `untilMouseUp` flag. If `untilMouseUp` is set to [`true`](../../Swift/true.md), this method returns [`true`](../../Swift/true.md) if the mouse button goes up while the cursor is anywhere; [`false`](../../Swift/false.md), otherwise. If `untilMouseUp` is set to [`false`](../../Swift/false.md), this method returns [`true`](../../Swift/true.md) if the mouse button goes up while the cursor is within `cellFrame`; [`false`](../../Swift/false.md), otherwise.

This method first invokes [`startTracking(at:in:)`](./starttracking%28at,in%29.md). If that method returns [`true`](../../Swift/true.md), then as mouse-dragged events are intercepted, [`continueTracking(last:current:in:)`](./continuetracking%28last,current,in%29.md) is invoked until either the method returns [`false`](../../Swift/false.md) or the mouse is released. Finally, [`stopTracking(last:current:in:mouseIsUp:)`](./stoptracking%28last,current,in,mouseisup%29.md) is invoked if the mouse is released. If `untilMouseUp` is [`true`](../../Swift/true.md), it’s invoked when the mouse button goes up while the cursor is anywhere. If `untilMouseUp` is [`false`](../../Swift/false.md), it’s invoked when the mouse button goes up while the cursor is within `cellFrame`. You usually override one or more of these methods to respond to specific mouse events.

## Parameters

- `event`: The event that caused the mouse tracking to occur.
- `cellFrame`: The receiver’s frame rectangle.
- `controlView`: The view containing the receiver. This is usually an `NSControl` object.
- `flag`: If [`true`](../../Swift/true.md), mouse tracking continues until the user releases the mouse button. If [`false`](../../Swift/false.md), tracking continues until the cursor leaves the tracking rectangle, specified by the `cellFrame` parameter, regardless of the mouse button state. See the discussion for more information.

## See Also

### Tracking the Mouse
- [func startTracking(at: NSPoint, in: NSView) -> Bool](./starttracking%28at,in%29.md)
  Begins tracking mouse events within the receiver.
- [func continueTracking(last: NSPoint, current: NSPoint, in: NSView) -> Bool](./continuetracking%28last,current,in%29.md)
  Returns a Boolean value that indicates whether mouse tracking should continue in the receiving cell.
- [func stopTracking(last: NSPoint, current: NSPoint, in: NSView, mouseIsUp: Bool)](./stoptracking%28last,current,in,mouseisup%29.md)
  Stops tracking mouse events within the receiver.
- [var mouseDownFlags: Int](./mousedownflags.md)
  The modifier flags for the last (left) mouse-down event.
- [class var prefersTrackingUntilMouseUp: Bool](./preferstrackinguntilmouseup.md)
  Returns a Boolean value that indicates whether tracking stops when the cursor leaves the cell.
- [func getPeriodicDelay(UnsafeMutablePointer<Float>, interval: UnsafeMutablePointer<Float>)](./getperiodicdelay%28_,interval%29.md)
  Returns the initial delay and repeat values for continuous sending of action messages to target objects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscell/trackmouse(with:in:of:untilmouseup:))*
# startTracking(at:in:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Begins tracking mouse events within the receiver.

**Availability**:
- macOS

## Declaration

```swift
func startTracking(at startPoint: NSPoint, in controlView: NSView) -> Bool
```

```objc
- (BOOL) startTrackingAt:(NSPoint) startPoint inView:(NSView *) controlView;
```

#### Return Value

[`true`](../../Swift/true.md) if the receiver is set to respond continuously or set to respond when the mouse is dragged, otherwise [`false`](../../Swift/false.md).

#### Discussion

The `NSCell` implementation of [`trackMouse(with:in:of:untilMouseUp:)`](./trackmouse%28with,in,of,untilmouseup%29.md) invokes this method when tracking begins.  Subclasses can override this method to implement special mouse-tracking behavior at the beginning of mouse tracking—for example, displaying a special cursor.

## Parameters

- `startPoint`: The initial location of the cursor.
- `controlView`: The `NSControl` object managing the receiver.

## See Also

### Tracking the Mouse
- [func trackMouse(with: NSEvent, in: NSRect, of: NSView, untilMouseUp: Bool) -> Bool](./trackmouse%28with,in,of,untilmouseup%29.md)
  Initiates the mouse tracking behavior in a cell.
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

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscell/starttracking(at:in:))*
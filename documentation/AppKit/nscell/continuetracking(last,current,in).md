# continueTracking(last:current:in:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns a Boolean value that indicates whether mouse tracking should continue in the receiving cell.

**Availability**:
- macOS

## Declaration

```swift
func continueTracking(last lastPoint: NSPoint, current currentPoint: NSPoint, in controlView: NSView) -> Bool
```

```objc
- (BOOL) continueTracking:(NSPoint) lastPoint at:(NSPoint) currentPoint inView:(NSView *) controlView;
```

#### Return Value

[`true`](../../Swift/true.md) if mouse tracking should continue, otherwise [`false`](../../Swift/false.md).

#### Discussion

This method is invoked in [`trackMouse(with:in:of:untilMouseUp:)`](./trackmouse%28with,in,of,untilmouseup%29.md). The default implementation returns [`true`](../../Swift/true.md) if the cell is set to continuously send action messages to its target when the mouse button is down or the mouse is being dragged. Subclasses can override this method to provide more sophisticated tracking behavior.

## Parameters

- `lastPoint`: Contains either the initial location of the cursor when tracking began or the previous current point.
- `currentPoint`: The current location of the cursor.
- `controlView`: The `NSControl` object managing the receiver.

## See Also

### Tracking the Mouse
- [func trackMouse(with: NSEvent, in: NSRect, of: NSView, untilMouseUp: Bool) -> Bool](./trackmouse%28with,in,of,untilmouseup%29.md)
  Initiates the mouse tracking behavior in a cell.
- [func startTracking(at: NSPoint, in: NSView) -> Bool](./starttracking%28at,in%29.md)
  Begins tracking mouse events within the receiver.
- [func stopTracking(last: NSPoint, current: NSPoint, in: NSView, mouseIsUp: Bool)](./stoptracking%28last,current,in,mouseisup%29.md)
  Stops tracking mouse events within the receiver.
- [var mouseDownFlags: Int](./mousedownflags.md)
  The modifier flags for the last (left) mouse-down event.
- [class var prefersTrackingUntilMouseUp: Bool](./preferstrackinguntilmouseup.md)
  Returns a Boolean value that indicates whether tracking stops when the cursor leaves the cell.
- [func getPeriodicDelay(UnsafeMutablePointer<Float>, interval: UnsafeMutablePointer<Float>)](./getperiodicdelay%28_,interval%29.md)
  Returns the initial delay and repeat values for continuous sending of action messages to target objects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscell/continuetracking(last:current:in:))*
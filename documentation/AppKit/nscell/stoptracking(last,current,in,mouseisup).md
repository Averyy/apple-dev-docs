# stopTracking(last:current:in:mouseIsUp:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Stops tracking mouse events within the receiver.

**Availability**:
- macOS

## Declaration

```swift
func stopTracking(last lastPoint: NSPoint, current stopPoint: NSPoint, in controlView: NSView, mouseIsUp flag: Bool)
```

```objc
- (void) stopTracking:(NSPoint) lastPoint at:(NSPoint) stopPoint inView:(NSView *) controlView mouseIsUp:(BOOL) flag;
```

#### Discussion

The default `NSCell` implementation of [`trackMouse(with:in:of:untilMouseUp:)`](./trackmouse%28with,in,of,untilmouseup%29.md) invokes this method when the cursor has left the bounds of the receiver or the mouse button goes up. The default `NSCell` implementation of this method does nothing. Subclasses often override this method to provide customized tracking behavior. The following example increments the state of a tristate cell when the mouse button is clicked:

```objc
- (void)stopTracking:(NSPoint)lastPoint at:(NSPoint)stopPoint
    inView:(NSView *)controlView mouseIsUp:(BOOL)flag
{
    if (flag == YES) {
        [self setTriState:([self triState]+1)];
    }
}
```

## Parameters

- `lastPoint`: Contains the previous position of the cursor.
- `stopPoint`: The current location of the cursor.
- `controlView`: The `NSControl` object managing the receiver.
- `flag`: If [`true`](../../Swift/true.md), this method was invoked because the user released the mouse button; otherwise, if [`false`](../../Swift/false.md), the cursor left the designated tracking rectangle.

## See Also

### Tracking the Mouse
- [func trackMouse(with: NSEvent, in: NSRect, of: NSView, untilMouseUp: Bool) -> Bool](./trackmouse%28with,in,of,untilmouseup%29.md)
  Initiates the mouse tracking behavior in a cell.
- [func startTracking(at: NSPoint, in: NSView) -> Bool](./starttracking%28at,in%29.md)
  Begins tracking mouse events within the receiver.
- [func continueTracking(last: NSPoint, current: NSPoint, in: NSView) -> Bool](./continuetracking%28last,current,in%29.md)
  Returns a Boolean value that indicates whether mouse tracking should continue in the receiving cell.
- [var mouseDownFlags: Int](./mousedownflags.md)
  The modifier flags for the last (left) mouse-down event.
- [class var prefersTrackingUntilMouseUp: Bool](./preferstrackinguntilmouseup.md)
  Returns a Boolean value that indicates whether tracking stops when the cursor leaves the cell.
- [func getPeriodicDelay(UnsafeMutablePointer<Float>, interval: UnsafeMutablePointer<Float>)](./getperiodicdelay%28_,interval%29.md)
  Returns the initial delay and repeat values for continuous sending of action messages to target objects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscell/stoptracking(last:current:in:mouseisup:))*
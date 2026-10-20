# prefersTrackingUntilMouseUp

**Framework**: AppKit  
**Kind**: property  
**Role**: Type Property

Returns a Boolean value that indicates whether tracking stops when the cursor leaves the cell.

**Availability**:
- macOS

## Declaration

```swift
class var prefersTrackingUntilMouseUp: Bool { get }
```

```objc
@property (class, readonly) BOOL prefersTrackingUntilMouseUp;
```

#### Return Value

[`true`](../../Swift/true.md) if tracking stops when the cursor leaves the cell, otherwise [`false`](../../Swift/false.md).

#### Discussion

The default implementation returns [`false`](../../Swift/false.md). Subclasses may override this method to return a different value.

## See Also

### Tracking the Mouse
- [func trackMouse(with: NSEvent, in: NSRect, of: NSView, untilMouseUp: Bool) -> Bool](./trackmouse%28with,in,of,untilmouseup%29.md)
  Initiates the mouse tracking behavior in a cell.
- [func startTracking(at: NSPoint, in: NSView) -> Bool](./starttracking%28at,in%29.md)
  Begins tracking mouse events within the receiver.
- [func continueTracking(last: NSPoint, current: NSPoint, in: NSView) -> Bool](./continuetracking%28last,current,in%29.md)
  Returns a Boolean value that indicates whether mouse tracking should continue in the receiving cell.
- [func stopTracking(last: NSPoint, current: NSPoint, in: NSView, mouseIsUp: Bool)](./stoptracking%28last,current,in,mouseisup%29.md)
  Stops tracking mouse events within the receiver.
- [var mouseDownFlags: Int](./mousedownflags.md)
  The modifier flags for the last (left) mouse-down event.
- [func getPeriodicDelay(UnsafeMutablePointer<Float>, interval: UnsafeMutablePointer<Float>)](./getperiodicdelay%28_,interval%29.md)
  Returns the initial delay and repeat values for continuous sending of action messages to target objects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscell/preferstrackinguntilmouseup)*
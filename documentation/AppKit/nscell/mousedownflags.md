# mouseDownFlags

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The modifier flags for the last (left) mouse-down event.

**Availability**:
- macOS

## Declaration

```swift
var mouseDownFlags: Int { get }
```

```objc
@property (readonly) NSInteger mouseDownFlags;
```

## Discussion

The value of this property is the value of the modifier flags from the most recent [`NSEvent`](../nsevent.md) object representing a mouse-down event. If tracking has not yet occurred or the event contained no modifier keys, the value of this property is `0`.

## See Also

### Related Documentation
- [var modifierFlags: NSEvent.ModifierFlags](../nsevent/modifierflags-swift.property.md)
  An integer bit field that indicates the pressed modifier keys.
### Tracking the Mouse
- [func trackMouse(with: NSEvent, in: NSRect, of: NSView, untilMouseUp: Bool) -> Bool](./trackmouse%28with,in,of,untilmouseup%29.md)
  Initiates the mouse tracking behavior in a cell.
- [func startTracking(at: NSPoint, in: NSView) -> Bool](./starttracking%28at,in%29.md)
  Begins tracking mouse events within the receiver.
- [func continueTracking(last: NSPoint, current: NSPoint, in: NSView) -> Bool](./continuetracking%28last,current,in%29.md)
  Returns a Boolean value that indicates whether mouse tracking should continue in the receiving cell.
- [func stopTracking(last: NSPoint, current: NSPoint, in: NSView, mouseIsUp: Bool)](./stoptracking%28last,current,in,mouseisup%29.md)
  Stops tracking mouse events within the receiver.
- [class var prefersTrackingUntilMouseUp: Bool](./preferstrackinguntilmouseup.md)
  Returns a Boolean value that indicates whether tracking stops when the cursor leaves the cell.
- [func getPeriodicDelay(UnsafeMutablePointer<Float>, interval: UnsafeMutablePointer<Float>)](./getperiodicdelay%28_,interval%29.md)
  Returns the initial delay and repeat values for continuous sending of action messages to target objects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscell/mousedownflags)*
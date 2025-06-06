# mouseDownFlags

**Framework**: AppKit  
**Kind**: property

The modifier flags for the last (left) mouse-down event.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var mouseDownFlags: Int { get }
```

#### Discussion

The value of this property is the value of the modifier flags from the most recent [`NSEvent`](nsevent.md) object representing a mouse-down event. If tracking has not yet occurred or the event contained no modifier keys, the value of this property is `0`.

## See Also

- [var modifierFlags: NSEvent.ModifierFlags](nsevent/modifierflags-swift.property.md)
  An integer bit field that indicates the pressed modifier keys.
- [func trackMouse(with: NSEvent, in: NSRect, of: NSView, untilMouseUp: Bool) -> Bool](nscell/trackmouse(with:in:of:untilmouseup:).md)
  Initiates the mouse tracking behavior in a cell.
- [func startTracking(at: NSPoint, in: NSView) -> Bool](nscell/starttracking(at:in:).md)
  Begins tracking mouse events within the receiver.
- [func continueTracking(last: NSPoint, current: NSPoint, in: NSView) -> Bool](nscell/continuetracking(last:current:in:).md)
  Returns a Boolean value that indicates whether mouse tracking should continue in the receiving cell.
- [func stopTracking(last: NSPoint, current: NSPoint, in: NSView, mouseIsUp: Bool)](nscell/stoptracking(last:current:in:mouseisup:).md)
  Stops tracking mouse events within the receiver.
- [class var prefersTrackingUntilMouseUp: Bool](nscell/preferstrackinguntilmouseup.md)
  Returns a Boolean value that indicates whether tracking stops when the cursor leaves the cell.
- [func getPeriodicDelay(UnsafeMutablePointer<Float>, interval: UnsafeMutablePointer<Float>)](nscell/getperiodicdelay(_:interval:).md)
  Returns the initial delay and repeat values for continuous sending of action messages to target objects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscell/mousedownflags)*
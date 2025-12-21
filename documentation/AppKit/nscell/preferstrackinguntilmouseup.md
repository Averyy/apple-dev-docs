# prefersTrackingUntilMouseUp

**Framework**: AppKit  
**Kind**: property

Returns a Boolean value that indicates whether tracking stops when the cursor leaves the cell.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
class var prefersTrackingUntilMouseUp: Bool { get }
```

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) if tracking stops when the cursor leaves the cell, otherwise [`false`](https://developer.apple.com/documentation/Swift/false).

#### Discussion

The default implementation returns [`false`](https://developer.apple.com/documentation/Swift/false). Subclasses may override this method to return a different value.

## See Also

- [func trackMouse(with: NSEvent, in: NSRect, of: NSView, untilMouseUp: Bool) -> Bool](nscell/trackmouse(with:in:of:untilmouseup:).md)
  Initiates the mouse tracking behavior in a cell.
- [func startTracking(at: NSPoint, in: NSView) -> Bool](nscell/starttracking(at:in:).md)
  Begins tracking mouse events within the receiver.
- [func continueTracking(last: NSPoint, current: NSPoint, in: NSView) -> Bool](nscell/continuetracking(last:current:in:).md)
  Returns a Boolean value that indicates whether mouse tracking should continue in the receiving cell.
- [func stopTracking(last: NSPoint, current: NSPoint, in: NSView, mouseIsUp: Bool)](nscell/stoptracking(last:current:in:mouseisup:).md)
  Stops tracking mouse events within the receiver.
- [var mouseDownFlags: Int](nscell/mousedownflags.md)
  The modifier flags for the last (left) mouse-down event.
- [func getPeriodicDelay(UnsafeMutablePointer<Float>, interval: UnsafeMutablePointer<Float>)](nscell/getperiodicdelay(_:interval:).md)
  Returns the initial delay and repeat values for continuous sending of action messages to target objects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscell/preferstrackinguntilmouseup)*
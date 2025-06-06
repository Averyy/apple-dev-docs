# continueTracking(last:current:in:)

**Framework**: AppKit  
**Kind**: method

Returns a Boolean value that indicates whether mouse tracking should continue in the receiving cell.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func continueTracking(last lastPoint: NSPoint, current currentPoint: NSPoint, in controlView: NSView) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if mouse tracking should continue, otherwise [`false`](https://developer.apple.com/documentation/swift/false).

#### Discussion

This method is invoked in [`trackMouse(with:in:of:untilMouseUp:)`](nscell/trackmouse(with:in:of:untilmouseup:).md). The default implementation returns [`true`](https://developer.apple.com/documentation/swift/true) if the cell is set to continuously send action messages to its target when the mouse button is down or the mouse is being dragged. Subclasses can override this method to provide more sophisticated tracking behavior.

## Parameters

- `lastPoint`: Contains either the initial location of the cursor when tracking began or the previous current point.
- `currentPoint`: The current location of the cursor.
- `controlView`: The   object managing the receiver.

## See Also

- [func trackMouse(with: NSEvent, in: NSRect, of: NSView, untilMouseUp: Bool) -> Bool](nscell/trackmouse(with:in:of:untilmouseup:).md)
  Initiates the mouse tracking behavior in a cell.
- [func startTracking(at: NSPoint, in: NSView) -> Bool](nscell/starttracking(at:in:).md)
  Begins tracking mouse events within the receiver.
- [func stopTracking(last: NSPoint, current: NSPoint, in: NSView, mouseIsUp: Bool)](nscell/stoptracking(last:current:in:mouseisup:).md)
  Stops tracking mouse events within the receiver.
- [var mouseDownFlags: Int](nscell/mousedownflags.md)
  The modifier flags for the last (left) mouse-down event.
- [class var prefersTrackingUntilMouseUp: Bool](nscell/preferstrackinguntilmouseup.md)
  Returns a Boolean value that indicates whether tracking stops when the cursor leaves the cell.
- [func getPeriodicDelay(UnsafeMutablePointer<Float>, interval: UnsafeMutablePointer<Float>)](nscell/getperiodicdelay(_:interval:).md)
  Returns the initial delay and repeat values for continuous sending of action messages to target objects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscell/continuetracking(last:current:in:))*
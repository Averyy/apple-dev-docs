# getPeriodicDelay(_:interval:)

**Framework**: AppKit  
**Kind**: method

Returns the initial delay and repeat values for continuous sending of action messages to target objects.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func getPeriodicDelay(_ delay: UnsafeMutablePointer<Float>, interval: UnsafeMutablePointer<Float>)
```

#### Discussion

The default implementation returns a delay of `0.2` and an interval of `0.025` seconds. Subclasses can override this method to supply their own delay and interval values.

## Parameters

- `delay`: On input, a pointer to a floating-point variable. On output, the variable contains the current delay (measured in seconds) before messages are sent. This parameter must not be  .
- `interval`: On input, a pointer to a floating point variable. On output, the variable contains the interval (measured in seconds) at which messages are sent. This parameter must not be  .

## See Also

- [var isContinuous: Bool](nscell/iscontinuous.md)
  A Boolean value indicating whether the cell sends its action message continuously during mouse tracking.
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
- [class var prefersTrackingUntilMouseUp: Bool](nscell/preferstrackinguntilmouseup.md)
  Returns a Boolean value that indicates whether tracking stops when the cursor leaves the cell.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscell/getperiodicdelay(_:interval:))*
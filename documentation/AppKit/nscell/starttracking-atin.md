# startTracking(at:in:)

**Framework**: AppKit  
**Kind**: method

Begins tracking mouse events within the receiver.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func startTracking(at startPoint: NSPoint, in controlView: NSView) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if the receiver is set to respond continuously or set to respond when the mouse is dragged, otherwise [`false`](https://developer.apple.com/documentation/swift/false).

#### Discussion

The `NSCell` implementation of [`trackMouse(with:in:of:untilMouseUp:)`](nscell/trackmouse(with:in:of:untilmouseup:).md) invokes this method when tracking begins.  Subclasses can override this method to implement special mouse-tracking behavior at the beginning of mouse tracking—for example, displaying a special cursor.

## Parameters

- `startPoint`: The initial location of the cursor.
- `controlView`: The   object managing the receiver.

## See Also

- [func trackMouse(with: NSEvent, in: NSRect, of: NSView, untilMouseUp: Bool) -> Bool](nscell/trackmouse(with:in:of:untilmouseup:).md)
  Initiates the mouse tracking behavior in a cell.
- [func continueTracking(last: NSPoint, current: NSPoint, in: NSView) -> Bool](nscell/continuetracking(last:current:in:).md)
  Returns a Boolean value that indicates whether mouse tracking should continue in the receiving cell.
- [func stopTracking(last: NSPoint, current: NSPoint, in: NSView, mouseIsUp: Bool)](nscell/stoptracking(last:current:in:mouseisup:).md)
  Stops tracking mouse events within the receiver.
- [var mouseDownFlags: Int](nscell/mousedownflags.md)
  The modifier flags for the last (left) mouse-down event.
- [class var prefersTrackingUntilMouseUp: Bool](nscell/preferstrackinguntilmouseup.md)
  Returns a Boolean value that indicates whether tracking stops when the cursor leaves the cell.
- [func getPeriodicDelay(UnsafeMutablePointer<Float>, interval: UnsafeMutablePointer<Float>)](nscell/getperiodicdelay(_:interval:).md)
  Returns the initial delay and repeat values for continuous sending of action messages to target objects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscell/starttracking(at:in:))*
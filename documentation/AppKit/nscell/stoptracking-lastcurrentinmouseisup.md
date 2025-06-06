# stopTracking(last:current:in:mouseIsUp:)

**Framework**: AppKit  
**Kind**: method

Stops tracking mouse events within the receiver.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func stopTracking(last lastPoint: NSPoint, current stopPoint: NSPoint, in controlView: NSView, mouseIsUp flag: Bool)
```

#### Discussion

The default `NSCell` implementation of [`trackMouse(with:in:of:untilMouseUp:)`](nscell/trackmouse(with:in:of:untilmouseup:).md) invokes this method when the cursor has left the bounds of the receiver or the mouse button goes up. The default `NSCell` implementation of this method does nothing. Subclasses often override this method to provide customized tracking behavior. The following example increments the state of a tristate cell when the mouse button is clicked:

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
- `controlView`: The   object managing the receiver.
- `flag`: If  , this method was invoked because the user released the mouse button; otherwise, if  , the cursor left the designated tracking rectangle.

## See Also

- [func trackMouse(with: NSEvent, in: NSRect, of: NSView, untilMouseUp: Bool) -> Bool](nscell/trackmouse(with:in:of:untilmouseup:).md)
  Initiates the mouse tracking behavior in a cell.
- [func startTracking(at: NSPoint, in: NSView) -> Bool](nscell/starttracking(at:in:).md)
  Begins tracking mouse events within the receiver.
- [func continueTracking(last: NSPoint, current: NSPoint, in: NSView) -> Bool](nscell/continuetracking(last:current:in:).md)
  Returns a Boolean value that indicates whether mouse tracking should continue in the receiving cell.
- [var mouseDownFlags: Int](nscell/mousedownflags.md)
  The modifier flags for the last (left) mouse-down event.
- [class var prefersTrackingUntilMouseUp: Bool](nscell/preferstrackinguntilmouseup.md)
  Returns a Boolean value that indicates whether tracking stops when the cursor leaves the cell.
- [func getPeriodicDelay(UnsafeMutablePointer<Float>, interval: UnsafeMutablePointer<Float>)](nscell/getperiodicdelay(_:interval:).md)
  Returns the initial delay and repeat values for continuous sending of action messages to target objects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscell/stoptracking(last:current:in:mouseisup:))*
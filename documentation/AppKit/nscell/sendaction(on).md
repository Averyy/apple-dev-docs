# sendAction(on:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Sets the conditions on which the receiver sends action messages to its target.

**Availability**:
- macOS

## Declaration

```swift
func sendAction(on mask: NSEvent.EventTypeMask) -> Int
```

```objc
- (NSInteger) sendActionOn:(NSEventMask) mask;
```

#### Return Value

A bit mask containing the previous settings. This bit mask uses the same values as specified in the `mask` parameter.

#### Discussion

You use this method during mouse tracking when the mouse button changes state, the mouse moves, or if the cell is marked to send its action continuously while tracking. Because of this, the only bits checked in `mask` are [`NSLeftMouseDownMask`](../nsleftmousedownmask.md),  [`NSLeftMouseUpMask`](../nsleftmouseupmask.md), [`NSLeftMouseDraggedMask`](../nsleftmousedraggedmask.md), and [`NSPeriodicMask`](../nsperiodicmask.md), which are declared in the [`NSEvent`](../nsevent.md) class reference.

You can use the [`isContinuous`](./iscontinuous.md) property to turn on the flag corresponding to [`NSPeriodicMask`](../nsperiodicmask.md) or [`NSLeftMouseDraggedMask`](../nsleftmousedraggedmask.md), whichever is appropriate to the given subclass of `NSCell`.

## Parameters

- `mask`: A bit mask containing the conditions for sending the action. The only conditions that are actually checked are associated with the [`NSLeftMouseDownMask`](../nsleftmousedownmask.md),  [`NSLeftMouseUpMask`](../nsleftmouseupmask.md), [`NSLeftMouseDraggedMask`](../nsleftmousedraggedmask.md), and [`NSPeriodicMask`](../nsperiodicmask.md) bits.

## See Also

### Managing the Target and Action
- [var action: Selector?](./action.md)
  The action performed by the cell.
- [var target: AnyObject?](./target.md)
  The object that receives the cell’s action messages.
- [var isContinuous: Bool](./iscontinuous.md)
  A Boolean value indicating whether the cell sends its action message continuously during mouse tracking.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscell/sendaction(on:))*
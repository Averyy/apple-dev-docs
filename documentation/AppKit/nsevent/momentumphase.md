# momentumPhase

**Framework**: AppKit  
**Kind**: property

The momentum phase for a scroll or flick gesture.

**Availability**:
- macOS 10.7+

## Declaration

```swift
var momentumPhase: NSEvent.Phase { get }
```

#### Discussion

This property is valid for [`NSScrollWheel`](nsscrollwheel.md) events. With the Magic Mouse and some trackpads, the user can use a scroll wheel or flick gesture resulting in a stream of scroll events that dissipate over time.

The location of these scroll wheel events changes as the user moves the cursor. These events are attached to the view that is under the cursor when the flick occurs. A custom view can use this method to recognize these momentum scroll events and further route the event to the appropriate sub component.

See [`NSEvent.Phase`](nsevent/phase-swift.struct.md) for possible values.

## See Also

- [var deltaX: CGFloat](nsevent/deltax.md)
  The x-coordinate change for scroll wheel, mouse-move, mouse-drag, and swipe events.
- [var deltaY: CGFloat](nsevent/deltay.md)
  The y-coordinate change for scroll wheel, mouse-move, mouse-drag, and swipe events.
- [var deltaZ: CGFloat](nsevent/deltaz.md)
  The z-coordinate change for a scroll wheel, mouse-move, or mouse-drag event.
- [var hasPreciseScrollingDeltas: Bool](nsevent/hasprecisescrollingdeltas.md)
  A Boolean value that indicates whether precise scrolling deltas are available.
- [var scrollingDeltaX: CGFloat](nsevent/scrollingdeltax.md)
  The scroll wheel’s horizontal delta.
- [var scrollingDeltaY: CGFloat](nsevent/scrollingdeltay.md)
  The scroll wheel’s vertical delta.
- [var isDirectionInvertedFromDevice: Bool](nsevent/isdirectioninvertedfromdevice.md)
  A Boolean value that indicates whether the user has changed the device inversion.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsevent/momentumphase)*
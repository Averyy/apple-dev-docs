# trackingRepeated

**Framework**: AppKit  
**Kind**: property  
**Role**: Type Property

A repeated tracking began event in the control. For this event the click count is greater than one.

**Availability**:
- macOS 27.0+

## Declaration

```swift
static var trackingRepeated: NSControl.Events { get }
```

```c
NSControlEventTrackingRepeated
```

## See Also

### Tracking events
- [static var trackingBegan: NSControl.Events](./trackingbegan.md)
  A tracking began event in the control.
- [static var trackingInside: NSControl.Events](./trackinginside.md)
  An event where the pointer or touch moves inside the bounds of the control.
- [static var trackingOutside: NSControl.Events](./trackingoutside.md)
  An event where the pointer or touch moves outside the bounds of the control.
- [static var trackingEntered: NSControl.Events](./trackingentered.md)
  An event where tracking transitions from outside to inside the bounds of the control.
- [static var trackingExited: NSControl.Events](./trackingexited.md)
  An event where tracking transitions from inside to outside the bounds of the control.
- [static var trackingEndedInside: NSControl.Events](./trackingendedinside.md)
  A tracking ended event where the pointer or touch is inside the bounds of the control.
- [static var trackingEndedOutside: NSControl.Events](./trackingendedoutside.md)
  A tracking ended event where the pointer or touch is outside the bounds of the control.
- [static var trackingCancelled: NSControl.Events](./trackingcancelled.md)
  A system event canceling the current tracking for the control.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscontrol/events/trackingrepeated)*
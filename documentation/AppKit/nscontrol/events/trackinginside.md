# trackingInside

**Framework**: AppKit  
**Kind**: property  
**Role**: Type Property

An event where the pointer or touch moves inside the bounds of the control.

**Availability**:
- macOS 11.0+

## Declaration

```swift
static var trackingInside: NSControl.Events { get }
```

```c
NSControlEventTrackingInside
```

## See Also

### Tracking events
- [static var trackingBegan: NSControl.Events](./trackingbegan.md)
  A tracking began event in the control.
- [static var trackingRepeated: NSControl.Events](./trackingrepeated.md)
  A repeated tracking began event in the control. For this event the click count is greater than one.
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

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscontrol/events/trackinginside)*
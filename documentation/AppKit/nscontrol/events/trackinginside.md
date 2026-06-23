# trackingInside

**Framework**: AppKit  
**Kind**: property

An event where the pointer or touch moves inside the bounds of the control.

**Availability**:
- macOS 11.0+

## Declaration

```swift
static var trackingInside: NSControl.Events { get }
```

## See Also

- [static var trackingBegan: NSControl.Events](nscontrol/events/trackingbegan.md)
  A tracking began event in the control.
- [static var trackingRepeated: NSControl.Events](nscontrol/events/trackingrepeated.md)
  A repeated tracking began event in the control. For this event the click count is greater than one.
- [static var trackingOutside: NSControl.Events](nscontrol/events/trackingoutside.md)
  An event where the pointer or touch moves outside the bounds of the control.
- [static var trackingEntered: NSControl.Events](nscontrol/events/trackingentered.md)
  An event where tracking transitions from outside to inside the bounds of the control.
- [static var trackingExited: NSControl.Events](nscontrol/events/trackingexited.md)
  An event where tracking transitions from inside to outside the bounds of the control.
- [static var trackingEndedInside: NSControl.Events](nscontrol/events/trackingendedinside.md)
  A tracking ended event where the pointer or touch is inside the bounds of the control.
- [static var trackingEndedOutside: NSControl.Events](nscontrol/events/trackingendedoutside.md)
  A tracking ended event where the pointer or touch is outside the bounds of the control.
- [static var trackingCancelled: NSControl.Events](nscontrol/events/trackingcancelled.md)
  A system event canceling the current tracking for the control.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscontrol/events/trackinginside)*
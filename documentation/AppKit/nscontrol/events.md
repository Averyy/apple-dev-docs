# NSControl.Events

**Framework**: AppKit  
**Kind**: struct

A set of events that a control can report to its target.

**Availability**:
- macOS 11.0+

## Declaration

```swift
struct Events
```

#### Discussion

You set up a control to send an action message to a target object by associating both target and action with one or more control events. To do this, call [`addTarget(_:action:for:)`](nscontrol/addtarget(_:action:for:).md) on the control for each target-action pair you want to specify.

```swift
let slider = NSSlider()
slider.addTarget(self, action: #selector(sliderValueChanged), for: .valueChanged)

let button = NSButton()
button.addTarget(self, action: #selector(buttonActivated), for: [.primaryActionTriggered, .menuActionTriggered])
```

Use tracking events to observe the progress of mouse interaction as it unfolds — for example, to respond to a drag in progress rather than only on completion. Use semantic events like [`valueChanged`](nscontrol/events/valuechanged.md), [`primaryActionTriggered`](nscontrol/events/primaryactiontriggered.md), or [`menuActionTriggered`](nscontrol/events/menuactiontriggered.md) to respond to higher-level, input-device-independent meanings. [`applicationReserved`](nscontrol/events/applicationreserved.md) is a range of bits available for app use.

## Topics

### Tracking events
- [static var trackingBegan: NSControl.Events](nscontrol/events/trackingbegan.md)
  A tracking began event in the control.
- [static var trackingRepeated: NSControl.Events](nscontrol/events/trackingrepeated.md)
  A repeated tracking began event in the control. For this event the click count is greater than one.
- [static var trackingInside: NSControl.Events](nscontrol/events/trackinginside.md)
  An event where the pointer or touch moves inside the bounds of the control.
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
### Semantic events
- [static var valueChanged: NSControl.Events](nscontrol/events/valuechanged.md)
  An event where dragging or otherwise manipulating a control causes it to emit a series of different values.
- [static var primaryActionTriggered: NSControl.Events](nscontrol/events/primaryactiontriggered.md)
  A semantic action triggered by buttons.
- [static var menuActionTriggered: NSControl.Events](nscontrol/events/menuactiontriggered.md)
  A menu action has triggered prior to the menu being presented.
### Aggregate events
- [static var allTrackingEvents: NSControl.Events](nscontrol/events/alltrackingevents.md)
  All tracking events.
- [static var allEvents: NSControl.Events](nscontrol/events/allevents.md)
  All events, including system events.
### Reserved ranges
- [static var applicationReserved: NSControl.Events](nscontrol/events/applicationreserved.md)
  A range of control-event values available for app use.
- [static var systemReserved: NSControl.Events](nscontrol/events/systemreserved.md)
  A range of control-event values reserved for internal framework use.
### Initializers
- [init(rawValue: UInt)](nscontrol/events/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../swift/bitwisecopyable.md)
- [Equatable](../swift/equatable.md)
- [ExpressibleByArrayLiteral](../swift/expressiblebyarrayliteral.md)
- [OptionSet](../swift/optionset.md)
- [RawRepresentable](../swift/rawrepresentable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)
- [SetAlgebra](../swift/setalgebra.md)

## See Also

- [func addTarget(Any?, action: Selector, for: NSControl.Events)](nscontrol/addtarget(_:action:for:).md)
  Registers a target-action pair for the specified control events.
- [func removeTarget(Any?, action: Selector?, for: NSControl.Events)](nscontrol/removetarget(_:action:for:).md)
  Stops the delivery of events to the specified target object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscontrol/events)*
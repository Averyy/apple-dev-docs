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
- [static var trackingRepeated: NSControl.Events](nscontrol/events/trackingrepeated.md)
- [static var trackingInside: NSControl.Events](nscontrol/events/trackinginside.md)
- [static var trackingOutside: NSControl.Events](nscontrol/events/trackingoutside.md)
- [static var trackingEntered: NSControl.Events](nscontrol/events/trackingentered.md)
- [static var trackingExited: NSControl.Events](nscontrol/events/trackingexited.md)
- [static var trackingEndedInside: NSControl.Events](nscontrol/events/trackingendedinside.md)
- [static var trackingEndedOutside: NSControl.Events](nscontrol/events/trackingendedoutside.md)
- [static var trackingCancelled: NSControl.Events](nscontrol/events/trackingcancelled.md)
### Semantic events
- [static var valueChanged: NSControl.Events](nscontrol/events/valuechanged.md)
- [static var primaryActionTriggered: NSControl.Events](nscontrol/events/primaryactiontriggered.md)
- [static var menuActionTriggered: NSControl.Events](nscontrol/events/menuactiontriggered.md)
### Aggregate events
- [static var allTrackingEvents: NSControl.Events](nscontrol/events/alltrackingevents.md)
- [static var allEvents: NSControl.Events](nscontrol/events/allevents.md)
### Reserved ranges
- [static var applicationReserved: NSControl.Events](nscontrol/events/applicationreserved.md)
- [static var systemReserved: NSControl.Events](nscontrol/events/systemreserved.md)
### Initializers
- [init(rawValue: UInt)](nscontrol/events/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [OptionSet](../Swift/OptionSet.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [SetAlgebra](../Swift/SetAlgebra.md)

## See Also

- [func addTarget(Any?, action: Selector, for: NSControl.Events)](nscontrol/addtarget(_:action:for:).md)
  Registers a target-action pair for the specified control events.
- [func removeTarget(Any?, action: Selector?, for: NSControl.Events)](nscontrol/removetarget(_:action:for:).md)
  Stops the delivery of events to the specified target object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscontrol/events)*
# NSSegmentedControl.SwitchTracking

**Framework**: AppKit  
**Kind**: enum

The following constants specify the type of tracking behavior a segmented control exhibits. They are used by [`trackingMode`](nssegmentedcontrol/trackingmode.md).

**Availability**:
- macOS ?+

## Declaration

```swift
enum SwitchTracking
```

## Topics

### Constants
- [NSSegmentedControl.SwitchTracking.selectOne](nssegmentedcontrol/switchtracking/selectone.md)
  Only one segment in the control can be selected at a time.
- [NSSegmentedControl.SwitchTracking.selectAny](nssegmentedcontrol/switchtracking/selectany.md)
  One or more segment cells in the control can be selected at a time.
- [NSSegmentedControl.SwitchTracking.momentary](nssegmentedcontrol/switchtracking/momentary.md)
  A segment is selected only when the user is pressing the mouse down within the bounds of the segment. When the mouse is no longer down within the segment, the segment is automatically deselected. A momentary segmented control sends an action when the user clicks a segment, and another action when the user releases the segment. If configured as continuous (see [`isContinuous`](nscontrol/iscontinuous.md)), the control also sends actions at repeating intervals until the user releases the segment, at which point the control sends its final action.
- [NSSegmentedControl.SwitchTracking.momentaryAccelerator](nssegmentedcontrol/switchtracking/momentaryaccelerator.md)
  On pressure-sensitive systems, when the user force clicks a segment, a momentary accelerator segmented control sends repeating actions as pressure changes occur. The control stops sending actions when the user releases pressure. A document-based app, for example, might implement a momentary accelerator segmented control in order to allow a user to adjust the speed of paging by using variable pressure. In this example, actions are sent to the app to indicate when pressure on the control has changed. The app then determines the amount of pressure currently applied, and adjusts navigation speed accordingly.
### Initializers
- [init?(rawValue: UInt)](nssegmentedcontrol/switchtracking/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [var trackingMode: NSSegmentedControl.SwitchTracking](nssegmentedcontrol/trackingmode.md)
  The type of tracking behavior the control exhibits.
- [var segmentStyle: NSSegmentedControl.Style](nssegmentedcontrol/segmentstyle.md)
  The visual style used to display the control.
- [NSSegmentedControl.Style](nssegmentedcontrol/style.md)
  The following constants specify the visual style used to display the segmented control. They are used by [`segmentStyle`](nssegmentedcontrol/segmentstyle.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssegmentedcontrol/switchtracking)*
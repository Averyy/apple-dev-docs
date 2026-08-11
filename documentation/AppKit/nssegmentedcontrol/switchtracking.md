# NSSegmentedControl.SwitchTracking

**Framework**: AppKit  
**Kind**: enum

Constants that specify the type of tracking behavior a segmented control exhibits.

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
  A tracking mode that selects a segment when a person clicks within the bounds of the segment.
- [NSSegmentedControl.SwitchTracking.momentaryAccelerator](nssegmentedcontrol/switchtracking/momentaryaccelerator.md)
  A tracking mode that sends repeating actions as pressure changes on Force Touch systems, stopping when someone releases the segment.
### Initializers
- [init?(rawValue: UInt)](nssegmentedcontrol/switchtracking/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var trackingMode: NSSegmentedControl.SwitchTracking](nssegmentedcontrol/trackingmode.md)
  The type of tracking behavior the control exhibits.
- [var segmentStyle: NSSegmentedControl.Style](nssegmentedcontrol/segmentstyle.md)
  The visual style used to display the control.
- [NSSegmentedControl.Style](nssegmentedcontrol/style.md)
  The following constants specify the visual style used to display the segmented control. They are used by [`segmentStyle`](nssegmentedcontrol/segmentstyle.md).
- [var role: NSSegmentedControl.Role](nssegmentedcontrol/role-swift.property.md)
- [NSSegmentedControl.Role](nssegmentedcontrol/role-swift.enum.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssegmentedcontrol/switchtracking)*
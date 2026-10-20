# NSSegmentedControl.SwitchTracking

**Framework**: AppKit  
**Kind**: enum  
**Role**: Enumeration

Constants that specify the type of tracking behavior a segmented control exhibits.

**Availability**:
- macOS

## Declaration

```swift
enum SwitchTracking
```

```c
enum NSSegmentSwitchTracking : NSUInteger;
```

## Topics

### Constants
- [NSSegmentedControl.SwitchTracking.selectOne](./switchtracking/selectone.md)
  Only one segment in the control can be selected at a time.
- [NSSegmentedControl.SwitchTracking.selectAny](./switchtracking/selectany.md)
  One or more segment cells in the control can be selected at a time.
- [NSSegmentedControl.SwitchTracking.momentary](./switchtracking/momentary.md)
  A tracking mode that selects a segment when a person clicks within the bounds of the segment.
- [NSSegmentedControl.SwitchTracking.momentaryAccelerator](./switchtracking/momentaryaccelerator.md)
  A tracking mode that sends repeating actions as pressure changes on Force Touch systems, stopping when someone releases the segment.
### Initializers
- [init?(rawValue: UInt)](./switchtracking/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Specifying the segment behavior
- [var trackingMode: NSSegmentedControl.SwitchTracking](./trackingmode.md)
  The type of tracking behavior the control exhibits.
- [var segmentStyle: NSSegmentedControl.Style](./segmentstyle.md)
  The visual style used to display the control.
- [NSSegmentedControl.Style](./style.md)
  The following constants specify the visual style used to display the segmented control. They are used by [`segmentStyle`](./segmentstyle.md).
- [var role: NSSegmentedControl.Role](./role-swift.property.md)
- [NSSegmentedControl.Role](./role-swift.enum.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssegmentedcontrol/switchtracking)*
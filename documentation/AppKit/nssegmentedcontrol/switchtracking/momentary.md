# NSSegmentedControl.SwitchTracking.momentary

**Framework**: AppKit  
**Kind**: case

A tracking mode that selects a segment when a person clicks within the bounds of the segment.

**Availability**:
- macOS ?+

## Declaration

```swift
case momentary
```

#### Discussion

A momentary segmented control sends an action when a person clicks a segment, and another action when the person releases the segment. If configured as continuous (see [`isContinuous`](nscontrol/iscontinuous.md)), the control also sends actions at repeating intervals until the person releases the segment, at which point the control sends its final action.

When the person clicks a segment, the [`selectedSegment`](nssegmentedcontrol/selectedsegment.md) value is the index of the active segment. When the person releases the segment, the [`selectedSegment`](nssegmentedcontrol/selectedsegment.md) value is `-1`.

This type of control is illustrated by the navigation segmented control in the Safari toolbar. When you click the back segment, for example, the previous webpage is displayed. This particular control is not configured as continuous. If it were, clicking and holding on the back segment would continue cycling through previous webpages until the segment is released.

## See Also

- [NSSegmentedControl.SwitchTracking.selectOne](nssegmentedcontrol/switchtracking/selectone.md)
  Only one segment in the control can be selected at a time.
- [NSSegmentedControl.SwitchTracking.selectAny](nssegmentedcontrol/switchtracking/selectany.md)
  One or more segment cells in the control can be selected at a time.
- [NSSegmentedControl.SwitchTracking.momentaryAccelerator](nssegmentedcontrol/switchtracking/momentaryaccelerator.md)
  A tracking mode that sends repeating actions as pressure changes on Force Touch systems, stopping when someone releases the segment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssegmentedcontrol/switchtracking/momentary)*
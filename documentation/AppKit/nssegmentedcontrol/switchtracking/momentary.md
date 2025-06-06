# NSSegmentedControl.SwitchTracking.momentary

**Framework**: AppKit  
**Kind**: case

A segment is selected only when the user is pressing the mouse down within the bounds of the segment. When the mouse is no longer down within the segment, the segment is automatically deselected. A momentary segmented control sends an action when the user clicks a segment, and another action when the user releases the segment. If configured as continuous (see [`isContinuous`](nscontrol/iscontinuous.md)), the control also sends actions at repeating intervals until the user releases the segment, at which point the control sends its final action.

**Availability**:
- macOS ?+

## Declaration

```swift
case momentary
```

#### Discussion

When the user clicks a segment, the [`selectedSegment`](nssegmentedcontrol/selectedsegment.md) value is the index of the active segment. When the user releases the segment, the [`selectedSegment`](nssegmentedcontrol/selectedsegment.md) value is `-1`.

This type of control is illustrated by the navigation segmented control in the Safari toolbar. When you click the back segment, for example, the previous webpage is displayed. This particular control is not configured as continuous. If it were, clicking and holding on the back segment would continue cycling through previous webpages until the segment is released.

## See Also

- [NSSegmentedControl.SwitchTracking.selectOne](nssegmentedcontrol/switchtracking/selectone.md)
  Only one segment in the control can be selected at a time.
- [NSSegmentedControl.SwitchTracking.selectAny](nssegmentedcontrol/switchtracking/selectany.md)
  One or more segment cells in the control can be selected at a time.
- [NSSegmentedControl.SwitchTracking.momentaryAccelerator](nssegmentedcontrol/switchtracking/momentaryaccelerator.md)
  On pressure-sensitive systems, when the user force clicks a segment, a momentary accelerator segmented control sends repeating actions as pressure changes occur. The control stops sending actions when the user releases pressure. A document-based app, for example, might implement a momentary accelerator segmented control in order to allow a user to adjust the speed of paging by using variable pressure. In this example, actions are sent to the app to indicate when pressure on the control has changed. The app then determines the amount of pressure currently applied, and adjusts navigation speed accordingly.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssegmentedcontrol/switchtracking/momentary)*
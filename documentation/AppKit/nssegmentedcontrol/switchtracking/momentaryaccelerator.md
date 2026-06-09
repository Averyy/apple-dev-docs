# NSSegmentedControl.SwitchTracking.momentaryAccelerator

**Framework**: AppKit  
**Kind**: case

A tracking mode that sends repeating actions as pressure changes on Force Touch systems, stopping when someone releases the segment.

**Availability**:
- macOS 10.10.3+

## Declaration

```swift
case momentaryAccelerator
```

#### Discussion

The control stops sending actions when the person releases pressure. A document-based app, for example, might implement a momentary accelerator segmented control in order to allow a person to adjust the speed of paging by using variable pressure. In this example, actions are sent to the app to indicate when pressure on the control has changed. The app then determines the amount of pressure currently applied, and adjusts navigation speed accordingly.

When the control is configured as continuous (see [`isContinuous`](nscontrol/iscontinuous.md)), the interval between repeating actions automatically adjusts to match the applied pressure. As the person presses harder, actions are sent more rapidly. As the person reduces pressure, actions slow down. As such, the person has direct control over how fast actions are sent. Continuous momentary accelerator segmented controls are intended for continuously advancing through a series of discrete objects, such as photos in an album or pages in a book.

When configured as noncontinuous, actions are sent whenever a change in pressure occurs. Noncontinuous momentary accelerator segmented controls are intended for adjusting the speed of navigation, such as playback speed in a media player, based on pressure. Once the control is released, a final action is sent.

When the person force clicks a segment in the control, [`selectedSegment`](nssegmentedcontrol/selectedsegment.md) value is the index of the active segment, and [`doubleValueForSelectedSegment`](nssegmentedcontrol/doublevalueforselectedsegment.md) is a measurement of pressure between `1.0` and approaching `2.0`. When the person releases pressure, the [`selectedSegment`](nssegmentedcontrol/selectedsegment.md) value is `-1` and [`doubleValueForSelectedSegment`](nssegmentedcontrol/doublevalueforselectedsegment.md) is `0.0`.

On a system that doesn’t support pressure sensitivity, a momentary accelerator segmented control behaves like a control of type [`NSSegmentedControl.SwitchTracking.momentary`](nssegmentedcontrol/switchtracking/momentary.md).

## See Also

- [NSSegmentedControl.SwitchTracking.selectOne](nssegmentedcontrol/switchtracking/selectone.md)
  Only one segment in the control can be selected at a time.
- [NSSegmentedControl.SwitchTracking.selectAny](nssegmentedcontrol/switchtracking/selectany.md)
  One or more segment cells in the control can be selected at a time.
- [NSSegmentedControl.SwitchTracking.momentary](nssegmentedcontrol/switchtracking/momentary.md)
  A tracking mode that selects a segment when a person clicks within the bounds of the segment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssegmentedcontrol/switchtracking/momentaryaccelerator)*
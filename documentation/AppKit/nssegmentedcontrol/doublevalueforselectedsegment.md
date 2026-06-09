# doubleValueForSelectedSegment

**Framework**: AppKit  
**Kind**: property

When the tracking mode for the control is set to use a momentary accelerator, returns a value for the selected segment.

**Availability**:
- macOS 10.10.3+

## Declaration

```swift
var doubleValueForSelectedSegment: Double { get }
```

#### Return Value

The value of the selected segment interpreted as a double-precision floating-point number.

#### Discussion

This method is intended for use with controls whose tracking mode is set to [`NSSegmentedControl.SwitchTracking.momentaryAccelerator`](nssegmentedcontrol/switchtracking/momentaryaccelerator.md). An assertion will occur if this method is called for other types of segmented controls.

## See Also

- [NSSegmentedControl.SwitchTracking.momentaryAccelerator](nssegmentedcontrol/switchtracking/momentaryaccelerator.md)
  A tracking mode that sends repeating actions as pressure changes on Force Touch systems, stopping when someone releases the segment.
- [var trackingMode: NSSegmentedControl.SwitchTracking](nssegmentedcontrol/trackingmode.md)
  The type of tracking behavior the control exhibits.
- [var selectedSegment: Int](nssegmentedcontrol/selectedsegment.md)
  The index of the selected segment of the control, or `-1` if no segment is selected.
- [var indexOfSelectedItem: Int](nssegmentedcontrol/indexofselecteditem.md)
- [func selectSegment(withTag: Int) -> Bool](nssegmentedcontrol/selectsegment(withtag:).md)
  Selects the segment with the specified tag.
- [func setSelected(Bool, forSegment: Int)](nssegmentedcontrol/setselected(_:forsegment:).md)
  Sets the selection state of the specified segment.
- [func isSelected(forSegment: Int) -> Bool](nssegmentedcontrol/isselected(forsegment:).md)
  Returns a Boolean value indicating whether the specified segment is selected.
- [var selectedSegmentBezelColor: NSColor?](nssegmentedcontrol/selectedsegmentbezelcolor.md)
  The color of the selected segment’s bezel, in appearances that support it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssegmentedcontrol/doublevalueforselectedsegment)*
# setSelected(_:forSegment:)

**Framework**: AppKit  
**Kind**: method

Sets the selection state of the specified segment.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func setSelected(_ selected: Bool, forSegment segment: Int)
```

#### Discussion

If the control allows only a single selection, this method deselects any other selected segments.

If the [`trackingMode`](nssegmentedcontrol/trackingmode.md) property of the segment is set to [`NSSegmentedControl.SwitchTracking.momentary`](nssegmentedcontrol/switchtracking/momentary.md), then attempting to set the selected state of the segment will have no effect.

## Parameters

- `selected`:   if you want to select the segment; otherwise,  .
- `segment`: The index of the segment whose selection state you want to set. This method raises an exception ( ) if the index is out of bounds.

## See Also

- [var selectedSegment: Int](nssegmentedcontrol/selectedsegment.md)
  The index of the selected segment of the control, or `-1` if no segment is selected.
- [var indexOfSelectedItem: Int](nssegmentedcontrol/indexofselecteditem.md)
- [func selectSegment(withTag: Int) -> Bool](nssegmentedcontrol/selectsegment(withtag:).md)
  Selects the segment with the specified tag.
- [func isSelected(forSegment: Int) -> Bool](nssegmentedcontrol/isselected(forsegment:).md)
  Returns a Boolean value indicating whether the specified segment is selected.
- [var selectedSegmentBezelColor: NSColor?](nssegmentedcontrol/selectedsegmentbezelcolor.md)
  The color of the selected segment’s bezel, in appearances that support it.
- [var doubleValueForSelectedSegment: Double](nssegmentedcontrol/doublevalueforselectedsegment.md)
  When the tracking mode for the control is set to use a momentary accelerator, returns a value for the selected segment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssegmentedcontrol/setselected(_:forsegment:))*
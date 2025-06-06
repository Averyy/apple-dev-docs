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

If the [`trackingMode`](nssegmentedcell/trackingmode.md) property of the segmented cell is set to [`NSSegmentedControl.SwitchTracking.momentary`](nssegmentedcontrol/switchtracking/momentary.md), then attempting to set the selected state of the segment will have no effect.

## Parameters

- `selected`:   if you want to select the segment; otherwise,  .
- `segment`: The index of the segment whose selection state you want to set. This method raises an exception ( ) if the index is out of bounds.

## See Also

- [func selectSegment(withTag: Int) -> Bool](nssegmentedcell/selectsegment(withtag:).md)
  Selects the segment with the specified tag.
- [func makeNextSegmentKey()](nssegmentedcell/makenextsegmentkey.md)
  Selects the next segment.
- [func makePreviousSegmentKey()](nssegmentedcell/makeprevioussegmentkey.md)
  Selects the previous segment.
- [var selectedSegment: Int](nssegmentedcell/selectedsegment.md)
  The index of the selected segment of the control, or `-1` if no segment is selected.
- [func isSelected(forSegment: Int) -> Bool](nssegmentedcell/isselected(forsegment:).md)
  Returns a Boolean value indicating whether the specified segment is selected,


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssegmentedcell/setselected(_:forsegment:))*
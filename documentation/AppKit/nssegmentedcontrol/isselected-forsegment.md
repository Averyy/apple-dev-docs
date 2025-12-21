# isSelected(forSegment:)

**Framework**: AppKit  
**Kind**: method

Returns a Boolean value indicating whether the specified segment is selected.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func isSelected(forSegment segment: Int) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) if the segment is selected; otherwise, [`false`](https://developer.apple.com/documentation/Swift/false).

## Parameters

- `segment`: The index of the segment whose selection state you want to get. This method raises an exception ( ) if the index is out of bounds.

## See Also

- [var selectedSegment: Int](nssegmentedcontrol/selectedsegment.md)
  The index of the selected segment of the control, or `-1` if no segment is selected.
- [var indexOfSelectedItem: Int](nssegmentedcontrol/indexofselecteditem.md)
- [func selectSegment(withTag: Int) -> Bool](nssegmentedcontrol/selectsegment(withtag:).md)
  Selects the segment with the specified tag.
- [func setSelected(Bool, forSegment: Int)](nssegmentedcontrol/setselected(_:forsegment:).md)
  Sets the selection state of the specified segment.
- [var selectedSegmentBezelColor: NSColor?](nssegmentedcontrol/selectedsegmentbezelcolor.md)
  The color of the selected segment’s bezel, in appearances that support it.
- [var doubleValueForSelectedSegment: Double](nssegmentedcontrol/doublevalueforselectedsegment.md)
  When the tracking mode for the control is set to use a momentary accelerator, returns a value for the selected segment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssegmentedcontrol/isselected(forsegment:))*
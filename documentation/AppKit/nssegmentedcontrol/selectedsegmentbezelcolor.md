# selectedSegmentBezelColor

**Framework**: AppKit  
**Kind**: property

The color of the selected segment’s bezel, in appearances that support it.

**Availability**:
- macOS 10.12.2+

## Declaration

```swift
@NSCopying
@MainActor var selectedSegmentBezelColor: NSColor? { get set }
```

## See Also

- [var selectedSegment: Int](nssegmentedcontrol/selectedsegment.md)
  The index of the selected segment of the control, or `-1` if no segment is selected.
- [var indexOfSelectedItem: Int](nssegmentedcontrol/indexofselecteditem.md)
- [func selectSegment(withTag: Int) -> Bool](nssegmentedcontrol/selectsegment(withtag:).md)
  Selects the segment with the specified tag.
- [func setSelected(Bool, forSegment: Int)](nssegmentedcontrol/setselected(_:forsegment:).md)
  Sets the selection state of the specified segment.
- [func isSelected(forSegment: Int) -> Bool](nssegmentedcontrol/isselected(forsegment:).md)
  Returns a Boolean value indicating whether the specified segment is selected.
- [var doubleValueForSelectedSegment: Double](nssegmentedcontrol/doublevalueforselectedsegment.md)
  When the tracking mode for the control is set to use a momentary accelerator, returns a value for the selected segment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssegmentedcontrol/selectedsegmentbezelcolor)*
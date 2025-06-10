# selectedSegment

**Framework**: AppKit  
**Kind**: property

The index of the selected segment of the control, or `-1` if no segment is selected.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var selectedSegment: Int { get set }
```

#### Discussion

If the control allows multiple selections, this property contains the most recently selected segment. If the index is out of bounds, an exception ([`rangeException`](https://developer.apple.com/documentation/Foundation/NSExceptionName/rangeException)) is raised.

## See Also

- [var indexOfSelectedItem: Int](nssegmentedcontrol/indexofselecteditem.md)
- [func selectSegment(withTag: Int) -> Bool](nssegmentedcontrol/selectsegment(withtag:).md)
  Selects the segment with the specified tag.
- [func setSelected(Bool, forSegment: Int)](nssegmentedcontrol/setselected(_:forsegment:).md)
  Sets the selection state of the specified segment.
- [func isSelected(forSegment: Int) -> Bool](nssegmentedcontrol/isselected(forsegment:).md)
  Returns a Boolean value indicating whether the specified segment is selected.
- [var selectedSegmentBezelColor: NSColor?](nssegmentedcontrol/selectedsegmentbezelcolor.md)
  The color of the selected segment’s bezel, in appearances that support it.
- [var doubleValueForSelectedSegment: Double](nssegmentedcontrol/doublevalueforselectedsegment.md)
  When the tracking mode for the control is set to use a momentary accelerator, returns a value for the selected segment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssegmentedcontrol/selectedsegment)*
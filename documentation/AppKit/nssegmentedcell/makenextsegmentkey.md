# makeNextSegmentKey()

**Framework**: AppKit  
**Kind**: method

Selects the next segment.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func makeNextSegmentKey()
```

#### Discussion

The next segment is the one to the right of the currently selected segment. For the last segment, the selection wraps back to the beginning of the control.

## See Also

- [func setSelected(Bool, forSegment: Int)](nssegmentedcell/setselected(_:forsegment:).md)
  Sets the selection state of the specified segment.
- [func selectSegment(withTag: Int) -> Bool](nssegmentedcell/selectsegment(withtag:).md)
  Selects the segment with the specified tag.
- [func makePreviousSegmentKey()](nssegmentedcell/makeprevioussegmentkey.md)
  Selects the previous segment.
- [var selectedSegment: Int](nssegmentedcell/selectedsegment.md)
  The index of the selected segment of the control, or `-1` if no segment is selected.
- [func isSelected(forSegment: Int) -> Bool](nssegmentedcell/isselected(forsegment:).md)
  Returns a Boolean value indicating whether the specified segment is selected,


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssegmentedcell/makenextsegmentkey())*
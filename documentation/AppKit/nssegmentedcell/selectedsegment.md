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

This property contains the zero-based index of the segment. If the control allows multiple selections, the value of this property is the index of the most recently selected segment.

If you specify an index that is out of bounds, an exception ([`rangeException`](https://developer.apple.com/documentation/foundation/nsexceptionname/1413262-rangeexception)) is raised.

## See Also

- [func setSelected(Bool, forSegment: Int)](nssegmentedcell/setselected(_:forsegment:).md)
  Sets the selection state of the specified segment.
- [func selectSegment(withTag: Int) -> Bool](nssegmentedcell/selectsegment(withtag:).md)
  Selects the segment with the specified tag.
- [func makeNextSegmentKey()](nssegmentedcell/makenextsegmentkey.md)
  Selects the next segment.
- [func makePreviousSegmentKey()](nssegmentedcell/makeprevioussegmentkey.md)
  Selects the previous segment.
- [func isSelected(forSegment: Int) -> Bool](nssegmentedcell/isselected(forsegment:).md)
  Returns a Boolean value indicating whether the specified segment is selected,


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssegmentedcell/selectedsegment)*
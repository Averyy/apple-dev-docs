# selectedSegment

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The index of the selected segment of the control, or `-1` if no segment is selected.

**Availability**:
- macOS

## Declaration

```swift
var selectedSegment: Int { get set }
```

```objc
@property NSInteger selectedSegment;
```

#### Discussion

This property contains the zero-based index of the segment. If the control allows multiple selections, the value of this property is the index of the most recently selected segment.

If you specify an index that is out of bounds, an exception ([`rangeException`](../../Foundation/nsexceptionname/rangeexception.md)) is raised.

## See Also

### Specifying the Selected Segment
- [func setSelected(Bool, forSegment: Int)](./setselected%28_,forsegment%29.md)
  Sets the selection state of the specified segment.
- [func selectSegment(withTag: Int) -> Bool](./selectsegment%28withtag%29.md)
  Selects the segment with the specified tag.
- [func makeNextSegmentKey()](./makenextsegmentkey%28%29.md)
  Selects the next segment.
- [func makePreviousSegmentKey()](./makeprevioussegmentkey%28%29.md)
  Selects the previous segment.
- [func isSelected(forSegment: Int) -> Bool](./isselected%28forsegment%29.md)
  Returns a Boolean value indicating whether the specified segment is selected,


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssegmentedcell/selectedsegment)*
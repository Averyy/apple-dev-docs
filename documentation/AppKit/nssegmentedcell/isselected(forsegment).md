# isSelected(forSegment:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns a Boolean value indicating whether the specified segment is selected,

**Availability**:
- macOS

## Declaration

```swift
func isSelected(forSegment segment: Int) -> Bool
```

```objc
- (BOOL) isSelectedForSegment:(NSInteger) segment;
```

#### Return Value

[`true`](../../Swift/true.md) if the segment is selected; otherwise, [`false`](../../Swift/false.md).

## Parameters

- `segment`: The index of the segment whose selection state you want to get. This method raises an exception ([`rangeException`](../../Foundation/nsexceptionname/rangeexception.md)) if the index is out of bounds.

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
- [var selectedSegment: Int](./selectedsegment.md)
  The index of the selected segment of the control, or `-1` if no segment is selected.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssegmentedcell/isselected(forsegment:))*
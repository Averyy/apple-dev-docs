# setSelected(_:forSegment:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Sets the selection state of the specified segment.

**Availability**:
- macOS

## Declaration

```swift
func setSelected(_ selected: Bool, forSegment segment: Int)
```

```objc
- (void) setSelected:(BOOL) selected forSegment:(NSInteger) segment;
```

#### Discussion

If the control allows only a single selection, this method deselects any other selected segments.

If the [`trackingMode`](./trackingmode.md) property of the segmented cell is set to [`NSSegmentedControl.SwitchTracking.momentary`](../nssegmentedcontrol/switchtracking/momentary.md), then attempting to set the selected state of the segment will have no effect.

## Parameters

- `selected`: [`true`](../../Swift/true.md) if you want to select the segment; otherwise, [`false`](../../Swift/false.md).
- `segment`: The index of the segment whose selection state you want to set. This method raises an exception ([`rangeException`](../../Foundation/nsexceptionname/rangeexception.md)) if the index is out of bounds.

## See Also

### Specifying the Selected Segment
- [func selectSegment(withTag: Int) -> Bool](./selectsegment%28withtag%29.md)
  Selects the segment with the specified tag.
- [func makeNextSegmentKey()](./makenextsegmentkey%28%29.md)
  Selects the next segment.
- [func makePreviousSegmentKey()](./makeprevioussegmentkey%28%29.md)
  Selects the previous segment.
- [var selectedSegment: Int](./selectedsegment.md)
  The index of the selected segment of the control, or `-1` if no segment is selected.
- [func isSelected(forSegment: Int) -> Bool](./isselected%28forsegment%29.md)
  Returns a Boolean value indicating whether the specified segment is selected,


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssegmentedcell/setselected(_:forsegment:))*
# makePreviousSegmentKey()

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Selects the previous segment.

**Availability**:
- macOS

## Declaration

```swift
func makePreviousSegmentKey()
```

```objc
- (void) makePreviousSegmentKey;
```

## Discussion

The previous segment is the one to the left of the currently selected segment. For the first segment, the selection wraps around to the last segment of the control.

## See Also

### Specifying the Selected Segment
- [func setSelected(Bool, forSegment: Int)](./setselected%28_,forsegment%29.md)
  Sets the selection state of the specified segment.
- [func selectSegment(withTag: Int) -> Bool](./selectsegment%28withtag%29.md)
  Selects the segment with the specified tag.
- [func makeNextSegmentKey()](./makenextsegmentkey%28%29.md)
  Selects the next segment.
- [var selectedSegment: Int](./selectedsegment.md)
  The index of the selected segment of the control, or `-1` if no segment is selected.
- [func isSelected(forSegment: Int) -> Bool](./isselected%28forsegment%29.md)
  Returns a Boolean value indicating whether the specified segment is selected,


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssegmentedcell/makeprevioussegmentkey())*
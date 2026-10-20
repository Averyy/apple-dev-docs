# makeNextSegmentKey()

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Selects the next segment.

**Availability**:
- macOS

## Declaration

```swift
func makeNextSegmentKey()
```

```objc
- (void) makeNextSegmentKey;
```

#### Discussion

The next segment is the one to the right of the currently selected segment. For the last segment, the selection wraps back to the beginning of the control.

## See Also

### Specifying the Selected Segment
- [func setSelected(Bool, forSegment: Int)](./setselected%28_,forsegment%29.md)
  Sets the selection state of the specified segment.
- [func selectSegment(withTag: Int) -> Bool](./selectsegment%28withtag%29.md)
  Selects the segment with the specified tag.
- [func makePreviousSegmentKey()](./makeprevioussegmentkey%28%29.md)
  Selects the previous segment.
- [var selectedSegment: Int](./selectedsegment.md)
  The index of the selected segment of the control, or `-1` if no segment is selected.
- [func isSelected(forSegment: Int) -> Bool](./isselected%28forsegment%29.md)
  Returns a Boolean value indicating whether the specified segment is selected,


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssegmentedcell/makenextsegmentkey())*
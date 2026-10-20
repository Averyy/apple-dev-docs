# selectSegment(withTag:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Selects the segment with the specified tag.

**Availability**:
- macOS

## Declaration

```swift
func selectSegment(withTag tag: Int) -> Bool
```

```objc
- (BOOL) selectSegmentWithTag:(NSInteger) tag;
```

#### Return Value

[`true`](../../Swift/true.md) if the segment was selected successfully; otherwise, [`false`](../../Swift/false.md).

#### Discussion

Typically, you use Interface Builder to specify the tag for each segment. You may also set this value programmatically using the [`setTag(_:forSegment:)`](./settag%28_,forsegment%29.md) method.

## Parameters

- `tag`: The tag associated with the desired segment.

## See Also

### Related Documentation
- [func setTag(Int, forSegment: Int)](./settag%28_,forsegment%29.md)
  Sets the tag for the specified segment.
### Specifying the Selected Segment
- [func setSelected(Bool, forSegment: Int)](./setselected%28_,forsegment%29.md)
  Sets the selection state of the specified segment.
- [func makeNextSegmentKey()](./makenextsegmentkey%28%29.md)
  Selects the next segment.
- [func makePreviousSegmentKey()](./makeprevioussegmentkey%28%29.md)
  Selects the previous segment.
- [var selectedSegment: Int](./selectedsegment.md)
  The index of the selected segment of the control, or `-1` if no segment is selected.
- [func isSelected(forSegment: Int) -> Bool](./isselected%28forsegment%29.md)
  Returns a Boolean value indicating whether the specified segment is selected,


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssegmentedcell/selectsegment(withtag:))*
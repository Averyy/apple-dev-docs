# selectSegment(withTag:)

**Framework**: AppKit  
**Kind**: method

Selects the segment with the specified tag.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func selectSegment(withTag tag: Int) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if the segment was selected successfully; otherwise, [`false`](https://developer.apple.com/documentation/swift/false).

#### Discussion

Typically, you use Interface Builder to specify the tag for each segment. You may also set this value programmatically using the [`setTag(_:forSegment:)`](nssegmentedcell/settag(_:forsegment:).md) method.

## Parameters

- `tag`: The tag associated with the desired segment.

## See Also

- [func setTag(Int, forSegment: Int)](nssegmentedcell/settag(_:forsegment:).md)
  Sets the tag for the specified segment.
- [func setSelected(Bool, forSegment: Int)](nssegmentedcell/setselected(_:forsegment:).md)
  Sets the selection state of the specified segment.
- [func makeNextSegmentKey()](nssegmentedcell/makenextsegmentkey.md)
  Selects the next segment.
- [func makePreviousSegmentKey()](nssegmentedcell/makeprevioussegmentkey.md)
  Selects the previous segment.
- [var selectedSegment: Int](nssegmentedcell/selectedsegment.md)
  The index of the selected segment of the control, or `-1` if no segment is selected.
- [func isSelected(forSegment: Int) -> Bool](nssegmentedcell/isselected(forsegment:).md)
  Returns a Boolean value indicating whether the specified segment is selected,


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssegmentedcell/selectsegment(withtag:))*
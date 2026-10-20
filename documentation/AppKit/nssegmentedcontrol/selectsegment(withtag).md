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

Typically, you use Interface Builder to specify the tag for each segment. You may also set this value programmatically using the `setTag:forSegment:` method of `NSSegmentedCell`.

## Parameters

- `tag`: The tag associated with the desired segment. A tag is an integer value that can be assigned to a segment as a way of identifying it without knowing its position in the control.

## See Also

### Related Documentation
- [func setTag(Int, forSegment: Int)](../nssegmentedcell/settag%28_,forsegment%29.md)
  Sets the tag for the specified segment.
### Managing the selected segment
- [var selectedSegment: Int](./selectedsegment.md)
  The index of the selected segment of the control, or `-1` if no segment is selected.
- [var indexOfSelectedItem: Int](./indexofselecteditem.md)
- [func setSelected(Bool, forSegment: Int)](./setselected%28_,forsegment%29.md)
  Sets the selection state of the specified segment.
- [func isSelected(forSegment: Int) -> Bool](./isselected%28forsegment%29.md)
  Returns a Boolean value indicating whether the specified segment is selected.
- [var selectedSegmentBezelColor: NSColor?](./selectedsegmentbezelcolor.md)
  The color of the selected segment’s bezel, in appearances that support it.
- [var doubleValueForSelectedSegment: Double](./doublevalueforselectedsegment.md)
  When the tracking mode for the control is set to use a momentary accelerator, returns a value for the selected segment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssegmentedcontrol/selectsegment(withtag:))*
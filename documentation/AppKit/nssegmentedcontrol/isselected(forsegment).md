# isSelected(forSegment:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns a Boolean value indicating whether the specified segment is selected.

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

### Managing the selected segment
- [var selectedSegment: Int](./selectedsegment.md)
  The index of the selected segment of the control, or `-1` if no segment is selected.
- [var indexOfSelectedItem: Int](./indexofselecteditem.md)
- [func selectSegment(withTag: Int) -> Bool](./selectsegment%28withtag%29.md)
  Selects the segment with the specified tag.
- [func setSelected(Bool, forSegment: Int)](./setselected%28_,forsegment%29.md)
  Sets the selection state of the specified segment.
- [var selectedSegmentBezelColor: NSColor?](./selectedsegmentbezelcolor.md)
  The color of the selected segment’s bezel, in appearances that support it.
- [var doubleValueForSelectedSegment: Double](./doublevalueforselectedsegment.md)
  When the tracking mode for the control is set to use a momentary accelerator, returns a value for the selected segment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssegmentedcontrol/isselected(forsegment:))*
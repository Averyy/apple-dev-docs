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

## Discussion

If the control allows only a single selection, this method deselects any other selected segments.

If the [`trackingMode`](./trackingmode.md) property of the segment is set to [`NSSegmentedControl.SwitchTracking.momentary`](./switchtracking/momentary.md), then attempting to set the selected state of the segment will have no effect.

## Parameters

- `selected`: [`true`](../../Swift/true.md) if you want to select the segment; otherwise, [`false`](../../Swift/false.md).
- `segment`: The index of the segment whose selection state you want to set. This method raises an exception ([`rangeException`](../../Foundation/nsexceptionname/rangeexception.md)) if the index is out of bounds.

## See Also

### Managing the selected segment
- [var selectedSegment: Int](./selectedsegment.md)
  The index of the selected segment of the control, or `-1` if no segment is selected.
- [var indexOfSelectedItem: Int](./indexofselecteditem.md)
- [func selectSegment(withTag: Int) -> Bool](./selectsegment%28withtag%29.md)
  Selects the segment with the specified tag.
- [func isSelected(forSegment: Int) -> Bool](./isselected%28forsegment%29.md)
  Returns a Boolean value indicating whether the specified segment is selected.
- [var selectedSegmentBezelColor: NSColor?](./selectedsegmentbezelcolor.md)
  The color of the selected segment’s bezel, in appearances that support it.
- [var doubleValueForSelectedSegment: Double](./doublevalueforselectedsegment.md)
  When the tracking mode for the control is set to use a momentary accelerator, returns a value for the selected segment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssegmentedcontrol/setselected(_:forsegment:))*
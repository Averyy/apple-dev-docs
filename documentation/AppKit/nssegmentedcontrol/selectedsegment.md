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

If the control allows multiple selections, this property contains the most recently selected segment. If the index is out of bounds, an exception ([`rangeException`](../../Foundation/nsexceptionname/rangeexception.md)) is raised.

## See Also

### Managing the selected segment
- [var indexOfSelectedItem: Int](./indexofselecteditem.md)
- [func selectSegment(withTag: Int) -> Bool](./selectsegment%28withtag%29.md)
  Selects the segment with the specified tag.
- [func setSelected(Bool, forSegment: Int)](./setselected%28_,forsegment%29.md)
  Sets the selection state of the specified segment.
- [func isSelected(forSegment: Int) -> Bool](./isselected%28forsegment%29.md)
  Returns a Boolean value indicating whether the specified segment is selected.
- [var selectedSegmentBezelColor: NSColor?](./selectedsegmentbezelcolor.md)
  The color of the selected segment’s bezel, in appearances that support it.
- [var doubleValueForSelectedSegment: Double](./doublevalueforselectedsegment.md)
  When the tracking mode for the control is set to use a momentary accelerator, returns a value for the selected segment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssegmentedcontrol/selectedsegment)*
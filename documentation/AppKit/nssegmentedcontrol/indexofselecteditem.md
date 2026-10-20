# indexOfSelectedItem

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

**Availability**:
- macOS 10.4+

## Declaration

```swift
var indexOfSelectedItem: Int { get }
```

```objc
@property (readonly) NSInteger indexOfSelectedItem;
```

## See Also

### Managing the selected segment
- [var selectedSegment: Int](./selectedsegment.md)
  The index of the selected segment of the control, or `-1` if no segment is selected.
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

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssegmentedcontrol/indexofselecteditem)*
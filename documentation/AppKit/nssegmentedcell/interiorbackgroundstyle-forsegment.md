# interiorBackgroundStyle(forSegment:)

**Framework**: AppKit  
**Kind**: method

Returns the interior background style for the specified segment.

**Availability**:
- macOS 10.5+

## Declaration

```swift
@MainActor
func interiorBackgroundStyle(forSegment segment: Int) -> NSView.BackgroundStyle
```

#### Return Value

The background style to use for specified segment. See [`NSView.BackgroundStyle`](nsview/backgroundstyle.md) for possible values.

#### Discussion

The interior background style describes the surface drawn onto in [`drawInterior(withFrame:in:)`](nscell/drawinterior(withframe:in:).md).

This is both an override point and a useful method to call. In a custom segment cell with a custom bezel, you can override this method to describe the surface on a per-segment basis.

## Parameters

- `segment`: The index of the segment whose background style you want to get. This method raises an exception ( ) if the index is out of bounds..

## See Also

- [var segmentStyle: NSSegmentedControl.Style](nssegmentedcell/segmentstyle.md)
  The visual style used to display the segmented control.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssegmentedcell/interiorbackgroundstyle(forsegment:))*
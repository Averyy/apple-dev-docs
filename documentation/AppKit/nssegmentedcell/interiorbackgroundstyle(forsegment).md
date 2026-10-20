# interiorBackgroundStyle(forSegment:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns the interior background style for the specified segment.

**Availability**:
- macOS 10.5+

## Declaration

```swift
func interiorBackgroundStyle(forSegment segment: Int) -> NSView.BackgroundStyle
```

```objc
- (NSBackgroundStyle) interiorBackgroundStyleForSegment:(NSInteger) segment;
```

#### Return Value

The background style to use for specified segment. See [`NSView.BackgroundStyle`](../nsview/backgroundstyle.md) for possible values.

#### Discussion

The interior background style describes the surface drawn onto in [`drawInterior(withFrame:in:)`](../nscell/drawinterior%28withframe,in%29.md).

This is both an override point and a useful method to call. In a custom segment cell with a custom bezel, you can override this method to describe the surface on a per-segment basis.

## Parameters

- `segment`: The index of the segment whose background style you want to get. This method raises an exception ([`rangeException`](../../Foundation/nsexceptionname/rangeexception.md)) if the index is out of bounds..

## See Also

### Specifying Segment Visual Styles
- [var segmentStyle: NSSegmentedControl.Style](./segmentstyle.md)
  The visual style used to display the segmented control.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssegmentedcell/interiorbackgroundstyle(forsegment:))*
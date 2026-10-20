# width(forSegment:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns the width of the specified segment.

**Availability**:
- macOS

## Declaration

```swift
func width(forSegment segment: Int) -> CGFloat
```

```objc
- (CGFloat) widthForSegment:(NSInteger) segment;
```

#### Return Value

The width of the segment, measured in points, or 0 if the segment is sized to fit the available space automatically.

## Parameters

- `segment`: The index of the segment whose width you want to get. This method raises an exception ([`rangeException`](../../Foundation/nsexceptionname/rangeexception.md)) if the index is out of bounds.

## See Also

### Adjusting the segment spacing
- [func setWidth(CGFloat, forSegment: Int)](./setwidth%28_,forsegment%29.md)
  Sets the width of the specified segment.
- [var segmentDistribution: NSSegmentedControl.Distribution](./segmentdistribution.md)
- [NSSegmentedControl.Distribution](./distribution.md)
- [var activeCompressionOptions: NSUserInterfaceCompressionOptions](./activecompressionoptions.md)
- [func compress(withPrioritizedCompressionOptions: [NSUserInterfaceCompressionOptions])](./compress%28withprioritizedcompressionoptions%29.md)
- [func minimumSize(withPrioritizedCompressionOptions: [NSUserInterfaceCompressionOptions]) -> NSSize](./minimumsize%28withprioritizedcompressionoptions%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssegmentedcontrol/width(forsegment:))*
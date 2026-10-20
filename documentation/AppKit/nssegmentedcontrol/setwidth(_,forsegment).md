# setWidth(_:forSegment:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Sets the width of the specified segment.

**Availability**:
- macOS

## Declaration

```swift
func setWidth(_ width: CGFloat, forSegment segment: Int)
```

```objc
- (void) setWidth:(CGFloat) width forSegment:(NSInteger) segment;
```

## Parameters

- `width`: The width of the segment, measured in points. Specify the value `0` if you want the segment to be sized to fit the available space automatically.
- `segment`: The index of the segment whose width you want to set. This method raises an exception ([`rangeException`](../../Foundation/nsexceptionname/rangeexception.md)) if the index is out of bounds.

## See Also

### Adjusting the segment spacing
- [func width(forSegment: Int) -> CGFloat](./width%28forsegment%29.md)
  Returns the width of the specified segment.
- [var segmentDistribution: NSSegmentedControl.Distribution](./segmentdistribution.md)
- [NSSegmentedControl.Distribution](./distribution.md)
- [var activeCompressionOptions: NSUserInterfaceCompressionOptions](./activecompressionoptions.md)
- [func compress(withPrioritizedCompressionOptions: [NSUserInterfaceCompressionOptions])](./compress%28withprioritizedcompressionoptions%29.md)
- [func minimumSize(withPrioritizedCompressionOptions: [NSUserInterfaceCompressionOptions]) -> NSSize](./minimumsize%28withprioritizedcompressionoptions%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssegmentedcontrol/setwidth(_:forsegment:))*
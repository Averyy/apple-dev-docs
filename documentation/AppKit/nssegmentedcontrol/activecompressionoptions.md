# activeCompressionOptions

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

**Availability**:
- macOS 10.13+

## Declaration

```swift
@NSCopying
var activeCompressionOptions: NSUserInterfaceCompressionOptions { get }
```

```objc
@property (copy, readonly) NSUserInterfaceCompressionOptions * activeCompressionOptions;
```

## See Also

### Adjusting the segment spacing
- [func setWidth(CGFloat, forSegment: Int)](./setwidth%28_,forsegment%29.md)
  Sets the width of the specified segment.
- [func width(forSegment: Int) -> CGFloat](./width%28forsegment%29.md)
  Returns the width of the specified segment.
- [var segmentDistribution: NSSegmentedControl.Distribution](./segmentdistribution.md)
- [NSSegmentedControl.Distribution](./distribution.md)
- [func compress(withPrioritizedCompressionOptions: [NSUserInterfaceCompressionOptions])](./compress%28withprioritizedcompressionoptions%29.md)
- [func minimumSize(withPrioritizedCompressionOptions: [NSUserInterfaceCompressionOptions]) -> NSSize](./minimumsize%28withprioritizedcompressionoptions%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssegmentedcontrol/activecompressionoptions)*
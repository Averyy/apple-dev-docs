# NSSegmentedControl.Distribution

**Framework**: AppKit  
**Kind**: enum  
**Role**: Enumeration

**Availability**:
- macOS 10.13+

## Declaration

```swift
enum Distribution
```

```c
enum NSSegmentDistribution : NSInteger;
```

## Topics

### Distribution Options
- [NSSegmentedControl.Distribution.fit](./distribution/fit.md)
  Dynamically sized segments will be sized to fit their contents, any remaining space will be left blank. This style is equivalent to the way segments were distributed on older systems.
- [NSSegmentedControl.Distribution.fill](./distribution/fill.md)
  Dynamically sized segments will be sized to fill the available space, with extra space being distributed equally among them. Default value.
- [NSSegmentedControl.Distribution.fillEqually](./distribution/fillequally.md)
  Dynamically sized segments will be sized to fill the available space, and kept the same size as each other.
- [NSSegmentedControl.Distribution.fillProportionally](./distribution/fillproportionally.md)
  Dynamically sized segments will be sized to fill the available space, and kept proportional to their fitting size.
### Initializers
- [init?(rawValue: Int)](./distribution/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Adjusting the segment spacing
- [func setWidth(CGFloat, forSegment: Int)](./setwidth%28_,forsegment%29.md)
  Sets the width of the specified segment.
- [func width(forSegment: Int) -> CGFloat](./width%28forsegment%29.md)
  Returns the width of the specified segment.
- [var segmentDistribution: NSSegmentedControl.Distribution](./segmentdistribution.md)
- [var activeCompressionOptions: NSUserInterfaceCompressionOptions](./activecompressionoptions.md)
- [func compress(withPrioritizedCompressionOptions: [NSUserInterfaceCompressionOptions])](./compress%28withprioritizedcompressionoptions%29.md)
- [func minimumSize(withPrioritizedCompressionOptions: [NSUserInterfaceCompressionOptions]) -> NSSize](./minimumsize%28withprioritizedcompressionoptions%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssegmentedcontrol/distribution)*
# NSSegmentedControl.Distribution

**Framework**: AppKit  
**Kind**: enum

**Availability**:
- macOS 10.13+

## Declaration

```swift
enum Distribution
```

## Topics

### Distribution Options
- [NSSegmentedControl.Distribution.fit](nssegmentedcontrol/distribution/fit.md)
  Dynamically sized segments will be sized to fit their contents, any remaining space will be left blank. This style is equivalent to the way segments were distributed on older systems.
- [NSSegmentedControl.Distribution.fill](nssegmentedcontrol/distribution/fill.md)
  Dynamically sized segments will be sized to fill the available space, with extra space being distributed equally among them. Default value.
- [NSSegmentedControl.Distribution.fillEqually](nssegmentedcontrol/distribution/fillequally.md)
  Dynamically sized segments will be sized to fill the available space, and kept the same size as each other.
- [NSSegmentedControl.Distribution.fillProportionally](nssegmentedcontrol/distribution/fillproportionally.md)
  Dynamically sized segments will be sized to fill the available space, and kept proportional to their fitting size.
### Initializers
- [init?(rawValue: Int)](nssegmentedcontrol/distribution/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../swift/bitwisecopyable.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [RawRepresentable](../swift/rawrepresentable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [func setWidth(CGFloat, forSegment: Int)](nssegmentedcontrol/setwidth(_:forsegment:).md)
  Sets the width of the specified segment.
- [func width(forSegment: Int) -> CGFloat](nssegmentedcontrol/width(forsegment:).md)
  Returns the width of the specified segment.
- [var segmentDistribution: NSSegmentedControl.Distribution](nssegmentedcontrol/segmentdistribution.md)
- [var activeCompressionOptions: NSUserInterfaceCompressionOptions](nssegmentedcontrol/activecompressionoptions.md)
- [func compress(withPrioritizedCompressionOptions: [NSUserInterfaceCompressionOptions])](nssegmentedcontrol/compress(withprioritizedcompressionoptions:).md)
- [func minimumSize(withPrioritizedCompressionOptions: [NSUserInterfaceCompressionOptions]) -> NSSize](nssegmentedcontrol/minimumsize(withprioritizedcompressionoptions:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssegmentedcontrol/distribution)*
# width(forSegment:)

**Framework**: AppKit  
**Kind**: method

Returns the width of the specified segment.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func width(forSegment segment: Int) -> CGFloat
```

#### Return Value

The width of the segment, measured in points, or 0 if the segment is sized to fit the available space automatically.

## Parameters

- `segment`: The index of the segment whose width you want to get. This method raises an exception ( ) if the index is out of bounds.

## See Also

- [func setWidth(CGFloat, forSegment: Int)](nssegmentedcontrol/setwidth(_:forsegment:).md)
  Sets the width of the specified segment.
- [var segmentDistribution: NSSegmentedControl.Distribution](nssegmentedcontrol/segmentdistribution.md)
- [NSSegmentedControl.Distribution](nssegmentedcontrol/distribution.md)
- [var activeCompressionOptions: NSUserInterfaceCompressionOptions](nssegmentedcontrol/activecompressionoptions.md)
- [func compress(withPrioritizedCompressionOptions: [NSUserInterfaceCompressionOptions])](nssegmentedcontrol/compress(withprioritizedcompressionoptions:).md)
- [func minimumSize(withPrioritizedCompressionOptions: [NSUserInterfaceCompressionOptions]) -> NSSize](nssegmentedcontrol/minimumsize(withprioritizedcompressionoptions:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssegmentedcontrol/width(forsegment:))*
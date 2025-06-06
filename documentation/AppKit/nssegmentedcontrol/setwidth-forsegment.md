# setWidth(_:forSegment:)

**Framework**: AppKit  
**Kind**: method

Sets the width of the specified segment.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func setWidth(_ width: CGFloat, forSegment segment: Int)
```

## Parameters

- `width`: The width of the segment, measured in points. Specify the value   if you want the segment to be sized to fit the available space automatically.
- `segment`: The index of the segment whose width you want to set. This method raises an exception ( ) if the index is out of bounds.

## See Also

- [func width(forSegment: Int) -> CGFloat](nssegmentedcontrol/width(forsegment:).md)
  Returns the width of the specified segment.
- [var segmentDistribution: NSSegmentedControl.Distribution](nssegmentedcontrol/segmentdistribution.md)
- [NSSegmentedControl.Distribution](nssegmentedcontrol/distribution.md)
- [var activeCompressionOptions: NSUserInterfaceCompressionOptions](nssegmentedcontrol/activecompressionoptions.md)
- [func compress(withPrioritizedCompressionOptions: [NSUserInterfaceCompressionOptions])](nssegmentedcontrol/compress(withprioritizedcompressionoptions:).md)
- [func minimumSize(withPrioritizedCompressionOptions: [NSUserInterfaceCompressionOptions]) -> NSSize](nssegmentedcontrol/minimumsize(withprioritizedcompressionoptions:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssegmentedcontrol/setwidth(_:forsegment:))*
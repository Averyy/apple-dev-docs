# rangeNotRequired

**Framework**: UIKit  
**Kind**: property  
**Role**: Type Property

Returns the value that causes the framework enumerate text segment rectangles, but avoids preparing a range object.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
static var rangeNotRequired: NSTextLayoutManager.SegmentOptions { get }
```

```c
NSTextLayoutManagerSegmentOptionsRangeNotRequired
```

## See Also

### Getting segment options
- [static var headSegmentExtended: NSTextLayoutManager.SegmentOptions](./headsegmentextended.md)
  Returns the value that causes the framework to extend the segment to the tail edge.
- [static var middleFragmentsExcluded: NSTextLayoutManager.SegmentOptions](./middlefragmentsexcluded.md)
  Returns the value that causes the framework to enumerate segments in only the first and last line fragments.
- [static var tailSegmentExtended: NSTextLayoutManager.SegmentOptions](./tailsegmentextended.md)
  Returns the value that causes the framework to extend the segment to the tail edge.
- [static var upstreamAffinity: NSTextLayoutManager.SegmentOptions](./upstreamaffinity.md)
  Returns the value that causes the framework to the place the segment based on the upstream affinity for an empty range.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nstextlayoutmanager/segmentoptions/rangenotrequired)*
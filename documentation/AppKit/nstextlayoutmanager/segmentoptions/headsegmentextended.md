# headSegmentExtended

**Framework**: AppKit  
**Kind**: property  
**Role**: Type Property

Returns the value that causes the framework to extend the segment to the tail edge.

**Availability**:
- macOS 12.0+

## Declaration

```swift
static var headSegmentExtended: NSTextLayoutManager.SegmentOptions { get }
```

```c
NSTextLayoutManagerSegmentOptionsHeadSegmentExtended
```

## See Also

### Getting segment options
- [static var middleFragmentsExcluded: NSTextLayoutManager.SegmentOptions](./middlefragmentsexcluded.md)
  Returns the value that causes the framework to enumerate segments in only the first and last line fragments.
- [static var rangeNotRequired: NSTextLayoutManager.SegmentOptions](./rangenotrequired.md)
  Returns the value that causes the framework enumerate text segment rectangles, but avoids preparing a range object.
- [static var tailSegmentExtended: NSTextLayoutManager.SegmentOptions](./tailsegmentextended.md)
  Returns the value that causes the framework to extend the segment to the tail edge.
- [static var upstreamAffinity: NSTextLayoutManager.SegmentOptions](./upstreamaffinity.md)
  Returns the value that causes the framework to the place the segment based on the upstream affinity for an empty range.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextlayoutmanager/segmentoptions/headsegmentextended)*
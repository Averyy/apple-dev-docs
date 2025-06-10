# middleFragmentsExcluded

**Framework**: AppKit  
**Kind**: property

Returns the value that causes the framework to enumerate segments in only the first and last line fragments.

**Availability**:
- macOS 12.0+

## Declaration

```swift
static var middleFragmentsExcluded: NSTextLayoutManager.SegmentOptions { get }
```

## See Also

- [static var headSegmentExtended: NSTextLayoutManager.SegmentOptions](nstextlayoutmanager/segmentoptions/headsegmentextended.md)
  Returns the value that causes the framework to extend the segment to the tail edge.
- [static var rangeNotRequired: NSTextLayoutManager.SegmentOptions](nstextlayoutmanager/segmentoptions/rangenotrequired.md)
  Returns the value that causes the framework enumerate text segment rectangles, but avoids preparing a range object.
- [static var tailSegmentExtended: NSTextLayoutManager.SegmentOptions](nstextlayoutmanager/segmentoptions/tailsegmentextended.md)
  Returns the value that causes the framework to extend the segment to the tail edge.
- [static var upstreamAffinity: NSTextLayoutManager.SegmentOptions](nstextlayoutmanager/segmentoptions/upstreamaffinity.md)
  Returns the value that causes the framework to the place the segment based on the upstream affinity for an empty range.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextlayoutmanager/segmentoptions/middlefragmentsexcluded)*
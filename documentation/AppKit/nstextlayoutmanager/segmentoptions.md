# NSTextLayoutManager.SegmentOptions

**Framework**: AppKit  
**Kind**: struct

Values that describe where and how the framework extends segments of a selection.

**Availability**:
- macOS 12.0+

## Declaration

```swift
struct SegmentOptions
```

## Topics

### Creating segment options
- [init(rawValue: UInt)](nstextlayoutmanager/segmentoptions/init(rawvalue:).md)
  Cceates a new segment option using the value you provide.
### Getting segment options
- [static var headSegmentExtended: NSTextLayoutManager.SegmentOptions](nstextlayoutmanager/segmentoptions/headsegmentextended.md)
  Returns the value that causes the framework to extend the segment to the tail edge.
- [static var middleFragmentsExcluded: NSTextLayoutManager.SegmentOptions](nstextlayoutmanager/segmentoptions/middlefragmentsexcluded.md)
  Returns the value that causes the framework to enumerate segments in only the first and last line fragments.
- [static var rangeNotRequired: NSTextLayoutManager.SegmentOptions](nstextlayoutmanager/segmentoptions/rangenotrequired.md)
  Returns the value that causes the framework enumerate text segment rectangles, but avoids preparing a range object.
- [static var tailSegmentExtended: NSTextLayoutManager.SegmentOptions](nstextlayoutmanager/segmentoptions/tailsegmentextended.md)
  Returns the value that causes the framework to extend the segment to the tail edge.
- [static var upstreamAffinity: NSTextLayoutManager.SegmentOptions](nstextlayoutmanager/segmentoptions/upstreamaffinity.md)
  Returns the value that causes the framework to the place the segment based on the upstream affinity for an empty range.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [OptionSet](../Swift/OptionSet.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [SetAlgebra](../Swift/SetAlgebra.md)

## See Also

- [var textViewportLayoutController: NSTextViewportLayoutController](nstextlayoutmanager/textviewportlayoutcontroller.md)
  Returns text viewport layout controller associated with the layout manager’s text container.
- [func invalidateLayout(for: NSTextRange)](nstextlayoutmanager/invalidatelayout(for:).md)
  Invalidates the layout information for specified text range.
- [func textLayoutFragment(for: any NSTextLocation) -> NSTextLayoutFragment?](nstextlayoutmanager/textlayoutfragment(for:)-68dez.md)
  Returns the text layout fragment from the document at the specified location.
- [func textLayoutFragment(for: CGPoint) -> NSTextLayoutFragment?](nstextlayoutmanager/textlayoutfragment(for:)-4dhrx.md)
  Returns the text layout fragment at the position you specify in the text container.
- [func ensureLayout(for: CGRect)](nstextlayoutmanager/ensurelayout(for:)-6ptsj.md)
  Performs the layout for filling the bounds you specify inside the last text container.
- [func ensureLayout(for: NSTextRange)](nstextlayoutmanager/ensurelayout(for:)-3duae.md)
  Performs the layout for specified text range.
- [func enumerateTextLayoutFragments(from: (any NSTextLocation)?, options: NSTextLayoutFragment.EnumerationOptions, using: (NSTextLayoutFragment) -> Bool) -> (any NSTextLocation)?](nstextlayoutmanager/enumeratetextlayoutfragments(from:options:using:).md)
  Enumerates the text layout fragments starting at the specified location.
- [NSTextLayoutManager.SegmentType](nstextlayoutmanager/segmenttype.md)
  Values that describe the rendering of selection boundaries.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextlayoutmanager/segmentoptions)*
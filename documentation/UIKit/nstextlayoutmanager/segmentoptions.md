# NSTextLayoutManager.SegmentOptions

**Framework**: UIKit  
**Kind**: struct  
**Role**: Structure

Values that describe where and how the framework extends segments of a selection.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
struct SegmentOptions
```

```c
enum NSTextLayoutManagerSegmentOptions : NSUInteger;
```

## Topics

### Creating segment options
- [init(rawValue: UInt)](./segmentoptions/init%28rawvalue%29.md)
  Cceates a new segment option using the value you provide.
### Getting segment options
- [static var headSegmentExtended: NSTextLayoutManager.SegmentOptions](./segmentoptions/headsegmentextended.md)
  Returns the value that causes the framework to extend the segment to the tail edge.
- [static var middleFragmentsExcluded: NSTextLayoutManager.SegmentOptions](./segmentoptions/middlefragmentsexcluded.md)
  Returns the value that causes the framework to enumerate segments in only the first and last line fragments.
- [static var rangeNotRequired: NSTextLayoutManager.SegmentOptions](./segmentoptions/rangenotrequired.md)
  Returns the value that causes the framework enumerate text segment rectangles, but avoids preparing a range object.
- [static var tailSegmentExtended: NSTextLayoutManager.SegmentOptions](./segmentoptions/tailsegmentextended.md)
  Returns the value that causes the framework to extend the segment to the tail edge.
- [static var upstreamAffinity: NSTextLayoutManager.SegmentOptions](./segmentoptions/upstreamaffinity.md)
  Returns the value that causes the framework to the place the segment based on the upstream affinity for an empty range.

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [ExpressibleByArrayLiteral](../../Swift/expressiblebyarrayliteral.md)
- [OptionSet](../../Swift/optionset.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)
- [SetAlgebra](../../Swift/setalgebra.md)

## See Also

### Causing layout generation
- [var textViewportLayoutController: NSTextViewportLayoutController](./textviewportlayoutcontroller.md)
  Returns text viewport layout controller associated with the layout manager’s text container.
- [func invalidateLayout(for: NSTextRange)](./invalidatelayout%28for%29.md)
  Invalidates the layout information for specified text range.
- [func textLayoutFragment(for: any NSTextLocation) -> NSTextLayoutFragment?](./textlayoutfragment%28for%29-68dez.md)
  Returns the text layout fragment from the document at the specified location.
- [func textLayoutFragment(for: CGPoint) -> NSTextLayoutFragment?](./textlayoutfragment%28for%29-4dhrx.md)
  Returns the text layout fragment at the position you specify in the text container.
- [func ensureLayout(for: CGRect)](./ensurelayout%28for%29-6ptsj.md)
  Performs the layout for filling the bounds you specify inside the last text container.
- [func ensureLayout(for: NSTextRange)](./ensurelayout%28for%29-3duae.md)
  Performs the layout for specified text range.
- [func enumerateTextLayoutFragments(from: (any NSTextLocation)?, options: NSTextLayoutFragment.EnumerationOptions, using: (NSTextLayoutFragment) -> Bool) -> (any NSTextLocation)?](./enumeratetextlayoutfragments%28from,options,using%29.md)
  Enumerates the text layout fragments starting at the specified location.
- [NSTextLayoutManager.SegmentType](./segmenttype.md)
  Values that describe the rendering of selection boundaries.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nstextlayoutmanager/segmentoptions)*
# NSTextLayoutManager.SegmentType

**Framework**: AppKit  
**Kind**: enum

Values that describe the rendering of selection boundaries.

**Availability**:
- macOS 12.0+

## Declaration

```swift
enum SegmentType
```

## Topics

### Kinds of text selection segments
- [NSTextLayoutManager.SegmentType.highlight](nstextlayoutmanager/segmenttype/highlight.md)
  The segment behavior suitable for highlighting.
- [NSTextLayoutManager.SegmentType.selection](nstextlayoutmanager/segmenttype/selection.md)
  The segment behavior suitable for selection rendering.
- [NSTextLayoutManager.SegmentType.standard](nstextlayoutmanager/segmenttype/standard.md)
  The standard segment, matching the typographic bounds of the range.
### Initializers
- [init?(rawValue: Int)](nstextlayoutmanager/segmenttype/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var textViewportLayoutController: NSTextViewportLayoutController](nstextlayoutmanager/textviewportlayoutcontroller.md)
  The text viewport layout controller associated with the layout manager’s text container.
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
- [NSTextLayoutManager.SegmentOptions](nstextlayoutmanager/segmentoptions.md)
  Values that describe where and how the framework extends segments of a selection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextlayoutmanager/segmenttype)*
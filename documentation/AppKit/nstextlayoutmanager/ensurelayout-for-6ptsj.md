# ensureLayout(for:)

**Framework**: AppKit  
**Kind**: method

Performs the layout for filling the bounds you specify inside the last text container.

**Availability**:
- macOS 12.0+

## Declaration

```swift
func ensureLayout(for bounds: CGRect)
```

## Parameters

- `bounds`: A   that describes the layout bounds.

## See Also

- [var textViewportLayoutController: NSTextViewportLayoutController](nstextlayoutmanager/textviewportlayoutcontroller.md)
  The text viewport layout controller associated with the layout manager’s text container.
- [func invalidateLayout(for: NSTextRange)](nstextlayoutmanager/invalidatelayout(for:).md)
  Invalidates the layout information for specified text range.
- [func textLayoutFragment(for: any NSTextLocation) -> NSTextLayoutFragment?](nstextlayoutmanager/textlayoutfragment(for:)-68dez.md)
  Returns the text layout fragment from the document at the specified location.
- [func textLayoutFragment(for: CGPoint) -> NSTextLayoutFragment?](nstextlayoutmanager/textlayoutfragment(for:)-4dhrx.md)
  Returns the text layout fragment at the position you specify in the text container.
- [func ensureLayout(for: NSTextRange)](nstextlayoutmanager/ensurelayout(for:)-3duae.md)
  Performs the layout for specified text range.
- [func enumerateTextLayoutFragments(from: (any NSTextLocation)?, options: NSTextLayoutFragment.EnumerationOptions, using: (NSTextLayoutFragment) -> Bool) -> (any NSTextLocation)?](nstextlayoutmanager/enumeratetextlayoutfragments(from:options:using:).md)
  Enumerates the text layout fragments starting at the specified location.
- [NSTextLayoutManager.SegmentType](nstextlayoutmanager/segmenttype.md)
  Values that describe the rendering of selection boundaries.
- [NSTextLayoutManager.SegmentOptions](nstextlayoutmanager/segmentoptions.md)
  Values that describe where and how the framework extends segments of a selection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextlayoutmanager/ensurelayout(for:)-6ptsj)*
# textLayoutFragment(for:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns the text layout fragment from the document at the specified location.

**Availability**:
- macOS 12.0+

## Declaration

```swift
func textLayoutFragment(for location: any NSTextLocation) -> NSTextLayoutFragment?
```

```objc
- (NSTextLayoutFragment *) textLayoutFragmentForLocation:(id<NSTextLocation>) location;
```

#### Return Value

An [`NSTextLayoutFragment`](../nstextlayoutfragment.md).

## Parameters

- `location`: The starting location.

## See Also

### Causing layout generation
- [var textViewportLayoutController: NSTextViewportLayoutController](./textviewportlayoutcontroller.md)
  The text viewport layout controller associated with the layout manager’s text container.
- [func invalidateLayout(for: NSTextRange)](./invalidatelayout%28for%29.md)
  Invalidates the layout information for specified text range.
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
- [NSTextLayoutManager.SegmentOptions](./segmentoptions.md)
  Values that describe where and how the framework extends segments of a selection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextlayoutmanager/textlayoutfragment(for:)-68dez)*
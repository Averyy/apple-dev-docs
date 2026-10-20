# ensureLayout(for:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Performs the layout for filling the bounds you specify inside the last text container.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
func ensureLayout(for bounds: CGRect)
```

```objc
- (void) ensureLayoutForBounds:(CGRect) bounds;
```

## Parameters

- `bounds`: A [`CGRect`](../../CoreFoundation/cgrect.md) that describes the layout bounds.

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
- [func ensureLayout(for: NSTextRange)](./ensurelayout%28for%29-3duae.md)
  Performs the layout for specified text range.
- [func enumerateTextLayoutFragments(from: (any NSTextLocation)?, options: NSTextLayoutFragment.EnumerationOptions, using: (NSTextLayoutFragment) -> Bool) -> (any NSTextLocation)?](./enumeratetextlayoutfragments%28from,options,using%29.md)
  Enumerates the text layout fragments starting at the specified location.
- [NSTextLayoutManager.SegmentType](./segmenttype.md)
  Values that describe the rendering of selection boundaries.
- [NSTextLayoutManager.SegmentOptions](./segmentoptions.md)
  Values that describe where and how the framework extends segments of a selection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nstextlayoutmanager/ensurelayout(for:)-6ptsj)*
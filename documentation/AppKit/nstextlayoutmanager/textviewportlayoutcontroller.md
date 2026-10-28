# textViewportLayoutController

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The text viewport layout controller associated with the layout manager’s text container.

**Availability**:
- macOS 12.0+

## Declaration

```swift
var textViewportLayoutController: NSTextViewportLayoutController { get }
```

```objc
@property (strong, readonly) NSTextViewportLayoutController * textViewportLayoutController;
```

## Discussion

The value of this property is `nil` if the text layout manager’s text container is `nil`. Set [`textContainer`](./textcontainer.md) before accessing this property.

## See Also

### Causing layout generation
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
- [NSTextLayoutManager.SegmentOptions](./segmentoptions.md)
  Values that describe where and how the framework extends segments of a selection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextlayoutmanager/textviewportlayoutcontroller)*
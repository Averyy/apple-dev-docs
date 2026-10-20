# shouldInvalidateLayoutForHighlightChange

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

Determines whether the scrubber should refresh its layout when an item is highlighted.

**Availability**:
- macOS 10.12.2+

## Declaration

```swift
var shouldInvalidateLayoutForHighlightChange: Bool { get }
```

```objc
@property (readonly) BOOL shouldInvalidateLayoutForHighlightChange;
```

#### Discussion

If [`true`](../../Swift/true.md), the scrubber invalidates its layout when an item is highlighted. Subclasses should return [`true`](../../Swift/true.md) if the highlight state affects the item layout.

The base implementation of this method returns [`false`](../../Swift/false.md).

## See Also

### Subclassing a scrubber layout
- [func prepare()](./prepare%28%29.md)
  Gives you an opportunity to perform layout calculations when the scrubber’s layout is invalidated.
- [var scrubberContentSize: NSSize](./scrubbercontentsize.md)
  The size required to contain all elements within the scrubber.
- [func layoutAttributesForItem(at: Int) -> NSScrubberLayoutAttributes?](./layoutattributesforitem%28at%29.md)
  The layout attributes for the item with the specified index.
- [func layoutAttributesForItems(in: NSRect) -> Set<NSScrubberLayoutAttributes>](./layoutattributesforitems%28in%29.md)
  The set of layout attributes for all items within the provided rectangle.
- [var shouldInvalidateLayoutForSelectionChange: Bool](./shouldinvalidatelayoutforselectionchange.md)
  Determines whether the scrubber should refresh its layout when the selection changes.
- [func shouldInvalidateLayoutForChange(fromVisibleRect: NSRect, toVisibleRect: NSRect) -> Bool](./shouldinvalidatelayoutforchange%28fromvisiblerect,tovisiblerect%29.md)
  Determines whether the scrubber should refresh its layout in response to a change of its visible region.
- [var automaticallyMirrorsInRightToLeftLayout: Bool](./automaticallymirrorsinrighttoleftlayout.md)
  Determines whether the scrubber mirrors its layout for right-to-left layouts.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsscrubberlayout/shouldinvalidatelayoutforhighlightchange)*
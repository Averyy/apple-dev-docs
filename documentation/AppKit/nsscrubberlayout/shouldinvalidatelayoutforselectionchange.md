# shouldInvalidateLayoutForSelectionChange

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

Determines whether the scrubber should refresh its layout when the selection changes.

**Availability**:
- macOS 10.12.2+

## Declaration

```swift
var shouldInvalidateLayoutForSelectionChange: Bool { get }
```

```objc
@property (readonly) BOOL shouldInvalidateLayoutForSelectionChange;
```

#### Discussion

If [`true`](../../Swift/true.md), the scrubber invalidates its layout when the selection changes. Subclasses should return [`true`](../../Swift/true.md) if the selection index affects the item layout.

The base implementation returns [`false`](../../Swift/false.md).

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
- [var shouldInvalidateLayoutForHighlightChange: Bool](./shouldinvalidatelayoutforhighlightchange.md)
  Determines whether the scrubber should refresh its layout when an item is highlighted.
- [func shouldInvalidateLayoutForChange(fromVisibleRect: NSRect, toVisibleRect: NSRect) -> Bool](./shouldinvalidatelayoutforchange%28fromvisiblerect,tovisiblerect%29.md)
  Determines whether the scrubber should refresh its layout in response to a change of its visible region.
- [var automaticallyMirrorsInRightToLeftLayout: Bool](./automaticallymirrorsinrighttoleftlayout.md)
  Determines whether the scrubber mirrors its layout for right-to-left layouts.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsscrubberlayout/shouldinvalidatelayoutforselectionchange)*
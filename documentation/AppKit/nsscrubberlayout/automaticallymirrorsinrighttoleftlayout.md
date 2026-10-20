# automaticallyMirrorsInRightToLeftLayout

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

Determines whether the scrubber mirrors its layout for right-to-left layouts.

**Availability**:
- macOS 10.12.2+

## Declaration

```swift
var automaticallyMirrorsInRightToLeftLayout: Bool { get }
```

```objc
@property (readonly) BOOL automaticallyMirrorsInRightToLeftLayout;
```

#### Discussion

If [`true`](../../Swift/true.md), the layout of a scrubber in a right-to-left interface is the mirror of the left-to-right version. If you wish to customize the behavior of the scrubber in right-to-left interfaces in a custom subclass, override this method to return [`false`](../../Swift/false.md).

The base implementation of this method returns [`true`](../../Swift/true.md).

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
- [var shouldInvalidateLayoutForHighlightChange: Bool](./shouldinvalidatelayoutforhighlightchange.md)
  Determines whether the scrubber should refresh its layout when an item is highlighted.
- [func shouldInvalidateLayoutForChange(fromVisibleRect: NSRect, toVisibleRect: NSRect) -> Bool](./shouldinvalidatelayoutforchange%28fromvisiblerect,tovisiblerect%29.md)
  Determines whether the scrubber should refresh its layout in response to a change of its visible region.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsscrubberlayout/automaticallymirrorsinrighttoleftlayout)*
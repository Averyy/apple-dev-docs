# shouldInvalidateLayoutForSelectionChange

**Framework**: AppKit  
**Kind**: property

Determines whether the scrubber should refresh its layout when the selection changes.

**Availability**:
- macOS 10.12.2+

## Declaration

```swift
@MainActor
var shouldInvalidateLayoutForSelectionChange: Bool { get }
```

#### Discussion

If [`true`](https://developer.apple.com/documentation/Swift/true), the scrubber invalidates its layout when the selection changes. Subclasses should return [`true`](https://developer.apple.com/documentation/Swift/true) if the selection index affects the item layout.

The base implementation returns [`false`](https://developer.apple.com/documentation/Swift/false).

## See Also

- [func prepare()](nsscrubberlayout/prepare.md)
  Gives you an opportunity to perform layout calculations when the scrubber’s layout is invalidated.
- [var scrubberContentSize: NSSize](nsscrubberlayout/scrubbercontentsize.md)
  The size required to contain all elements within the scrubber.
- [func layoutAttributesForItem(at: Int) -> NSScrubberLayoutAttributes?](nsscrubberlayout/layoutattributesforitem(at:).md)
  The layout attributes for the item with the specified index.
- [func layoutAttributesForItems(in: NSRect) -> Set<NSScrubberLayoutAttributes>](nsscrubberlayout/layoutattributesforitems(in:).md)
  The set of layout attributes for all items within the provided rectangle.
- [var shouldInvalidateLayoutForHighlightChange: Bool](nsscrubberlayout/shouldinvalidatelayoutforhighlightchange.md)
  Determines whether the scrubber should refresh its layout when an item is highlighted.
- [func shouldInvalidateLayoutForChange(fromVisibleRect: NSRect, toVisibleRect: NSRect) -> Bool](nsscrubberlayout/shouldinvalidatelayoutforchange(fromvisiblerect:tovisiblerect:).md)
  Determines whether the scrubber should refresh its layout in response to a change of its visible region.
- [var automaticallyMirrorsInRightToLeftLayout: Bool](nsscrubberlayout/automaticallymirrorsinrighttoleftlayout.md)
  Determines whether the scrubber mirrors its layout for right-to-left layouts.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsscrubberlayout/shouldinvalidatelayoutforselectionchange)*
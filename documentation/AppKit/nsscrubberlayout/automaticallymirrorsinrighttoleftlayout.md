# automaticallyMirrorsInRightToLeftLayout

**Framework**: AppKit  
**Kind**: property

Determines whether the scrubber mirrors its layout for right-to-left layouts.

**Availability**:
- macOS 10.12.2+

## Declaration

```swift
@MainActor
var automaticallyMirrorsInRightToLeftLayout: Bool { get }
```

#### Discussion

If [`true`](https://developer.apple.com/documentation/swift/true), the layout of a scrubber in a right-to-left interface is the mirror of the left-to-right version. If you wish to customize the behavior of the scrubber in right-to-left interfaces in a custom subclass, override this method to return [`false`](https://developer.apple.com/documentation/swift/false).

The base implementation of this method returns [`true`](https://developer.apple.com/documentation/swift/true).

## See Also

- [func prepare()](nsscrubberlayout/prepare.md)
  Gives you an opportunity to perform layout calculations when the scrubber’s layout is invalidated.
- [var scrubberContentSize: NSSize](nsscrubberlayout/scrubbercontentsize.md)
  The size required to contain all elements within the scrubber.
- [func layoutAttributesForItem(at: Int) -> NSScrubberLayoutAttributes?](nsscrubberlayout/layoutattributesforitem(at:).md)
  The layout attributes for the item with the specified index.
- [func layoutAttributesForItems(in: NSRect) -> Set<NSScrubberLayoutAttributes>](nsscrubberlayout/layoutattributesforitems(in:).md)
  The set of layout attributes for all items within the provided rectangle.
- [var shouldInvalidateLayoutForSelectionChange: Bool](nsscrubberlayout/shouldinvalidatelayoutforselectionchange.md)
  Determines whether the scrubber should refresh its layout when the selection changes.
- [var shouldInvalidateLayoutForHighlightChange: Bool](nsscrubberlayout/shouldinvalidatelayoutforhighlightchange.md)
  Determines whether the scrubber should refresh its layout when an item is highlighted.
- [func shouldInvalidateLayoutForChange(fromVisibleRect: NSRect, toVisibleRect: NSRect) -> Bool](nsscrubberlayout/shouldinvalidatelayoutforchange(fromvisiblerect:tovisiblerect:).md)
  Determines whether the scrubber should refresh its layout in response to a change of its visible region.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsscrubberlayout/automaticallymirrorsinrighttoleftlayout)*
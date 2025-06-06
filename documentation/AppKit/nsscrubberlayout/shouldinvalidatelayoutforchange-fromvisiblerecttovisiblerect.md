# shouldInvalidateLayoutForChange(fromVisibleRect:toVisibleRect:)

**Framework**: AppKit  
**Kind**: method

Determines whether the scrubber should refresh its layout in response to a change of its visible region.

**Availability**:
- macOS 10.12.2+

## Declaration

```swift
@MainActor
func shouldInvalidateLayoutForChange(fromVisibleRect: NSRect, toVisibleRect: NSRect) -> Bool
```

#### Discussion

If [`true`](https://developer.apple.com/documentation/swift/true), the scrubber invalidates its layout in response to a change of the visible region, in response to a user scroll action, or to the scrubber being resized. Subclasses that rely on the size or origin of the visible region should return [`true`](https://developer.apple.com/documentation/swift/true).

The base implementation of this method returns [`false`](https://developer.apple.com/documentation/swift/false).

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
- [var automaticallyMirrorsInRightToLeftLayout: Bool](nsscrubberlayout/automaticallymirrorsinrighttoleftlayout.md)
  Determines whether the scrubber mirrors its layout for right-to-left layouts.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsscrubberlayout/shouldinvalidatelayoutforchange(fromvisiblerect:tovisiblerect:))*
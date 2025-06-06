# prepare()

**Framework**: AppKit  
**Kind**: method

Gives you an opportunity to perform layout calculations when the scrubber’s layout is invalidated.

**Availability**:
- macOS 10.12.2+

## Declaration

```swift
@MainActor
func prepare()
```

#### Discussion

Use this method in subclasses to perform layout calculations and caching in advance of rendering the scrubber.

The system calls this method when the scrubber’s layout is invalidated.

The base implementation of this method does nothing.

## See Also

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
- [var automaticallyMirrorsInRightToLeftLayout: Bool](nsscrubberlayout/automaticallymirrorsinrighttoleftlayout.md)
  Determines whether the scrubber mirrors its layout for right-to-left layouts.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsscrubberlayout/prepare())*
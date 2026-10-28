# layoutAttributesForItem(at:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

The layout attributes for the item with the specified index.

**Availability**:
- macOS 10.12.2+

## Declaration

```swift
func layoutAttributesForItem(at index: Int) -> NSScrubberLayoutAttributes?
```

```objc
- (NSScrubberLayoutAttributes *) layoutAttributesForItemAtIndex:(NSInteger) index;
```

## Discussion

The base implementation returns `nil`.

## See Also

### Subclassing a scrubber layout
- [func prepare()](./prepare%28%29.md)
  Gives you an opportunity to perform layout calculations when the scrubber’s layout is invalidated.
- [var scrubberContentSize: NSSize](./scrubbercontentsize.md)
  The size required to contain all elements within the scrubber.
- [func layoutAttributesForItems(in: NSRect) -> Set<NSScrubberLayoutAttributes>](./layoutattributesforitems%28in%29.md)
  The set of layout attributes for all items within the provided rectangle.
- [var shouldInvalidateLayoutForSelectionChange: Bool](./shouldinvalidatelayoutforselectionchange.md)
  Determines whether the scrubber should refresh its layout when the selection changes.
- [var shouldInvalidateLayoutForHighlightChange: Bool](./shouldinvalidatelayoutforhighlightchange.md)
  Determines whether the scrubber should refresh its layout when an item is highlighted.
- [func shouldInvalidateLayoutForChange(fromVisibleRect: NSRect, toVisibleRect: NSRect) -> Bool](./shouldinvalidatelayoutforchange%28fromvisiblerect,tovisiblerect%29.md)
  Determines whether the scrubber should refresh its layout in response to a change of its visible region.
- [var automaticallyMirrorsInRightToLeftLayout: Bool](./automaticallymirrorsinrighttoleftlayout.md)
  Determines whether the scrubber mirrors its layout for right-to-left layouts.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsscrubberlayout/layoutattributesforitem(at:))*
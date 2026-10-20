# prepare()

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Gives you an opportunity to perform layout calculations when the scrubber’s layout is invalidated.

**Availability**:
- macOS 10.12.2+

## Declaration

```swift
func prepare()
```

```objc
- (void) prepareLayout;
```

#### Discussion

Use this method in subclasses to perform layout calculations and caching in advance of rendering the scrubber.

The system calls this method when the scrubber’s layout is invalidated.

The base implementation of this method does nothing.

## See Also

### Subclassing a scrubber layout
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
- [var automaticallyMirrorsInRightToLeftLayout: Bool](./automaticallymirrorsinrighttoleftlayout.md)
  Determines whether the scrubber mirrors its layout for right-to-left layouts.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsscrubberlayout/prepare())*
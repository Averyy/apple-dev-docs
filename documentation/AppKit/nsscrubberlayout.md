# NSScrubberLayout

**Framework**: AppKit  
**Kind**: class

An abstract class that describes the layout of items within a scrubber control.

**Availability**:
- macOS 10.12.2+

## Declaration

```swift
@MainActor
class NSScrubberLayout
```

#### Overview

To determine the layout of items in a scrubber, use one of the built-in subclasses ([`NSScrubberProportionalLayout`](nsscrubberproportionallayout.md) or [`NSScrubberFlowLayout`](nsscrubberflowlayout.md)), or create a custom subclass to implement your own layout.

## Topics

### Creating a scrubber layout
- [init()](nsscrubberlayout/init.md)
  Initializes and returns a newly allocated scrubber layout object from code.
- [init(coder: NSCoder)](nsscrubberlayout/init(coder:).md)
  Initializes and returns a newly allocated scrubber layout object from a storyboard or nib file.
### Configuring a scrubber layout
- [class var layoutAttributesClass: AnyClass](nsscrubberlayout/layoutattributesclass.md)
  A property containing a class that describes layout attributes.
- [var scrubber: NSScrubber?](nsscrubberlayout/scrubber.md)
  The scrubber control that this layout is assigned to.
- [var visibleRect: NSRect](nsscrubberlayout/visiblerect.md)
  The currently visible rectangle, in the coordinate space of the scrubber content.
- [func invalidateLayout()](nsscrubberlayout/invalidatelayout.md)
  Signals that the layout has been invalidated, and that the scrubber control should perform a new layout pass.
### Subclassing a scrubber layout
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
- [var automaticallyMirrorsInRightToLeftLayout: Bool](nsscrubberlayout/automaticallymirrorsinrighttoleftlayout.md)
  Determines whether the scrubber mirrors its layout for right-to-left layouts.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Inherited By
- [NSScrubberFlowLayout](nsscrubberflowlayout.md)
- [NSScrubberProportionalLayout](nsscrubberproportionallayout.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [class NSScrubberFlowLayout](nsscrubberflowlayout.md)
  A concrete layout object that arranges items end-to-end in a linear strip.
- [protocol NSScrubberFlowLayoutDelegate](nsscrubberflowlayoutdelegate.md)
  A protocol that a scrubber delegate can adopt to provide the size of an item.
- [class NSScrubberProportionalLayout](nsscrubberproportionallayout.md)
  A concrete layout object that sizes each item to some fraction of the scrubber’s visible size.
- [class NSScrubberLayoutAttributes](nsscrubberlayoutattributes.md)
  The layout of a scrubber item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsscrubberlayout)*
# NSScrubberFlowLayout

**Framework**: AppKit  
**Kind**: class  
**Role**: Class

A concrete layout object that arranges items end-to-end in a linear strip.

**Availability**:
- macOS 10.12.2+

## Declaration

```swift
class NSScrubberFlowLayout
```

```objc
@interface NSScrubberFlowLayout : NSScrubberLayout
```

#### Overview

To set the size of items on a per-item basis, ensure that your scrubber delegate conforms to the [`NSScrubberFlowLayoutDelegate`](./nsscrubberflowlayoutdelegate.md) protocol, and provides an implementation of the [`scrubber(_:layout:sizeForItemAt:)`](./nsscrubberflowlayoutdelegate/scrubber%28_,layout,sizeforitemat%29.md) method.

## Topics

### Configuring the layout
- [var itemSpacing: CGFloat](./nsscrubberflowlayout/itemspacing.md)
  The horizontal spacing between items, specified in points.
- [var itemSize: NSSize](./nsscrubberflowlayout/itemsize.md)
  The frame size for each item in the scrubber.
### Invalidating the layout
- [func invalidateLayoutForItems(at: IndexSet)](./nsscrubberflowlayout/invalidatelayoutforitems%28at%29.md)
  Informs the scrubber that it should perform a new layout pass for the items at the specified indexes.

## Relationships

### Inherits From
- [NSScrubberLayout](./nsscrubberlayout.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Scrubber layouts
- [protocol NSScrubberFlowLayoutDelegate](./nsscrubberflowlayoutdelegate.md)
  A protocol that a scrubber delegate can adopt to provide the size of an item.
- [class NSScrubberProportionalLayout](./nsscrubberproportionallayout.md)
  A concrete layout object that sizes each item to some fraction of the scrubber’s visible size.
- [class NSScrubberLayoutAttributes](./nsscrubberlayoutattributes.md)
  The layout of a scrubber item.
- [class NSScrubberLayout](./nsscrubberlayout.md)
  An abstract class that describes the layout of items within a scrubber control.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsscrubberflowlayout)*
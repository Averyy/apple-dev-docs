# NSScrubberFlowLayoutDelegate

**Framework**: AppKit  
**Kind**: protocol

A protocol that a scrubber delegate can adopt to provide the size of an item.

**Availability**:
- macOS ?+

## Declaration

```swift
protocol NSScrubberFlowLayoutDelegate : NSScrubberDelegate
```

#### Overview

This protocol conforms to the [`NSScrubberDelegate`](nsscrubberdelegate.md) protocol. Create an object that conforms to [`NSScrubberFlowLayoutDelegate`](nsscrubberflowlayoutdelegate.md) and assign it to the [`delegate`](nsscrubber/delegate.md) property of your scrubber object.

## Topics

### Controlling the item size
- [func scrubber(NSScrubber, layout: NSScrubberFlowLayout, sizeForItemAt: Int) -> NSSize](nsscrubberflowlayoutdelegate/scrubber(_:layout:sizeforitemat:).md)
  Asks the delegate for the size of each item in a scrubber whose items are arranged in a flow layout.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSScrubberDelegate](nsscrubberdelegate.md)

## See Also

- [class NSScrubberFlowLayout](nsscrubberflowlayout.md)
  A concrete layout object that arranges items end-to-end in a linear strip.
- [class NSScrubberProportionalLayout](nsscrubberproportionallayout.md)
  A concrete layout object that sizes each item to some fraction of the scrubber’s visible size.
- [class NSScrubberLayoutAttributes](nsscrubberlayoutattributes.md)
  The layout of a scrubber item.
- [class NSScrubberLayout](nsscrubberlayout.md)
  An abstract class that describes the layout of items within a scrubber control.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsscrubberflowlayoutdelegate)*
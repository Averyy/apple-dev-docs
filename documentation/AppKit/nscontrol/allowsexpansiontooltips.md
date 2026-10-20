# allowsExpansionToolTips

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether expansion tool tips are shown when the control is hovered over.

**Availability**:
- macOS 10.8+

## Declaration

```swift
var allowsExpansionToolTips: Bool { get set }
```

```objc
@property BOOL allowsExpansionToolTips;
```

#### Discussion

When the value of this property is [`true`](../../Swift/true.md), the expansion tool tip will expand; [`false`](../../Swift/false.md) means the tool tip won’t expand. The default value is [`false`](../../Swift/false.md).

Expansion tooltips are shown when the cell cannot show the full content and the user hovers the pointer over the control. This is controlled by the [`NSCell`](../nscell.md) class method [`expansionFrame(withFrame:in:)`](../nscell/expansionframe%28withframe,in%29.md) and is drawn by [`draw(withExpansionFrame:in:)`](../nscell/draw%28withexpansionframe,in%29.md). This value is encoded along with the control.

In general, it is recommended to turn this on for [`NSTextField`](../nstextfield.md) instances in a view-based [`NSTableView`](../nstableview.md).

## See Also

### Managing Expansion Tool Tips
- [func draw(withExpansionFrame: NSRect, in: NSView)](./draw%28withexpansionframe,in%29.md)
  Performs custom expansion tool tip drawing.
- [func expansionFrame(withFrame: NSRect) -> NSRect](./expansionframe%28withframe%29.md)
  The frame in which a tool tip can be displayed, if needed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscontrol/allowsexpansiontooltips)*
# allowsExpansionToolTips

**Framework**: AppKit  
**Kind**: property

A Boolean value that indicates whether expansion tool tips are shown when the control is hovered over.

**Availability**:
- macOS 10.8+

## Declaration

```swift
@MainActor
var allowsExpansionToolTips: Bool { get set }
```

#### Discussion

When the value of this property is [`true`](https://developer.apple.com/documentation/swift/true), the expansion tool tip will expand; [`false`](https://developer.apple.com/documentation/swift/false) means the tool tip won’t expand. The default value is [`false`](https://developer.apple.com/documentation/swift/false).

Expansion tooltips are shown when the cell cannot show the full content and the user hovers the pointer over the control. This is controlled by the [`NSCell`](nscell.md) class method [`expansionFrame(withFrame:in:)`](nscell/expansionframe(withframe:in:).md) and is drawn by [`draw(withExpansionFrame:in:)`](nscell/draw(withexpansionframe:in:).md). This value is encoded along with the control.

In general, it is recommended to turn this on for [`NSTextField`](nstextfield.md) instances in a view-based [`NSTableView`](nstableview.md).

## See Also

- [func draw(withExpansionFrame: NSRect, in: NSView)](nscontrol/draw(withexpansionframe:in:).md)
  Performs custom expansion tool tip drawing.
- [func expansionFrame(withFrame: NSRect) -> NSRect](nscontrol/expansionframe(withframe:).md)
  The frame in which a tool tip can be displayed, if needed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscontrol/allowsexpansiontooltips)*
# isHighlighted

**Framework**: AppKit  
**Kind**: property

A Boolean value indicating whether the cell has a highlighted appearance.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var isHighlighted: Bool { get set }
```

#### Discussion

When the value of this property is [`true`](https://developer.apple.com/documentation/swift/true), the cell draws itself with a highlighted appearance. The default value of this property is [`false`](https://developer.apple.com/documentation/swift/false).

Assigning a new value to this property has no effect by default. Subclasses can override the property to provide a highlighting behavior. For example, the [`NSButtonCell`](nsbuttoncell.md) class overrides this property, so that when the value is [`true`](https://developer.apple.com/documentation/swift/true) the button draws the button with a highlight appearance specified by [`NSCell.Attribute.cellLightsByBackground`](nscell/attribute/celllightsbybackground.md), [`NSCell.Attribute.cellLightsByContents`](nscell/attribute/celllightsbycontents.md), or [`NSCell.Attribute.cellLightsByGray`](nscell/attribute/celllightsbygray.md).

## See Also

- [func draw(withFrame: NSRect, in: NSView)](nscell/draw(withframe:in:).md)
  Draws the receiver’s border and then draws the interior of the cell.
- [func highlightColor(withFrame: NSRect, in: NSView) -> NSColor?](nscell/highlightcolor(withframe:in:).md)
  Returns the color the receiver uses when drawing the selection highlight.
- [func drawInterior(withFrame: NSRect, in: NSView)](nscell/drawinterior(withframe:in:).md)
  Draws the interior portion of the receiver, which includes the image or text portion but does not include the border.
- [var controlView: NSView?](nscell/controlview.md)
  The view associated with the cell.
- [func highlight(Bool, withFrame: NSRect, in: NSView)](nscell/highlight(_:withframe:in:).md)
  Redraws the receiver with the specified highlight setting.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscell/ishighlighted)*
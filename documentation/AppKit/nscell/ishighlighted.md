# isHighlighted

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value indicating whether the cell has a highlighted appearance.

**Availability**:
- macOS

## Declaration

```swift
var isHighlighted: Bool { get set }
```

```objc
@property (getter=isHighlighted) BOOL highlighted;
```

#### Discussion

When the value of this property is [`true`](../../Swift/true.md), the cell draws itself with a highlighted appearance. The default value of this property is [`false`](../../Swift/false.md).

Assigning a new value to this property has no effect by default. Subclasses can override the property to provide a highlighting behavior. For example, the [`NSButtonCell`](../nsbuttoncell.md) class overrides this property, so that when the value is [`true`](../../Swift/true.md) the button draws the button with a highlight appearance specified by [`NSCell.Attribute.cellLightsByBackground`](./attribute/celllightsbybackground.md), [`NSCell.Attribute.cellLightsByContents`](./attribute/celllightsbycontents.md), or [`NSCell.Attribute.cellLightsByGray`](./attribute/celllightsbygray.md).

## See Also

### Drawing and Highlighting
- [func draw(withFrame: NSRect, in: NSView)](./draw%28withframe,in%29.md)
  Draws the receiver’s border and then draws the interior of the cell.
- [func highlightColor(withFrame: NSRect, in: NSView) -> NSColor?](./highlightcolor%28withframe,in%29.md)
  Returns the color the receiver uses when drawing the selection highlight.
- [func drawInterior(withFrame: NSRect, in: NSView)](./drawinterior%28withframe,in%29.md)
  Draws the interior portion of the receiver, which includes the image or text portion but does not include the border.
- [var controlView: NSView?](./controlview.md)
  The view associated with the cell.
- [func highlight(Bool, withFrame: NSRect, in: NSView)](./highlight%28_,withframe,in%29.md)
  Redraws the receiver with the specified highlight setting.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscell/ishighlighted)*
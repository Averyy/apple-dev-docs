# NSTextBlock

**Framework**: AppKit  
**Kind**: class

A block of text laid out in a subregion of the text container.

**Availability**:
- macOS ?+

## Declaration

```swift
class NSTextBlock
```

#### Overview

A text block appears as an attribute of a paragraph, and as part of the paragraph style. The most important subclass of [`NSTextBlock`](nstextblock.md) is [`NSTextTableBlock`](nstexttableblock.md), which represents a block of text that appears as a cell in a table. The table itself is a [`NSTextTable`](nstexttable.md) object. All [`NSTextBlock`](nstextblock.md) objects reference this table, which controls their sizing and positioning.

## Topics

### Creating text blocks
- [init()](nstextblock/init.md)
  Initializes and returns an empty text block object.
### Working with dimensions of content
- [func setValue(CGFloat, type: NSTextBlock.ValueType, for: NSTextBlock.Dimension)](nstextblock/setvalue(_:type:for:).md)
  Sets a dimension of the text block.
- [func value(for: NSTextBlock.Dimension) -> CGFloat](nstextblock/value(for:).md)
  Returns the value of the specified text block dimension.
- [func valueType(for: NSTextBlock.Dimension) -> NSTextBlock.ValueType](nstextblock/valuetype(for:).md)
  Returns the value type of the specified text block dimension.
- [func setContentWidth(CGFloat, type: NSTextBlock.ValueType)](nstextblock/setcontentwidth(_:type:).md)
  Sets the width of the text block.
- [var contentWidth: CGFloat](nstextblock/contentwidth.md)
  The width of the text block.
- [var contentWidthValueType: NSTextBlock.ValueType](nstextblock/contentwidthvaluetype.md)
  The type of value stored for the text block width.
- [NSTextBlock.Dimension](nstextblock/dimension.md)
  The following constants specify values used by the methods [`setValue(_:type:for:)`](nstextblock/setvalue(_:type:for:).md), [`value(for:)`](nstextblock/value(for:).md), and [`valueType(for:)`](nstextblock/valuetype(for:).md) to specify text block dimensions.
- [NSTextBlock.ValueType](nstextblock/valuetype.md)
  The following constants specify values used by the methods [`setValue(_:type:for:)`](nstextblock/setvalue(_:type:for:).md) and [`valueType(for:)`](nstextblock/valuetype(for:).md) to specify text block value types.
### Getting and setting margins, borders, and padding
- [func setWidth(CGFloat, type: NSTextBlock.ValueType, for: NSTextBlock.Layer, edge: NSRectEdge)](nstextblock/setwidth(_:type:for:edge:).md)
  Sets the width of a specified edge of a specified layer of the text block.
- [func setWidth(CGFloat, type: NSTextBlock.ValueType, for: NSTextBlock.Layer)](nstextblock/setwidth(_:type:for:).md)
  Sets the width of all edges of a specified layer of the text block.
- [func width(for: NSTextBlock.Layer, edge: NSRectEdge) -> CGFloat](nstextblock/width(for:edge:).md)
  Returns the width of an edge of a specified layer of the text block.
- [func widthValueType(for: NSTextBlock.Layer, edge: NSRectEdge) -> NSTextBlock.ValueType](nstextblock/widthvaluetype(for:edge:).md)
  Returns the value type of an edge of a specified layer of the text block.
- [NSTextBlock.Layer](nstextblock/layer.md)
  The following constants specify values used by the properties and methods [`contentWidthValueType`](nstextblock/contentwidthvaluetype.md), [`setWidth(_:type:for:edge:)`](nstextblock/setwidth(_:type:for:edge:).md), [`setWidth(_:type:for:)`](nstextblock/setwidth(_:type:for:).md), [`width(for:edge:)`](nstextblock/width(for:edge:).md), and [`widthValueType(for:edge:)`](nstextblock/widthvaluetype(for:edge:).md) to specify text block layer values.
### Getting and setting alignment
- [var verticalAlignment: NSTextBlock.VerticalAlignment](nstextblock/verticalalignment-swift.property.md)
  The vertical alignment of the text block.
- [NSTextBlock.VerticalAlignment](nstextblock/verticalalignment-swift.enum.md)
  The following constants specify values used by the property [`verticalAlignment`](nstextblock/verticalalignment-swift.property.md) to specify vertical alignment.
### Working with color
- [var backgroundColor: NSColor?](nstextblock/backgroundcolor.md)
  The background color of the text block.
- [func setBorderColor(NSColor?, for: NSRectEdge)](nstextblock/setbordercolor(_:for:).md)
  Sets the border color of the specified edge of the text block.
- [func setBorderColor(NSColor?)](nstextblock/setbordercolor(_:).md)
  Sets the color of all borders of the text block.
- [func borderColor(for: NSRectEdge) -> NSColor?](nstextblock/bordercolor(for:).md)
  Returns the border color of the specified text block edge.
### Determining size and position of a text block
- [func rectForLayout(at: NSPoint, in: NSRect, textContainer: NSTextContainer, characterRange: NSRange) -> NSRect](nstextblock/rectforlayout(at:in:textcontainer:characterrange:).md)
  Returns the rectangle within which glyphs should be laid out for the specified arguments.
- [func boundsRect(forContentRect: NSRect, in: NSRect, textContainer: NSTextContainer, characterRange: NSRange) -> NSRect](nstextblock/boundsrect(forcontentrect:in:textcontainer:characterrange:).md)
  Returns the rectangle the text in the block actually occupies, including padding, borders, and margins.
### Drawing colors and decorations
- [func drawBackground(withFrame: NSRect, in: NSView, characterRange: NSRange, layoutManager: NSLayoutManager)](nstextblock/drawbackground(withframe:in:characterrange:layoutmanager:).md)
  Called by the layout manager to draw any colors and other decorations before the text is drawn.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Inherited By
- [NSTextTable](nstexttable.md)
- [NSTextTableBlock](nstexttableblock.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)

## See Also

- [class NSParagraphStyle](nsparagraphstyle.md)
  The paragraph or ruler attributes for an attributed string.
- [class NSMutableParagraphStyle](nsmutableparagraphstyle.md)
  An object for changing the values of the subattributes in a paragraph style attribute.
- [class NSTextTab](nstexttab.md)
  A tab in a paragraph.
- [class NSTextList](nstextlist.md)
  A section of text that forms a single list.
- [class NSTextTable](nstexttable.md)
  An object that represents a text table as a whole.
- [class NSTextTableBlock](nstexttableblock.md)
  A text block that appears as a cell in a text table.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextblock)*
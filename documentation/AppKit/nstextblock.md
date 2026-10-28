# NSTextBlock

**Framework**: AppKit  
**Kind**: class  
**Role**: Class

A block of text laid out in a subregion of the text container.

**Availability**:
- macOS 10.0+

## Declaration

```swift
class NSTextBlock
```

```objc
@interface NSTextBlock : NSObject
```

## Overview

A text block appears as an attribute of a paragraph, and as part of the paragraph style. The most important subclass of [`NSTextBlock`](./nstextblock.md) is [`NSTextTableBlock`](./nstexttableblock.md), which represents a block of text that appears as a cell in a table. The table itself is a [`NSTextTable`](./nstexttable.md) object. All [`NSTextBlock`](./nstextblock.md) objects reference this table, which controls their sizing and positioning.

## Topics

### Creating text blocks
- [init()](./nstextblock/init%28%29.md)
  Initializes and returns an empty text block object.
- [init?(coder: NSCoder)](./nstextblock/init%28coder%29.md)
### Working with dimensions of content
- [func setValue(CGFloat, type: NSTextBlock.ValueType, for: NSTextBlock.Dimension)](./nstextblock/setvalue%28_,type,for%29.md)
  Sets a dimension of the text block.
- [func value(for: NSTextBlock.Dimension) -> CGFloat](./nstextblock/value%28for%29.md)
  Returns the value of the specified text block dimension.
- [func valueType(for: NSTextBlock.Dimension) -> NSTextBlock.ValueType](./nstextblock/valuetype%28for%29.md)
  Returns the value type of the specified text block dimension.
- [func setContentWidth(CGFloat, type: NSTextBlock.ValueType)](./nstextblock/setcontentwidth%28_,type%29.md)
  Sets the width of the text block.
- [var contentWidth: CGFloat](./nstextblock/contentwidth.md)
  The width of the text block.
- [var contentWidthValueType: NSTextBlock.ValueType](./nstextblock/contentwidthvaluetype.md)
  The type of value stored for the text block width.
- [NSTextBlock.Dimension](./nstextblock/dimension.md)
  The following constants specify values used by the methods [`setValue(_:type:for:)`](./nstextblock/setvalue%28_,type,for%29.md), [`value(for:)`](./nstextblock/value%28for%29.md), and [`valueType(for:)`](./nstextblock/valuetype%28for%29.md) to specify text block dimensions.
- [NSTextBlock.ValueType](./nstextblock/valuetype.md)
  The following constants specify values used by the methods [`setValue(_:type:for:)`](./nstextblock/setvalue%28_,type,for%29.md) and [`valueType(for:)`](./nstextblock/valuetype%28for%29.md) to specify text block value types.
### Getting and setting margins, borders, and padding
- [func setWidth(CGFloat, type: NSTextBlock.ValueType, for: NSTextBlock.Layer)](./nstextblock/setwidth%28_,type,for%29.md)
  Sets the width of all edges of a specified layer of the text block.
- [func setWidth(CGFloat, type: NSTextBlock.ValueType, for: NSTextBlock.Layer, rectEdge: CGRectEdge)](./nstextblock/setwidth%28_,type,for,rectedge%29.md)
- [func width(for: NSTextBlock.Layer, rectEdge: CGRectEdge) -> CGFloat](./nstextblock/width%28for,rectedge%29.md)
- [func widthValueType(for: NSTextBlock.Layer, rectEdge: CGRectEdge) -> NSTextBlock.ValueType](./nstextblock/widthvaluetype%28for,rectedge%29.md)
- [NSTextBlock.Layer](./nstextblock/layer.md)
  The following constants specify values used by the properties and methods [`contentWidthValueType`](./nstextblock/contentwidthvaluetype.md), [`setWidth(_:type:for:edge:)`](./nstextblock/setwidth%28_,type,for,edge%29.md), [`setWidth(_:type:for:)`](./nstextblock/setwidth%28_,type,for%29.md), [`width(for:edge:)`](./nstextblock/width%28for,edge%29.md), and [`widthValueType(for:edge:)`](./nstextblock/widthvaluetype%28for,edge%29.md) to specify text block layer values.
### Getting and setting alignment
- [var verticalAlignment: NSTextBlock.VerticalAlignment](./nstextblock/verticalalignment-swift.property.md)
  The vertical alignment of the text block.
- [NSTextBlock.VerticalAlignment](./nstextblock/verticalalignment-swift.enum.md)
  The following constants specify values used by the property [`verticalAlignment`](./nstextblock/verticalalignment-swift.property.md) to specify vertical alignment.
### Working with color
- [var backgroundColor: NSColor?](./nstextblock/backgroundcolor.md)
  The background color of the text block.
- [func setBorderColor(NSColor?)](./nstextblock/setbordercolor%28_%29.md)
  Sets the color of all borders of the text block.
- [func setBorderColor(NSColor?, rectEdge: CGRectEdge)](./nstextblock/setbordercolor%28_,rectedge%29.md)
### Determining size and position of a text block
- [func rectForLayout(at: NSPoint, in: NSRect, textContainer: NSTextContainer, characterRange: NSRange) -> NSRect](./nstextblock/rectforlayout%28at,in,textcontainer,characterrange%29.md)
  Returns the rectangle within which glyphs should be laid out for the specified arguments.
- [func boundsRect(forContentRect: NSRect, in: NSRect, textContainer: NSTextContainer, characterRange: NSRange) -> NSRect](./nstextblock/boundsrect%28forcontentrect,in,textcontainer,characterrange%29.md)
  Returns the rectangle the text in the block actually occupies, including padding, borders, and margins.
### Drawing colors and decorations
- [func drawBackground(withFrame: NSRect, in: NSView?, characterRange: NSRange, layoutManager: NSLayoutManager)](./nstextblock/drawbackground%28withframe,in,characterrange,layoutmanager%29.md)
  Called by the layout manager to draw any colors and other decorations before the text is drawn.
### Deprecated
- [func setWidth(CGFloat, type: NSTextBlock.ValueType, for: NSTextBlock.Layer, edge: NSRectEdge)](./nstextblock/setwidth%28_,type,for,edge%29.md)
  Sets the width of a specified edge of a specified layer of the text block.
- [func width(for: NSTextBlock.Layer, edge: NSRectEdge) -> CGFloat](./nstextblock/width%28for,edge%29.md)
  Returns the width of an edge of a specified layer of the text block.
- [func widthValueType(for: NSTextBlock.Layer, edge: NSRectEdge) -> NSTextBlock.ValueType](./nstextblock/widthvaluetype%28for,edge%29.md)
  Returns the value type of an edge of a specified layer of the text block.
- [func borderColor(for: NSRectEdge) -> NSColor?](./nstextblock/bordercolor%28for%29-273pl.md)
- [func setBorderColor(NSColor?, for: NSRectEdge)](./nstextblock/setbordercolor%28_,for%29.md)
  Sets the border color of the specified edge of the text block.
- [func borderColor(for: CGRectEdge) -> NSColor?](./nstextblock/bordercolor%28for%29-5m8cr.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Inherited By
- [NSTextTable](./nstexttable.md)
- [NSTextTableBlock](./nstexttableblock.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)

## See Also

### Tables
- [class NSTextTable](./nstexttable.md)
  An object that represents a text table as a whole.
- [class NSTextTableBlock](./nstexttableblock.md)
  A text block that appears as a cell in a text table.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextblock)*
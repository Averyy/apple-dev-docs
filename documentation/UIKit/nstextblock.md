# NSTextBlock

**Framework**: UIKit  
**Kind**: class

An object that defines the size, spacing, and appearance of a block of text in an attributed string.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class NSTextBlock
```

## Mentions

- [Adding tables to attributed strings in UIKit](adding-tables-to-attributed-strings.md)

#### Overview

A text block lets you control how a paragraph looks and where it sits — you can configure its content dimensions, margin, border, padding, and colors.

You create a text block, configure its properties, then assign it to a paragraph by setting the [`textBlocks`](nsparagraphstyle/textblocks.md) property on an [`NSMutableParagraphStyle`](nsmutableparagraphstyle.md) and applying that style to a range in an `NSMutableAttributedString`. To represent a cell inside a table, use [`NSTextTableBlock`](nstexttableblock.md) instead.

##### Understand Content Dimensions

Each text block has three layers around its content: padding, border, and margin. You can configure the width of each layer per edge using [`setWidth(_:type:for:rectEdge:)`](nstextblock/setwidth(_:type:for:rectedge:).md), or set all edges at once using [`setWidth(_:type:for:)`](nstextblock/setwidth(_:type:for:).md). Use [`NSTextBlock.Dimension`](nstextblock/dimension.md) to set the content area’s width, height, and minimum or maximum constraints. Use [`NSTextBlock.ValueType`](nstextblock/valuetype.md) to specify whether a dimension is an absolute point value or a percentage.

##### Configure Visual Appearance

Set a background color using [`backgroundColor`](nstextblock/backgroundcolor.md). Configure border colors per edge using `setBorderColor(_:for:)`, or apply a single color to all four edges at once using [`setBorderColor(_:)`](nstextblock/setbordercolor(_:).md).

## Topics

### Initializing a text block
- [init()](nstextblock/init.md)
- [init?(coder: NSCoder)](nstextblock/init(coder:).md)
### Setting content dimensions
- [func setValue(CGFloat, type: NSTextBlock.ValueType, for: NSTextBlock.Dimension)](nstextblock/setvalue(_:type:for:).md)
- [func value(for: NSTextBlock.Dimension) -> CGFloat](nstextblock/value(for:).md)
- [func valueType(for: NSTextBlock.Dimension) -> NSTextBlock.ValueType](nstextblock/valuetype(for:).md)
- [func setContentWidth(CGFloat, type: NSTextBlock.ValueType)](nstextblock/setcontentwidth(_:type:).md)
- [var contentWidth: CGFloat](nstextblock/contentwidth.md)
- [var contentWidthValueType: NSTextBlock.ValueType](nstextblock/contentwidthvaluetype.md)
### Setting layer widths
- [func setWidth(CGFloat, type: NSTextBlock.ValueType, for: NSTextBlock.Layer)](nstextblock/setwidth(_:type:for:).md)
- [func setWidth(CGFloat, type: NSTextBlock.ValueType, for: NSTextBlock.Layer, rectEdge: CGRectEdge)](nstextblock/setwidth(_:type:for:rectedge:).md)
- [func width(for: NSTextBlock.Layer, rectEdge: CGRectEdge) -> CGFloat](nstextblock/width(for:rectedge:).md)
- [func widthValueType(for: NSTextBlock.Layer, rectEdge: CGRectEdge) -> NSTextBlock.ValueType](nstextblock/widthvaluetype(for:rectedge:).md)
### Configuring appearance
- [var verticalAlignment: NSTextBlock.VerticalAlignment](nstextblock/verticalalignment-swift.property.md)
- [var backgroundColor: UIColor?](nstextblock/backgroundcolor.md)
- [func setBorderColor(UIColor?)](nstextblock/setbordercolor(_:).md)
- [func setBorderColor(UIColor?, rectEdge: CGRectEdge)](nstextblock/setbordercolor(_:rectedge:).md)
- [func borderColor(for: CGRectEdge) -> UIColor?](nstextblock/bordercolor(for:).md)
### Supporting types
- [NSTextBlock.ValueType](nstextblock/valuetype.md)
- [NSTextBlock.Dimension](nstextblock/dimension.md)
- [NSTextBlock.Layer](nstextblock/layer.md)
- [NSTextBlock.VerticalAlignment](nstextblock/verticalalignment-swift.enum.md)

## Relationships

### Inherits From
- [NSObject](../objectivec/nsobject-swift.class.md)
### Inherited By
- [NSTextTable](nstexttable.md)
- [NSTextTableBlock](nstexttableblock.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSCoding](../foundation/nscoding.md)
- [NSCopying](../foundation/nscopying.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)
- [NSSecureCoding](../foundation/nssecurecoding.md)

## See Also

- [Adding tables to attributed strings in UIKit](adding-tables-to-attributed-strings.md)
  Create and configure tables in attributed strings and display them in a text view.
- [class NSTextTable](nstexttable.md)
  An object that represents a table of rows and columns in an attributed string.
- [class NSTextTableBlock](nstexttableblock.md)
  A text block that represents a single cell in a text table.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nstextblock)*
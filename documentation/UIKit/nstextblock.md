# NSTextBlock

**Framework**: UIKit  
**Kind**: class  
**Role**: Class

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

```objc
@interface NSTextBlock : NSObject
```

## Mentions

- [Adding tables to attributed strings in UIKit](./adding-tables-to-attributed-strings.md)

#### Overview

A text block lets you control how a paragraph looks and where it sits — you can configure its content dimensions, margin, border, padding, and colors.

You create a text block, configure its properties, then assign it to a paragraph by setting the [`textBlocks`](./nsparagraphstyle/textblocks.md) property on an [`NSMutableParagraphStyle`](./nsmutableparagraphstyle.md) and applying that style to a range in an `NSMutableAttributedString`. To represent a cell inside a table, use [`NSTextTableBlock`](./nstexttableblock.md) instead.

##### Understand content dimensions

Each text block has three layers around its content: padding, border, and margin. You can configure the width of each layer per edge using [`setWidth(_:type:for:rectEdge:)`](./nstextblock/setwidth%28_,type,for,rectedge%29.md), or set all edges at once using [`setWidth(_:type:for:)`](./nstextblock/setwidth%28_,type,for%29.md). Use [`NSTextBlock.Dimension`](./nstextblock/dimension.md) to set the content area’s width, height, and minimum or maximum constraints. Use [`NSTextBlock.ValueType`](./nstextblock/valuetype.md) to specify whether a dimension is an absolute point value or a percentage.

##### Configure visual appearance

Set a background color using [`backgroundColor`](./nstextblock/backgroundcolor.md). Configure border colors per edge using `setBorderColor(_:for:)`, or apply a single color to all four edges at once using [`setBorderColor(_:)`](./nstextblock/setbordercolor%28_%29.md).

## Topics

### Initializing a text block
- [init()](./nstextblock/init%28%29.md)
- [init?(coder: NSCoder)](./nstextblock/init%28coder%29.md)
### Setting content dimensions
- [func setValue(CGFloat, type: NSTextBlock.ValueType, for: NSTextBlock.Dimension)](./nstextblock/setvalue%28_,type,for%29.md)
- [func value(for: NSTextBlock.Dimension) -> CGFloat](./nstextblock/value%28for%29.md)
- [func valueType(for: NSTextBlock.Dimension) -> NSTextBlock.ValueType](./nstextblock/valuetype%28for%29.md)
- [func setContentWidth(CGFloat, type: NSTextBlock.ValueType)](./nstextblock/setcontentwidth%28_,type%29.md)
- [var contentWidth: CGFloat](./nstextblock/contentwidth.md)
- [var contentWidthValueType: NSTextBlock.ValueType](./nstextblock/contentwidthvaluetype.md)
### Setting layer widths
- [func setWidth(CGFloat, type: NSTextBlock.ValueType, for: NSTextBlock.Layer)](./nstextblock/setwidth%28_,type,for%29.md)
- [func setWidth(CGFloat, type: NSTextBlock.ValueType, for: NSTextBlock.Layer, rectEdge: CGRectEdge)](./nstextblock/setwidth%28_,type,for,rectedge%29.md)
- [func width(for: NSTextBlock.Layer, rectEdge: CGRectEdge) -> CGFloat](./nstextblock/width%28for,rectedge%29.md)
- [func widthValueType(for: NSTextBlock.Layer, rectEdge: CGRectEdge) -> NSTextBlock.ValueType](./nstextblock/widthvaluetype%28for,rectedge%29.md)
### Configuring appearance
- [var verticalAlignment: NSTextBlock.VerticalAlignment](./nstextblock/verticalalignment-swift.property.md)
- [var backgroundColor: UIColor?](./nstextblock/backgroundcolor.md)
- [func setBorderColor(UIColor?)](./nstextblock/setbordercolor%28_%29.md)
- [func setBorderColor(UIColor?, rectEdge: CGRectEdge)](./nstextblock/setbordercolor%28_,rectedge%29.md)
- [func borderColor(for: CGRectEdge) -> UIColor?](./nstextblock/bordercolor%28for%29.md)
### Supporting types
- [NSTextBlock.ValueType](./nstextblock/valuetype.md)
- [NSTextBlock.Dimension](./nstextblock/dimension.md)
- [NSTextBlock.Layer](./nstextblock/layer.md)
- [NSTextBlock.VerticalAlignment](./nstextblock/verticalalignment-swift.enum.md)

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
- [Adding tables to attributed strings in UIKit](./adding-tables-to-attributed-strings.md)
  Create and configure tables in attributed strings and display them in a text view.
- [class NSTextTable](./nstexttable.md)
  An object that represents a table of rows and columns in an attributed string.
- [class NSTextTableBlock](./nstexttableblock.md)
  A text block that represents a single cell in a text table.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nstextblock)*
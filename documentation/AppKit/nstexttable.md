# NSTextTable

**Framework**: AppKit  
**Kind**: class  
**Role**: Class

An object that represents a text table as a whole.

**Availability**:
- macOS 10.0+

## Declaration

```swift
class NSTextTable
```

```objc
@interface NSTextTable : NSTextBlock
```

## Overview

A text table is responsible for laying out and drawing the text table blocks it contains, and it maintains the basic parameters of the table.

## Topics

### Getting and setting number of columns
- [var numberOfColumns: Int](./nstexttable/numberofcolumns.md)
  The number of columns in the text table.
### Getting and setting layout algorithm
- [var layoutAlgorithm: NSTextTable.LayoutAlgorithm](./nstexttable/layoutalgorithm-swift.property.md)
  The text table layout algorithm.
### Collapsing borders
- [var collapsesBorders: Bool](./nstexttable/collapsesborders.md)
  A Boolean value indicating whether the text table borders are collapsible.
### Hiding empty cells
- [var hidesEmptyCells: Bool](./nstexttable/hidesemptycells.md)
  A Boolean value indicating whether the text table hides empty cells.
### Determining layout rectangles
- [func rect(for: NSTextTableBlock, layoutAt: NSPoint, in: NSRect, textContainer: NSTextContainer, characterRange: NSRange) -> NSRect](./nstexttable/rect%28for,layoutat,in,textcontainer,characterrange%29.md)
  Returns the rectangle within which glyphs should be laid out for a text table block.
- [func boundsRect(for: NSTextTableBlock, contentRect: NSRect, in: NSRect, textContainer: NSTextContainer, characterRange: NSRange) -> NSRect](./nstexttable/boundsrect%28for,contentrect,in,textcontainer,characterrange%29.md)
  Returns the rectangle the text table block actually occupies, including padding, borders, and margins.
### Drawing the table
- [func drawBackground(for: NSTextTableBlock, withFrame: NSRect, in: NSView, characterRange: NSRange, layoutManager: NSLayoutManager)](./nstexttable/drawbackground%28for,withframe,in,characterrange,layoutmanager%29.md)
  Draws any colors and other decorations for a text table block.
### Constants
- [NSTextTable.LayoutAlgorithm](./nstexttable/layoutalgorithm-swift.enum.md)
  These constants, specifying the type of text table layout algorithm, are used with [`layoutAlgorithm`](./nstexttable/layoutalgorithm-swift.property.md).

## Relationships

### Inherits From
- [NSTextBlock](./nstextblock.md)
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
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Tables
- [class NSTextTableBlock](./nstexttableblock.md)
  A text block that appears as a cell in a text table.
- [class NSTextBlock](./nstextblock.md)
  A block of text laid out in a subregion of the text container.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstexttable)*
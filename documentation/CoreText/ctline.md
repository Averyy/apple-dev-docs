# CTLine

**Framework**: Core Text  
**Kind**: class  
**Role**: Class

A line of text.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```swift
class CTLine
```

```c
typedef const struct __CTLine * CTLineRef;
```

## Overview

A `CTLine` object contains an array of glyph runs. Line objects are created by the typesetter during a framesetting operation and can draw themselves directly into a graphics context.

## Topics

### Creating Lines
- [func CTLineCreateWithAttributedString(CFAttributedString) -> CTLine](./ctlinecreatewithattributedstring%28_%29.md)
  Creates a single immutable line object from an attributed string.
- [func CTLineCreateTruncatedLine(CTLine, Double, CTLineTruncationType, CTLine?) -> CTLine?](./ctlinecreatetruncatedline%28_,_,_,_%29.md)
  Creates a truncated line from an existing line.
- [func CTLineCreateJustifiedLine(CTLine, CGFloat, Double) -> CTLine?](./ctlinecreatejustifiedline%28_,_,_%29.md)
  Creates a justified line from an existing line.
### Drawing the Line
- [func CTLineDraw(CTLine, CGContext)](./ctlinedraw%28_,_%29.md)
  Draws a complete line.
### Getting Line Data
- [func CTLineGetGlyphCount(CTLine) -> CFIndex](./ctlinegetglyphcount%28_%29.md)
  Returns the total glyph count for the line object.
- [func CTLineGetGlyphRuns(CTLine) -> CFArray](./ctlinegetglyphruns%28_%29.md)
  Returns the array of glyph runs that make up the line object.
- [func CTLineGetStringRange(CTLine) -> CFRange](./ctlinegetstringrange%28_%29.md)
  Gets the range of characters that originally spawned the glyphs in the line.
- [func CTLineGetPenOffsetForFlush(CTLine, CGFloat, Double) -> Double](./ctlinegetpenoffsetforflush%28_,_,_%29.md)
  Gets the pen offset required to draw flush text.
### Measuring Lines
- [func CTLineGetImageBounds(CTLine, CGContext?) -> CGRect](./ctlinegetimagebounds%28_,_%29.md)
  Calculates the image bounds for a line.
- [func CTLineGetTypographicBounds(CTLine, UnsafeMutablePointer<CGFloat>?, UnsafeMutablePointer<CGFloat>?, UnsafeMutablePointer<CGFloat>?) -> Double](./ctlinegettypographicbounds%28_,_,_,_%29.md)
  Calculates the typographic bounds of a line.
- [func CTLineGetTrailingWhitespaceWidth(CTLine) -> Double](./ctlinegettrailingwhitespacewidth%28_%29.md)
  Returns the trailing whitespace width for a line.
### Getting Line Positioning
- [func CTLineGetStringIndexForPosition(CTLine, CGPoint) -> CFIndex](./ctlinegetstringindexforposition%28_,_%29.md)
  Performs hit testing.
- [func CTLineGetOffsetForStringIndex(CTLine, CFIndex, UnsafeMutablePointer<CGFloat>?) -> CGFloat](./ctlinegetoffsetforstringindex%28_,_,_%29.md)
  Determines the graphical offset or offsets for a string index.
- [func CTLineEnumerateCaretOffsets(CTLine, (Double, CFIndex, Bool, UnsafeMutablePointer<Bool>) -> Void)](./ctlineenumeratecaretoffsets%28_,_%29.md)
  Enumerates caret offsets for characters in a line.
### Getting the Type Identifier
- [func CTLineGetTypeID() -> CFTypeID](./ctlinegettypeid%28%29.md)
  Returns the Core Foundation type identifier of the line object.
### Constants
- [enum CTLineTruncationType](./ctlinetruncationtype.md)
  Truncation types required by the [`CTLineCreateTruncatedLine(_:_:_:_:)`](./ctlinecreatetruncatedline%28_,_,_,_%29.md) function to tell the truncation engine which type of truncation is being requested.

## Relationships

### Conforms To
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)

## See Also

### Opaque Types
- [class CTFont](./ctfont.md)
  A font object.
- [class CTFontCollection](./ctfontcollection.md)
  A font collection.
- [class CTFontDescriptor](./ctfontdescriptor.md)
  A font descriptor.
- [class CTFrame](./ctframe.md)
  A frame.
- [class CTFramesetter](./ctframesetter.md)
  Generate text frames.
- [class CTGlyphInfo](./ctglyphinfo.md)
  Override a font’s specified mapping from Unicode to the glyph ID.
- [class CTParagraphStyle](./ctparagraphstyle.md)
  Paragraph or ruler attributes in an attributed string.
- [class CTRun](./ctrun.md)
  A glyph run.
- [class CTRunDelegate](./ctrundelegate.md)
  A run delegate.
- [class CTTextTab](./cttexttab.md)
  A tab in a paragraph style, storing an alignment type and location.
- [class CTTypesetter](./cttypesetter.md)
  A typesetter which performs line layout.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretext/ctline)*
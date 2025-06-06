# CTRun

**Framework**: Core Text  
**Kind**: class

A glyph run.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
class CTRun
```

#### Overview

A glyph run is a set of consecutive glyphs sharing the same attributes and direction.

The typesetter creates glyph runs as it produces lines from character strings, attributes, and font objects. That is, a line is constructed of one or more glyphs runs. Glyph runs can draw themselves into a graphic context, if desired, although most users have no need to interact directly with glyph runs.

## Topics

### Getting Glyph Run Data
- [func CTRunGetGlyphCount(CTRun) -> CFIndex](ctrungetglyphcount(_:).md)
  Gets the glyph count for the run.
- [func CTRunGetAttributes(CTRun) -> CFDictionary](ctrungetattributes(_:).md)
  Returns the attribute dictionary that was used to create the glyph run.
- [func CTRunGetStatus(CTRun) -> CTRunStatus](ctrungetstatus(_:).md)
  Returns the run’s status.
- [func CTRunGetGlyphsPtr(CTRun) -> UnsafePointer<CGGlyph>?](ctrungetglyphsptr(_:).md)
  Returns a direct pointer for the glyph array stored in the run.
- [func CTRunGetGlyphs(CTRun, CFRange, UnsafeMutablePointer<CGGlyph>)](ctrungetglyphs(_:_:_:).md)
  Copies a range of glyphs into a user-provided buffer.
- [func CTRunGetPositionsPtr(CTRun) -> UnsafePointer<CGPoint>?](ctrungetpositionsptr(_:).md)
  Returns a direct pointer for the glyph position array stored in the run.
- [func CTRunGetPositions(CTRun, CFRange, UnsafeMutablePointer<CGPoint>)](ctrungetpositions(_:_:_:).md)
  Copies a range of glyph positions into a user-provided buffer.
- [func CTRunGetAdvancesPtr(CTRun) -> UnsafePointer<CGSize>?](ctrungetadvancesptr(_:).md)
  Returns a direct pointer for the glyph advance array stored in the run.
- [func CTRunGetAdvances(CTRun, CFRange, UnsafeMutablePointer<CGSize>)](ctrungetadvances(_:_:_:).md)
  Copies a range of glyph advances into a user-provided buffer.
- [func CTRunGetStringIndicesPtr(CTRun) -> UnsafePointer<CFIndex>?](ctrungetstringindicesptr(_:).md)
  Returns a direct pointer for the string indices stored in the run.
- [func CTRunGetStringIndices(CTRun, CFRange, UnsafeMutablePointer<CFIndex>)](ctrungetstringindices(_:_:_:).md)
  Copies a range of string indices into a user-provided buffer.
- [func CTRunGetStringRange(CTRun) -> CFRange](ctrungetstringrange(_:).md)
  Gets the range of characters that originally spawned the glyphs in the run.
### Measuring the Glyph Run
- [func CTLineGetBoundsWithOptions(CTLine, CTLineBoundsOptions) -> CGRect](ctlinegetboundswithoptions(_:_:).md)
  Calculates the bounds for a line.
- [func CTRunGetTypographicBounds(CTRun, CFRange, UnsafeMutablePointer<CGFloat>?, UnsafeMutablePointer<CGFloat>?, UnsafeMutablePointer<CGFloat>?) -> Double](ctrungettypographicbounds(_:_:_:_:_:).md)
  Gets the typographic bounds of the run.
- [func CTRunGetImageBounds(CTRun, CGContext?, CFRange) -> CGRect](ctrungetimagebounds(_:_:_:).md)
  Calculates the image bounds for a glyph range.
- [func CTRunGetBaseAdvancesAndOrigins(CTRun, CFRange, UnsafeMutablePointer<CGSize>?, UnsafeMutablePointer<CGPoint>?)](ctrungetbaseadvancesandorigins(_:_:_:_:).md)
  Copies a range of base advances and origins into user-provided buffers.
### Drawing the Glyph Run
- [func CTRunDraw(CTRun, CGContext, CFRange)](ctrundraw(_:_:_:).md)
  Draws a complete run or part of one.
- [func CTRunGetTextMatrix(CTRun) -> CGAffineTransform](ctrungettextmatrix(_:).md)
  Returns the text matrix needed to draw this run.
### Getting the Type Identifier
- [func CTRunGetTypeID() -> CFTypeID](ctrungettypeid().md)
  Returns the Core Foundation type identifier of the run object.
### Constants
- [struct CTRunStatus](ctrunstatus.md)
  A bitfield that represents the disposition of the run.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)

## See Also

- [class CTFont](ctfont.md)
  A font object.
- [class CTFontCollection](ctfontcollection.md)
  A font collection.
- [class CTFontDescriptor](ctfontdescriptor.md)
  A font descriptor.
- [class CTFrame](ctframe.md)
  A frame.
- [class CTFramesetter](ctframesetter.md)
  Generate text frames.
- [class CTGlyphInfo](ctglyphinfo.md)
  Override a font’s specified mapping from Unicode to the glyph ID.
- [class CTLine](ctline.md)
  A line of text.
- [class CTParagraphStyle](ctparagraphstyle.md)
  Paragraph or ruler attributes in an attributed string.
- [class CTRunDelegate](ctrundelegate.md)
  A run delegate.
- [class CTTextTab](cttexttab.md)
  A tab in a paragraph style, storing an alignment type and location.
- [class CTTypesetter](cttypesetter.md)
  A typesetter which performs line layout.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretext/ctrun)*
# CTFrame

**Framework**: Core Text  
**Kind**: class

A frame.

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
class CTFrame
```

#### Overview

A frame contains multiple lines of text. The frame object is the output resulting from the text-framing process performed by a [`CTFramesetter`](ctframesetter.md) object.

You can draw the entire text frame directly into the current graphic context. The frame object contains an array of line objects that can be retrieved for individual rendering or to get glyph information.

## Topics

### Getting Frame Data
- [func CTFrameGetStringRange(CTFrame) -> CFRange](ctframegetstringrange(_:).md)
  Returns the range of characters originally requested to fill the frame.
- [func CTFrameGetVisibleStringRange(CTFrame) -> CFRange](ctframegetvisiblestringrange(_:).md)
  Returns the range of characters that actually fit in the frame.
- [func CTFrameGetPath(CTFrame) -> CGPath](ctframegetpath(_:).md)
  Returns the path used to create the frame.
- [func CTFrameGetFrameAttributes(CTFrame) -> CFDictionary?](ctframegetframeattributes(_:).md)
  Returns the frame attributes used to create the frame.
### Getting Lines
- [func CTFrameGetLines(CTFrame) -> CFArray](ctframegetlines(_:).md)
  Returns an array of lines stored in the frame.
- [func CTFrameGetLineOrigins(CTFrame, CFRange, UnsafeMutablePointer<CGPoint>)](ctframegetlineorigins(_:_:_:).md)
  Copies a range of line origins for a frame.
### Drawing the Frame
- [func CTFrameDraw(CTFrame, CGContext)](ctframedraw(_:_:).md)
  Draws an entire frame into a context.
### Getting the Type Identifier
- [func CTFrameGetTypeID() -> CFTypeID](ctframegettypeid().md)
  Returns the type identifier for the CTFrame opaque type.
### Data Types
- [enum CTFramePathFillRule](ctframepathfillrule.md)
  These constants specify the fill rule used by a frame
### Constants
- [enum CTFrameProgression](ctframeprogression.md)
  Constants that specify frame progression types.
- [let kCTFrameProgressionAttributeName: CFString](kctframeprogressionattributename.md)
  Specifies progression for a frame.
- [let kCTFramePathFillRuleAttributeName: CFString](kctframepathfillruleattributename.md)
  The key used to specify the fill rule for a frame.
- [let kCTFramePathWidthAttributeName: CFString](kctframepathwidthattributename.md)
  The key used to specify the frame width.
- [let kCTFrameClippingPathsAttributeName: CFString](kctframeclippingpathsattributename.md)
  Specifies array of paths to clip frame.
- [let kCTFramePathClippingPathAttributeName: CFString](kctframepathclippingpathattributename.md)
  Specifies clipping path.

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
- [class CTFramesetter](ctframesetter.md)
  Generate text frames.
- [class CTGlyphInfo](ctglyphinfo.md)
  Override a font’s specified mapping from Unicode to the glyph ID.
- [class CTLine](ctline.md)
  A line of text.
- [class CTParagraphStyle](ctparagraphstyle.md)
  Paragraph or ruler attributes in an attributed string.
- [class CTRun](ctrun.md)
  A glyph run.
- [class CTRunDelegate](ctrundelegate.md)
  A run delegate.
- [class CTTextTab](cttexttab.md)
  A tab in a paragraph style, storing an alignment type and location.
- [class CTTypesetter](cttypesetter.md)
  A typesetter which performs line layout.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretext/ctframe)*
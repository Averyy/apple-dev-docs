# CTFramesetter

**Framework**: Core Text  
**Kind**: class  
**Role**: Class

Generate text frames.

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
class CTFramesetter
```

```c
typedef const struct __CTFramesetter * CTFramesetterRef;
```

## Overview

`CTFramesetter` is an object factory for [`CTFrame`](./ctframe.md) objects.

The framesetter takes an attributed string object and a shape descriptor object and calls into the typesetter to create line objects that fill that shape. The output is a frame object containing an array of lines. The frame can then draw itself directly into the current graphic context.

## Topics

### Creating a Framesetter
- [func CTFramesetterCreateWithAttributedString(CFAttributedString) -> CTFramesetter](./ctframesettercreatewithattributedstring%28_%29.md)
  Creates an immutable framesetter object from an attributed string.
- [func CTFramesetterCreateWithTypesetter(CTTypesetter) -> CTFramesetter](./ctframesettercreatewithtypesetter%28_%29.md)
  Creates a framesetter directly from a typesetter.
### Creating Frames
- [func CTFramesetterCreateFrame(CTFramesetter, CFRange, CGPath, CFDictionary?) -> CTFrame](./ctframesettercreateframe%28_,_,_,_%29.md)
  Creates an immutable frame using a framesetter.
- [func CTFramesetterGetTypesetter(CTFramesetter) -> CTTypesetter](./ctframesettergettypesetter%28_%29.md)
  Returns the typesetter object being used by the framesetter.
### Frame Sizing
- [func CTFramesetterSuggestFrameSizeWithConstraints(CTFramesetter, CFRange, CFDictionary?, CGSize, UnsafeMutablePointer<CFRange>?) -> CGSize](./ctframesettersuggestframesizewithconstraints%28_,_,_,_,_%29.md)
  Determines the frame size needed for a string range.
### Getting the Type Identifier
- [func CTFramesetterGetTypeID() -> CFTypeID](./ctframesettergettypeid%28%29.md)
  Returns the Core Foundation type identifier of the framesetter object.

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
- [class CTGlyphInfo](./ctglyphinfo.md)
  Override a font’s specified mapping from Unicode to the glyph ID.
- [class CTLine](./ctline.md)
  A line of text.
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

*[View on Apple Developer](https://developer.apple.com/documentation/coretext/ctframesetter)*
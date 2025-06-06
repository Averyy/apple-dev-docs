# CTRunDelegate

**Framework**: Core Text  
**Kind**: class

A run delegate.

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
class CTRunDelegate
```

#### Overview

A run delegate is assigned to a run (attribute range) to control typographic traits such glyph ascent, glyph descent, and glyph width.

The callbacks defined for `CTRunDelegate` objects are provided by the owner of a run delegate and are used to modify glyph metrics during layout. The values returned by the delegate are applied to each glyph in the run or runs corresponding to the attribute with that delegate.

## Topics

### Creating a Run Delegate
- [func CTRunDelegateCreate(UnsafePointer<CTRunDelegateCallbacks>, UnsafeMutableRawPointer?) -> CTRunDelegate?](ctrundelegatecreate(_:_:).md)
  Creates an immutable instance of a run delegate.
### Getting Information About a Run Delegate
- [func CTRunDelegateGetRefCon(CTRunDelegate) -> UnsafeMutableRawPointer](ctrundelegategetrefcon(_:).md)
  Returns a run delegate’s “refCon” value.
- [func CTRunDelegateGetTypeID() -> CFTypeID](ctrundelegategettypeid().md)
  Returns the type of CTRunDelegate objects.
### Callbacks
- [typealias CTRunDelegateGetAscentCallback](ctrundelegategetascentcallback.md)
  Defines a pointer to a function that determines typographic ascent of glyphs in the run.
- [typealias CTRunDelegateGetDescentCallback](ctrundelegategetdescentcallback.md)
  Defines a pointer to a function that determines typographic descent of glyphs in the run.
- [typealias CTRunDelegateGetWidthCallback](ctrundelegategetwidthcallback.md)
  Defines a pointer to a function that determines the typographic width of glyphs in the run.
- [typealias CTRunDelegateDeallocateCallback](ctrundelegatedeallocatecallback.md)
  Defines a pointer to a function that is invoked when a CTRunDelegate object is deallocated.
### Data Types
- [struct CTRunDelegateCallbacks](ctrundelegatecallbacks.md)
  A structure holding pointers to callbacks implemented by the run delegate.
### Constants
- [Run Delegate Versions](1498177-run-delegate-versions.md)
  The version of the run delegate.

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
- [class CTRun](ctrun.md)
  A glyph run.
- [class CTTextTab](cttexttab.md)
  A tab in a paragraph style, storing an alignment type and location.
- [class CTTypesetter](cttypesetter.md)
  A typesetter which performs line layout.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretext/ctrundelegate)*
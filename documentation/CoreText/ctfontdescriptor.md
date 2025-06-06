# CTFontDescriptor

**Framework**: Core Text  
**Kind**: class

A font descriptor.

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
class CTFontDescriptor
```

#### Overview

A font descriptor is a dictionary of attributes (such as name, point size, and variation) that can completely specify a font.

A font descriptor can be an incomplete specification, in which case the system chooses the most appropriate font to match the given attributes.

## Topics

### Creating Font Descriptors
- [func CTFontDescriptorCreateWithNameAndSize(CFString, CGFloat) -> CTFontDescriptor](ctfontdescriptorcreatewithnameandsize(_:_:).md)
  Creates a new font descriptor with the provided PostScript name and size.
- [func CTFontDescriptorCreateWithAttributes(CFDictionary) -> CTFontDescriptor](ctfontdescriptorcreatewithattributes(_:).md)
  Creates a new font descriptor reference from a dictionary of attributes.
- [func CTFontDescriptorCreateCopyWithAttributes(CTFontDescriptor, CFDictionary) -> CTFontDescriptor](ctfontdescriptorcreatecopywithattributes(_:_:).md)
  Creates a copy of the original font descriptor with new attributes.
- [func CTFontDescriptorCreateCopyWithVariation(CTFontDescriptor, CFNumber, CGFloat) -> CTFontDescriptor](ctfontdescriptorcreatecopywithvariation(_:_:_:).md)
  Creates a copy of the original font descriptor with a new variation instance.
- [func CTFontDescriptorCreateCopyWithFeature(CTFontDescriptor, CFNumber, CFNumber) -> CTFontDescriptor](ctfontdescriptorcreatecopywithfeature(_:_:_:).md)
  Copies a font descriptor with new feature settings.
- [func CTFontDescriptorCreateCopyWithFamily(CTFontDescriptor, CFString) -> CTFontDescriptor?](ctfontdescriptorcreatecopywithfamily(_:_:).md)
  Creates a copy of the font descriptor in the specified family based on the traits of the original.
- [func CTFontDescriptorCreateCopyWithSymbolicTraits(CTFontDescriptor, CTFontSymbolicTraits, CTFontSymbolicTraits) -> CTFontDescriptor?](ctfontdescriptorcreatecopywithsymbolictraits(_:_:_:).md)
  Creates a copy of the font descriptor with the specified symbolic traits as the original.
- [func CTFontDescriptorCreateMatchingFontDescriptors(CTFontDescriptor, CFSet?) -> CFArray?](ctfontdescriptorcreatematchingfontdescriptors(_:_:).md)
  Returns an array of normalized font descriptors matching the provided descriptor.
- [func CTFontDescriptorCreateMatchingFontDescriptor(CTFontDescriptor, CFSet?) -> CTFontDescriptor?](ctfontdescriptorcreatematchingfontdescriptor(_:_:).md)
  Returns the single preferred matching font descriptor based on the original descriptor and system precedence.
### Getting Attributes
- [func CTFontDescriptorCopyAttributes(CTFontDescriptor) -> CFDictionary](ctfontdescriptorcopyattributes(_:).md)
  Returns the attributes dictionary of the font descriptor.
- [func CTFontDescriptorCopyAttribute(CTFontDescriptor, CFString) -> CFTypeRef?](ctfontdescriptorcopyattribute(_:_:).md)
  Returns the value associated with an arbitrary attribute.
- [func CTFontDescriptorCopyLocalizedAttribute(CTFontDescriptor, CFString, UnsafeMutablePointer<Unmanaged<CFString>?>?) -> CFTypeRef?](ctfontdescriptorcopylocalizedattribute(_:_:_:).md)
  Returns a localized value for the requested attribute, if available.
### Getting the Font Descriptor Type
- [func CTFontDescriptorGetTypeID() -> CFTypeID](ctfontdescriptorgettypeid().md)
  Returns the type identifier for Core Text font descriptor references.
### Accessing Font Attributes
- [Font Attributes](font-attributes.md)
  The keys for accessing font attributes from a font descriptor.
- [enum CTFontOrientation](ctfontorientation.md)
  The intended rendering orientation of the font for obtaining glyph metrics.
- [enum CTFontFormat](ctfontformat.md)
  The recognized format of the font.
- [typealias CTFontPriority](ctfontpriority.md)
  The priority of font descriptors when resolving duplicates and sorting match results.
### Accessing Font Traits
- [Font Traits](font-traits.md)
  The keys for accessing font traits from a font descriptor.
- [Font Class Mask Shift Constants](font-class-mask-shift-constants.md)
  These constants represent the font class mask shift.
- [struct CTFontSymbolicTraits](ctfontsymbolictraits.md)
  The symbolic representation of stylistic font attributes.
- [struct CTFontStylisticClass](ctfontstylisticclass.md)
  The stylistic class values of the font.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)

## See Also

- [class CTFont](ctfont.md)
  A font object.
- [class CTFontCollection](ctfontcollection.md)
  A font collection.
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
- [class CTRunDelegate](ctrundelegate.md)
  A run delegate.
- [class CTTextTab](cttexttab.md)
  A tab in a paragraph style, storing an alignment type and location.
- [class CTTypesetter](cttypesetter.md)
  A typesetter which performs line layout.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretext/ctfontdescriptor)*
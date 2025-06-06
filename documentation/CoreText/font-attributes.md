# Font Attributes

**Framework**: Core Text

The keys for accessing font attributes from a font descriptor.

## Topics

### Font Attribute Keys
- [let kCTFontURLAttribute: CFString](kctfonturlattribute.md)
  The font URL from the font descriptor.
- [let kCTFontNameAttribute: CFString](kctfontnameattribute.md)
  The PostScript name from the font descriptor.
- [let kCTFontDisplayNameAttribute: CFString](kctfontdisplaynameattribute.md)
  The name used to display the font.
- [let kCTFontFamilyNameAttribute: CFString](kctfontfamilynameattribute.md)
  The font family name from the font descriptor.
- [let kCTFontStyleNameAttribute: CFString](kctfontstylenameattribute.md)
  The style name of the font.
- [let kCTFontTraitsAttribute: CFString](kctfonttraitsattribute.md)
  The dictionary of font traits for stylistic information.
- [let kCTFontVariationAttribute: CFString](kctfontvariationattribute.md)
  The dictionary of font variation.
- [let kCTFontSizeAttribute: CFString](kctfontsizeattribute.md)
  The font point size.
- [let kCTFontMatrixAttribute: CFString](kctfontmatrixattribute.md)
  The font transformation matrix when creating a font.
- [let kCTFontCascadeListAttribute: CFString](kctfontcascadelistattribute.md)
  The cascade list used for a font reference.
- [let kCTFontCharacterSetAttribute: CFString](kctfontcharactersetattribute.md)
  The Unicode character coverage set for a font reference.
- [let kCTFontLanguagesAttribute: CFString](kctfontlanguagesattribute.md)
  A list of covered languages for a font reference.
- [let kCTFontBaselineAdjustAttribute: CFString](kctfontbaselineadjustattribute.md)
  The baseline adjustment for a font reference.
- [let kCTFontMacintoshEncodingsAttribute: CFString](kctfontmacintoshencodingsattribute.md)
  The Macintosh encodings for a font reference.
- [let kCTFontFeaturesAttribute: CFString](kctfontfeaturesattribute.md)
  The font features for a font reference.
- [let kCTFontFeatureSettingsAttribute: CFString](kctfontfeaturesettingsattribute.md)
  The font features settings for a font reference.
- [let kCTFontFixedAdvanceAttribute: CFString](kctfontfixedadvanceattribute.md)
  A fixed advance to be used for a font reference.
- [let kCTFontOrientationAttribute: CFString](kctfontorientationattribute.md)
  The orientation for the glyphs of the font.
- [let kCTFontFormatAttribute: CFString](kctfontformatattribute.md)
  The recognized format of the font.
- [let kCTFontRegistrationScopeAttribute: CFString](kctfontregistrationscopeattribute.md)
  The font descriptor’s registration scope.
- [let kCTFontPriorityAttribute: CFString](kctfontpriorityattribute.md)
  The font priority used by font descriptors when resolving duplicates and sorting match results.
- [let kCTFontEnabledAttribute: CFString](kctfontenabledattribute.md)
  The font enabled state.
- [let kCTFontDownloadableAttribute: CFString](kctfontdownloadableattribute.md)
  The font downloadable state.
- [let kCTFontDownloadedAttribute: CFString](kctfontdownloadedattribute.md)
  The download state.

## See Also

- [func CTFontDescriptorCopyAttribute(CTFontDescriptor, CFString) -> CFTypeRef?](ctfontdescriptorcopyattribute(_:_:).md)
  Returns the value associated with an arbitrary attribute.
- [func CTFontDescriptorCopyAttributes(CTFontDescriptor) -> CFDictionary](ctfontdescriptorcopyattributes(_:).md)
  Returns the attributes dictionary of the font descriptor.
- [func CTFontCopyAttribute(CTFont, CFString) -> CFTypeRef?](ctfontcopyattribute(_:_:).md)
  Returns the value associated with an arbitrary attribute of the given font.
- [enum CTFontOrientation](ctfontorientation.md)
  The intended rendering orientation of the font for obtaining glyph metrics.
- [enum CTFontFormat](ctfontformat.md)
  The recognized format of the font.
- [typealias CTFontPriority](ctfontpriority.md)
  The priority of font descriptors when resolving duplicates and sorting match results.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretext/font-attributes)*
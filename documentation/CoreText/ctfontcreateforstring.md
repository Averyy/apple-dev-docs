# CTFontCreateForString(_:_:_:)

**Framework**: Core Text  
**Kind**: func

Returns a font reference that most accurately maps the string range based on the current font.

**Availability**:
- iOS 3.2+
- iPadOS 3.2+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func CTFontCreateForString(_ currentFont: CTFont, _ string: CFString, _ range: CFRange) -> CTFont
```

#### Return Value

The best substitute font from the cascade list of the current font that can encode the specified string range.

#### Discussion

If the current font can encode the string range, the function retains and returns the font.

## Parameters

- `currentFont`: The current font that contains a valid cascade list.
- `string`: A Unicode string containing characters that can’t be encoded by the current font.
- `range`: A   structure specifying the range of the string to map.

## See Also

- [func CTFontCopyCharacterSet(CTFont) -> CFCharacterSet](ctfontcopycharacterset(_:).md)
  Returns the Unicode character set of the font.
- [func CTFontGetGlyphsForCharacters(CTFont, UnsafePointer<UniChar>, UnsafeMutablePointer<CGGlyph>, CFIndex) -> Bool](ctfontgetglyphsforcharacters(_:_:_:_:).md)
  Performs basic character-to-glyph mapping.
- [let kCTFontCascadeListAttribute: CFString](kctfontcascadelistattribute.md)
  The cascade list used for a font reference.
- [func CTFontCreateWithName(CFString, CGFloat, UnsafePointer<CGAffineTransform>?) -> CTFont](ctfontcreatewithname(_:_:_:).md)
  Returns a new font reference for the given name.
- [func CTFontCreateWithNameAndOptions(CFString, CGFloat, UnsafePointer<CGAffineTransform>?, CTFontOptions) -> CTFont](ctfontcreatewithnameandoptions(_:_:_:_:).md)
  Returns a new font reference for the given name.
- [func CTFontCreateWithFontDescriptor(CTFontDescriptor, CGFloat, UnsafePointer<CGAffineTransform>?) -> CTFont](ctfontcreatewithfontdescriptor(_:_:_:).md)
  Returns a new font reference that best matches the given font descriptor.
- [func CTFontCreateWithFontDescriptorAndOptions(CTFontDescriptor, CGFloat, UnsafePointer<CGAffineTransform>?, CTFontOptions) -> CTFont](ctfontcreatewithfontdescriptorandoptions(_:_:_:_:).md)
  Returns a new font reference that best matches the given font descriptor.
- [func CTFontCreateUIFontForLanguage(CTFontUIFontType, CGFloat, CFString?) -> CTFont?](ctfontcreateuifontforlanguage(_:_:_:).md)
  Returns the special user-interface font for the given language and user-interface type.
- [func CTFontCreateCopyWithAttributes(CTFont, CGFloat, UnsafePointer<CGAffineTransform>?, CTFontDescriptor?) -> CTFont](ctfontcreatecopywithattributes(_:_:_:_:).md)
  Returns a new font with additional attributes based on the original font.
- [func CTFontCreateCopyWithSymbolicTraits(CTFont, CGFloat, UnsafePointer<CGAffineTransform>?, CTFontSymbolicTraits, CTFontSymbolicTraits) -> CTFont?](ctfontcreatecopywithsymbolictraits(_:_:_:_:_:).md)
  Returns a new font in the same font family as the original with the specified symbolic traits.
- [func CTFontCreateCopyWithFamily(CTFont, CGFloat, UnsafePointer<CGAffineTransform>?, CFString) -> CTFont?](ctfontcreatecopywithfamily(_:_:_:_:).md)
  Returns a new font in the specified family based on the traits of the original font.
- [func CTFontCreateForStringWithLanguage(CTFont, CFString, CFRange, CFString?) -> CTFont](ctfontcreateforstringwithlanguage(_:_:_:_:).md)
  Returns a font reference that most accurately maps the string range based on the current font and language.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretext/ctfontcreateforstring(_:_:_:))*
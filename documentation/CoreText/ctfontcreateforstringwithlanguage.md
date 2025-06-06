# CTFontCreateForStringWithLanguage(_:_:_:_:)

**Framework**: Core Text  
**Kind**: func

Returns a font reference that most accurately maps the string range based on the current font and language.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func CTFontCreateForStringWithLanguage(_ currentFont: CTFont, _ string: CFString, _ range: CFRange, _ language: CFString?) -> CTFont
```

#### Return Value

The best substitute font that can encode the specified string range.

#### Discussion

The current font itself can be returned if it covers the string provided. If the caller does not specify the language parameter, the function uses the current system language. The format of the language identifier should conform to [`UTS #35`](https://developer.apple.comhttp://unicode.org/reports/tr35/).

## Parameters

- `currentFont`: The current font that contains a valid cascade list.
- `string`: A Unicode string containing characters that can’t be encoded by the current font.
- `range`: A   specifying the range of the string to map.
- `language`: A language identifier to select a font for a particular localization.

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
- [func CTFontCreateForString(CTFont, CFString, CFRange) -> CTFont](ctfontcreateforstring(_:_:_:).md)
  Returns a font reference that most accurately maps the string range based on the current font.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretext/ctfontcreateforstringwithlanguage(_:_:_:_:))*
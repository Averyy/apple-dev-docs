# CTFontCreateForStringWithLanguage(_:_:_:_:)

**Framework**: Core Text  
**Kind**: func  
**Role**: Function

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

```c
extern CTFontRefCTFontCreateForStringWithLanguage(CTFontRef currentFont, CFStringRef string, CFRange range, CFStringRef language);
```

## Return Value

The best substitute font that can encode the specified string range.

## Discussion

The current font itself can be returned if it covers the string provided. If the caller does not specify the language parameter, the function uses the current system language. The format of the language identifier should conform to [UTS #35](http://unicode.org/reports/tr35/).

## Parameters

- `currentFont`: The current font that contains a valid cascade list.
- `string`: A Unicode string containing characters that can’t be encoded by the current font.
- `range`: A [`CFRange`](../CoreFoundation/cfrange.md) specifying the range of the string to map.
- `language`: A language identifier to select a font for a particular localization.

## See Also

### Related Documentation
- [func CTFontCopyCharacterSet(CTFont) -> CFCharacterSet](./ctfontcopycharacterset%28_%29.md)
  Returns the Unicode character set of the font.
- [func CTFontGetGlyphsForCharacters(CTFont, UnsafePointer<UniChar>, UnsafeMutablePointer<CGGlyph>, CFIndex) -> Bool](./ctfontgetglyphsforcharacters%28_,_,_,_%29.md)
  Performs basic character-to-glyph mapping.
- [let kCTFontCascadeListAttribute: CFString](./kctfontcascadelistattribute.md)
  The cascade list used for a font reference.
### Creating Fonts
- [func CTFontCreateWithName(CFString, CGFloat, UnsafePointer<CGAffineTransform>?) -> CTFont](./ctfontcreatewithname%28_,_,_%29.md)
  Returns a new font reference for the given name.
- [func CTFontCreateWithNameAndOptions(CFString, CGFloat, UnsafePointer<CGAffineTransform>?, CTFontOptions) -> CTFont](./ctfontcreatewithnameandoptions%28_,_,_,_%29.md)
  Returns a new font reference for the given name.
- [func CTFontCreateWithFontDescriptor(CTFontDescriptor, CGFloat, UnsafePointer<CGAffineTransform>?) -> CTFont](./ctfontcreatewithfontdescriptor%28_,_,_%29.md)
  Returns a new font reference that best matches the given font descriptor.
- [func CTFontCreateWithFontDescriptorAndOptions(CTFontDescriptor, CGFloat, UnsafePointer<CGAffineTransform>?, CTFontOptions) -> CTFont](./ctfontcreatewithfontdescriptorandoptions%28_,_,_,_%29.md)
  Returns a new font reference that best matches the given font descriptor.
- [func CTFontCreateUIFontForLanguage(CTFontUIFontType, CGFloat, CFString?) -> CTFont?](./ctfontcreateuifontforlanguage%28_,_,_%29.md)
  Returns the special user-interface font for the given language and user-interface type.
- [func CTFontCreateCopyWithAttributes(CTFont, CGFloat, UnsafePointer<CGAffineTransform>?, CTFontDescriptor?) -> CTFont](./ctfontcreatecopywithattributes%28_,_,_,_%29.md)
  Returns a new font with additional attributes based on the original font.
- [func CTFontCreateCopyWithSymbolicTraits(CTFont, CGFloat, UnsafePointer<CGAffineTransform>?, CTFontSymbolicTraits, CTFontSymbolicTraits) -> CTFont?](./ctfontcreatecopywithsymbolictraits%28_,_,_,_,_%29.md)
  Returns a new font in the same font family as the original with the specified symbolic traits.
- [func CTFontCreateCopyWithFamily(CTFont, CGFloat, UnsafePointer<CGAffineTransform>?, CFString) -> CTFont?](./ctfontcreatecopywithfamily%28_,_,_,_%29.md)
  Returns a new font in the specified family based on the traits of the original font.
- [func CTFontCreateForString(CTFont, CFString, CFRange) -> CTFont](./ctfontcreateforstring%28_,_,_%29.md)
  Returns a font reference that most accurately maps the string range based on the current font.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretext/ctfontcreateforstringwithlanguage(_:_:_:_:))*
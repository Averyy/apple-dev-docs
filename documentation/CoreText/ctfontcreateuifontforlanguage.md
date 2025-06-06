# CTFontCreateUIFontForLanguage(_:_:_:)

**Framework**: Core Text  
**Kind**: func

Returns the special user-interface font for the given language and user-interface type.

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
func CTFontCreateUIFontForLanguage(_ uiType: CTFontUIFontType, _ size: CGFloat, _ language: CFString?) -> CTFont?
```

#### Return Value

The correct font for various user-interface uses.

#### Discussion

The only required parameter is the `uiType` selector; the other parameters have default values.

## Parameters

- `uiType`: A  constant specifying the intended user-interface use for the requested font reference. See Enumerations for possible values.
- `size`: The point size for the font reference. If   is specified, the default size for the requested user-interface type is used.
- `language`: Language specifier string to select a font for a particular localization. If   is specified, the current system language is used. The format of the language identifier should conform to the RFC 3066bis standard.

## See Also

- [func CTFontCreateWithName(CFString, CGFloat, UnsafePointer<CGAffineTransform>?) -> CTFont](ctfontcreatewithname(_:_:_:).md)
  Returns a new font reference for the given name.
- [func CTFontCreateWithNameAndOptions(CFString, CGFloat, UnsafePointer<CGAffineTransform>?, CTFontOptions) -> CTFont](ctfontcreatewithnameandoptions(_:_:_:_:).md)
  Returns a new font reference for the given name.
- [func CTFontCreateWithFontDescriptor(CTFontDescriptor, CGFloat, UnsafePointer<CGAffineTransform>?) -> CTFont](ctfontcreatewithfontdescriptor(_:_:_:).md)
  Returns a new font reference that best matches the given font descriptor.
- [func CTFontCreateWithFontDescriptorAndOptions(CTFontDescriptor, CGFloat, UnsafePointer<CGAffineTransform>?, CTFontOptions) -> CTFont](ctfontcreatewithfontdescriptorandoptions(_:_:_:_:).md)
  Returns a new font reference that best matches the given font descriptor.
- [func CTFontCreateCopyWithAttributes(CTFont, CGFloat, UnsafePointer<CGAffineTransform>?, CTFontDescriptor?) -> CTFont](ctfontcreatecopywithattributes(_:_:_:_:).md)
  Returns a new font with additional attributes based on the original font.
- [func CTFontCreateCopyWithSymbolicTraits(CTFont, CGFloat, UnsafePointer<CGAffineTransform>?, CTFontSymbolicTraits, CTFontSymbolicTraits) -> CTFont?](ctfontcreatecopywithsymbolictraits(_:_:_:_:_:).md)
  Returns a new font in the same font family as the original with the specified symbolic traits.
- [func CTFontCreateCopyWithFamily(CTFont, CGFloat, UnsafePointer<CGAffineTransform>?, CFString) -> CTFont?](ctfontcreatecopywithfamily(_:_:_:_:).md)
  Returns a new font in the specified family based on the traits of the original font.
- [func CTFontCreateForString(CTFont, CFString, CFRange) -> CTFont](ctfontcreateforstring(_:_:_:).md)
  Returns a font reference that most accurately maps the string range based on the current font.
- [func CTFontCreateForStringWithLanguage(CTFont, CFString, CFRange, CFString?) -> CTFont](ctfontcreateforstringwithlanguage(_:_:_:_:).md)
  Returns a font reference that most accurately maps the string range based on the current font and language.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretext/ctfontcreateuifontforlanguage(_:_:_:))*
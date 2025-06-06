# CTFontCreateCopyWithFamily(_:_:_:_:)

**Framework**: Core Text  
**Kind**: func

Returns a new font in the specified family based on the traits of the original font.

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
func CTFontCreateCopyWithFamily(_ font: CTFont, _ size: CGFloat, _ matrix: UnsafePointer<CGAffineTransform>?, _ family: CFString) -> CTFont?
```

#### Return Value

A new font reference with the original traits in the given family, or `NULL` if none is found in the system.

## Parameters

- `font`: The original font reference on which to base the new font.
- `size`: The point size for the font reference. If   is specified, the original font’s size is preserved.
- `matrix`: The transformation matrix for the font.  In most cases, set this parameter to be  .  If   is specified, the original font’s matrix is preserved.
- `family`: The name of the desired family.

## See Also

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
- [func CTFontCreateForString(CTFont, CFString, CFRange) -> CTFont](ctfontcreateforstring(_:_:_:).md)
  Returns a font reference that most accurately maps the string range based on the current font.
- [func CTFontCreateForStringWithLanguage(CTFont, CFString, CFRange, CFString?) -> CTFont](ctfontcreateforstringwithlanguage(_:_:_:_:).md)
  Returns a font reference that most accurately maps the string range based on the current font and language.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretext/ctfontcreatecopywithfamily(_:_:_:_:))*
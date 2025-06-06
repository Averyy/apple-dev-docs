# CTFontCreateWithName(_:_:_:)

**Framework**: Core Text  
**Kind**: func

Returns a new font reference for the given name.

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
func CTFontCreateWithName(_ name: CFString, _ size: CGFloat, _ matrix: UnsafePointer<CGAffineTransform>?) -> CTFont
```

#### Return Value

Returns a `CTFontRef` that best matches the name provided with size and matrix attributes.

#### Discussion

The `name` parameter is the only required parameter, and default values are used for unspecified parameters (`0.0` for `size` and `NULL` for `matrix`). If all parameters cannot be matched identically, a best match is found.

## Parameters

- `name`: The font name for which you wish to create a new font reference. A valid PostScript name is preferred, although other font name types are matched in a fallback manner.
- `size`: The point size for the font reference. If   is specified, the default font size of   is used.  This parameter is optional.
- `matrix`: The transformation matrix for the font.  In most cases, set this parameter to be  .  If   is specified, the identity matrix is used. This parameter is optional.

## See Also

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
- [func CTFontCreateForStringWithLanguage(CTFont, CFString, CFRange, CFString?) -> CTFont](ctfontcreateforstringwithlanguage(_:_:_:_:).md)
  Returns a font reference that most accurately maps the string range based on the current font and language.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretext/ctfontcreatewithname(_:_:_:))*
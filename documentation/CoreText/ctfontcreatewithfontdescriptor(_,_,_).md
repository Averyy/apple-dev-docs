# CTFontCreateWithFontDescriptor(_:_:_:)

**Framework**: Core Text  
**Kind**: func  
**Role**: Function

Returns a new font reference that best matches the given font descriptor.

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
func CTFontCreateWithFontDescriptor(_ descriptor: CTFontDescriptor, _ size: CGFloat, _ matrix: UnsafePointer<CGAffineTransform>?) -> CTFont
```

```c
extern CTFontRefCTFontCreateWithFontDescriptor(CTFontDescriptorRef descriptor, CGFloat size, const CGAffineTransform *matrix);
```

#### Return Value

A CTFontRef that best matches the attributes provided with the font descriptor.

#### Discussion

The `size` and `matrix` parameters override any specified in the font descriptor unless they are unspecified (`0.0` for `size` and `NULL` for `matrix`). A best match font is always returned, and default values are used for any unspecified parameters.

## Parameters

- `descriptor`: A font descriptor containing attributes that specify the requested font.
- `size`: The point size for the font reference. If `0.0` is specified, the default font size of `12.0` is used.  This parameter is optional.
- `matrix`: The transformation matrix for the font.  In most cases, set this parameter to be `NULL`.  If `NULL` is specified, the identity matrix is used.  This parameter is optional.

## See Also

### Creating Fonts
- [func CTFontCreateWithName(CFString, CGFloat, UnsafePointer<CGAffineTransform>?) -> CTFont](./ctfontcreatewithname%28_,_,_%29.md)
  Returns a new font reference for the given name.
- [func CTFontCreateWithNameAndOptions(CFString, CGFloat, UnsafePointer<CGAffineTransform>?, CTFontOptions) -> CTFont](./ctfontcreatewithnameandoptions%28_,_,_,_%29.md)
  Returns a new font reference for the given name.
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
- [func CTFontCreateForStringWithLanguage(CTFont, CFString, CFRange, CFString?) -> CTFont](./ctfontcreateforstringwithlanguage%28_,_,_,_%29.md)
  Returns a font reference that most accurately maps the string range based on the current font and language.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretext/ctfontcreatewithfontdescriptor(_:_:_:))*
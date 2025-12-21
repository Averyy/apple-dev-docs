# CTFontCopyDefaultCascadeListForLanguages(_:_:)

**Framework**: Core Text  
**Kind**: func

Retrieves an ordered list of font substitution preferences.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func CTFontCopyDefaultCascadeListForLanguages(_ font: CTFont, _ languagePrefList: CFArray?) -> CFArray?
```

#### Return Value

An ordered list of [`CTFontDescriptor`](ctfontdescriptor.md)s for font fallback according to the given language preferences.

#### Discussion

When the original `font` used for text layout and rendering does not support a certain Unicode character from the provided text, the system follows this list to pick a fallback font that includes the character.

The font alternatives in the cascade list match the original font’s style, weight, and width.

## Parameters

- `font`: The font reference.
- `languagePrefList`: The language preference list, an ordered array of  s of ISO language codes.

## See Also

- [func CTFontCopyFontDescriptor(CTFont) -> CTFontDescriptor](ctfontcopyfontdescriptor(_:).md)
  Returns the normalized font descriptor for the given font reference.
- [func CTFontCopyAttribute(CTFont, CFString) -> CFTypeRef?](ctfontcopyattribute(_:_:).md)
  Returns the value associated with an arbitrary attribute of the given font.
- [func CTFontGetSize(CTFont) -> CGFloat](ctfontgetsize(_:).md)
  Returns the point size of the given font.
- [func CTFontGetMatrix(CTFont) -> CGAffineTransform](ctfontgetmatrix(_:).md)
  Returns the transformation matrix of the given font.
- [func CTFontGetSymbolicTraits(CTFont) -> CTFontSymbolicTraits](ctfontgetsymbolictraits(_:).md)
  Returns the symbolic traits of the given font.
- [func CTFontCopyTraits(CTFont) -> CFDictionary](ctfontcopytraits(_:).md)
  Returns the traits dictionary of the given font.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretext/ctfontcopydefaultcascadelistforlanguages(_:_:))*
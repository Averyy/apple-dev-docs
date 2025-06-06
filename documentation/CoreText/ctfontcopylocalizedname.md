# CTFontCopyLocalizedName(_:_:_:)

**Framework**: Core Text  
**Kind**: func

Returns a reference to a localized name for the given font.

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
func CTFontCopyLocalizedName(_ font: CTFont, _ nameKey: CFString, _ actualLanguage: UnsafeMutablePointer<Unmanaged<CFString>?>?) -> CFString?
```

#### Return Value

A specific localized name from the font reference or `NULL` if the font does not have an entry for the requested name key.

#### Discussion

The name is localized based on the user’s global language preference precedence. That is, the user’s language preference is a list of languages in order of precedence. So, for example, if the list had Japanese and English, in that order, then a font that did not have Japanese name strings but had English strings would return the English strings.

## Parameters

- `font`: The font reference.
- `nameKey`: The name specifier. See   for possible values.
- `actualLanguage`: On output, points to the language string of the returned name string. The format of the language identifier conforms to the RFC 3066bis standard.

## See Also

- [func CTFontCopyPostScriptName(CTFont) -> CFString](ctfontcopypostscriptname(_:).md)
  Returns the PostScript name of the given font.
- [func CTFontCopyFamilyName(CTFont) -> CFString](ctfontcopyfamilyname(_:).md)
  Returns the family name of the given font.
- [func CTFontCopyFullName(CTFont) -> CFString](ctfontcopyfullname(_:).md)
  Returns the full name of the given font.
- [func CTFontCopyDisplayName(CTFont) -> CFString](ctfontcopydisplayname(_:).md)
  Returns the display name of the given font.
- [func CTFontCopyName(CTFont, CFString) -> CFString?](ctfontcopyname(_:_:).md)
  Returns a reference to the requested name of the given font.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretext/ctfontcopylocalizedname(_:_:_:))*
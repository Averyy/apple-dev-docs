# CTFontCopyName(_:_:)

**Framework**: Core Text  
**Kind**: func

Returns a reference to the requested name of the given font.

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
func CTFontCopyName(_ font: CTFont, _ nameKey: CFString) -> CFString?
```

#### Return Value

The requested name for the font, or `NULL` if the font does not have an entry for the requested name. The Unicode version of the name is preferred, otherwise the first available version is returned.

## Parameters

- `font`: The font reference.
- `nameKey`: The name specifier. See   for possible values.

## See Also

- [func CTFontCopyPostScriptName(CTFont) -> CFString](ctfontcopypostscriptname(_:).md)
  Returns the PostScript name of the given font.
- [func CTFontCopyFamilyName(CTFont) -> CFString](ctfontcopyfamilyname(_:).md)
  Returns the family name of the given font.
- [func CTFontCopyFullName(CTFont) -> CFString](ctfontcopyfullname(_:).md)
  Returns the full name of the given font.
- [func CTFontCopyDisplayName(CTFont) -> CFString](ctfontcopydisplayname(_:).md)
  Returns the display name of the given font.
- [func CTFontCopyLocalizedName(CTFont, CFString, UnsafeMutablePointer<Unmanaged<CFString>?>?) -> CFString?](ctfontcopylocalizedname(_:_:_:).md)
  Returns a reference to a localized name for the given font.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretext/ctfontcopyname(_:_:))*
# CTFontCopyDisplayName(_:)

**Framework**: Core Text  
**Kind**: func

Returns the display name of the given font.

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
func CTFontCopyDisplayName(_ font: CTFont) -> CFString
```

#### Discussion

A retained reference to the localized display name of the font.

## Parameters

- `font`: The font reference.

## See Also

- [func CTFontCopyPostScriptName(CTFont) -> CFString](ctfontcopypostscriptname(_:).md)
  Returns the PostScript name of the given font.
- [func CTFontCopyFamilyName(CTFont) -> CFString](ctfontcopyfamilyname(_:).md)
  Returns the family name of the given font.
- [func CTFontCopyFullName(CTFont) -> CFString](ctfontcopyfullname(_:).md)
  Returns the full name of the given font.
- [func CTFontCopyName(CTFont, CFString) -> CFString?](ctfontcopyname(_:_:).md)
  Returns a reference to the requested name of the given font.
- [func CTFontCopyLocalizedName(CTFont, CFString, UnsafeMutablePointer<Unmanaged<CFString>?>?) -> CFString?](ctfontcopylocalizedname(_:_:_:).md)
  Returns a reference to a localized name for the given font.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretext/ctfontcopydisplayname(_:))*
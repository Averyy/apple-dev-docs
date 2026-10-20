# CTFontCopyFamilyName(_:)

**Framework**: Core Text  
**Kind**: func  
**Role**: Function

Returns the family name of the given font.

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
func CTFontCopyFamilyName(_ font: CTFont) -> CFString
```

```c
extern CFStringRefCTFontCopyFamilyName(CTFontRef font);
```

#### Return Value

A retained reference to the family name of the font.

## Parameters

- `font`: The font reference.

## See Also

### Getting Font Names
- [func CTFontCopyPostScriptName(CTFont) -> CFString](./ctfontcopypostscriptname%28_%29.md)
  Returns the PostScript name of the given font.
- [func CTFontCopyFullName(CTFont) -> CFString](./ctfontcopyfullname%28_%29.md)
  Returns the full name of the given font.
- [func CTFontCopyDisplayName(CTFont) -> CFString](./ctfontcopydisplayname%28_%29.md)
  Returns the display name of the given font.
- [func CTFontCopyName(CTFont, CFString) -> CFString?](./ctfontcopyname%28_,_%29.md)
  Returns a reference to the requested name of the given font.
- [func CTFontCopyLocalizedName(CTFont, CFString, UnsafeMutablePointer<Unmanaged<CFString>?>?) -> CFString?](./ctfontcopylocalizedname%28_,_,_%29.md)
  Returns a reference to a localized name for the given font.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretext/ctfontcopyfamilyname(_:))*
# CTFontCopyPostScriptName(_:)

**Framework**: Core Text  
**Kind**: func  
**Role**: Function

Returns the PostScript name of the given font.

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
func CTFontCopyPostScriptName(_ font: CTFont) -> CFString
```

```c
extern CFStringRefCTFontCopyPostScriptName(CTFontRef font);
```

## Return Value

A retained reference to the PostScript name of the font.

## Parameters

- `font`: The font reference.

## See Also

### Getting Font Names
- [func CTFontCopyFamilyName(CTFont) -> CFString](./ctfontcopyfamilyname%28_%29.md)
  Returns the family name of the given font.
- [func CTFontCopyFullName(CTFont) -> CFString](./ctfontcopyfullname%28_%29.md)
  Returns the full name of the given font.
- [func CTFontCopyDisplayName(CTFont) -> CFString](./ctfontcopydisplayname%28_%29.md)
  Returns the display name of the given font.
- [func CTFontCopyName(CTFont, CFString) -> CFString?](./ctfontcopyname%28_,_%29.md)
  Returns a reference to the requested name of the given font.
- [func CTFontCopyLocalizedName(CTFont, CFString, UnsafeMutablePointer<Unmanaged<CFString>?>?) -> CFString?](./ctfontcopylocalizedname%28_,_,_%29.md)
  Returns a reference to a localized name for the given font.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretext/ctfontcopypostscriptname(_:))*
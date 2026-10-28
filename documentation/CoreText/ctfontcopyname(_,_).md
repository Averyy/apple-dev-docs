# CTFontCopyName(_:_:)

**Framework**: Core Text  
**Kind**: func  
**Role**: Function

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

```c
extern CFStringRefCTFontCopyName(CTFontRef font, CFStringRef nameKey);
```

## Return Value

The requested name for the font, or `NULL` if the font does not have an entry for the requested name. The Unicode version of the name is preferred, otherwise the first available version is returned.

## Parameters

- `font`: The font reference.
- `nameKey`: The name specifier. See [Name Specifier Constants](./name-specifier-constants.md) for possible values.

## See Also

### Getting Font Names
- [func CTFontCopyPostScriptName(CTFont) -> CFString](./ctfontcopypostscriptname%28_%29.md)
  Returns the PostScript name of the given font.
- [func CTFontCopyFamilyName(CTFont) -> CFString](./ctfontcopyfamilyname%28_%29.md)
  Returns the family name of the given font.
- [func CTFontCopyFullName(CTFont) -> CFString](./ctfontcopyfullname%28_%29.md)
  Returns the full name of the given font.
- [func CTFontCopyDisplayName(CTFont) -> CFString](./ctfontcopydisplayname%28_%29.md)
  Returns the display name of the given font.
- [func CTFontCopyLocalizedName(CTFont, CFString, UnsafeMutablePointer<Unmanaged<CFString>?>?) -> CFString?](./ctfontcopylocalizedname%28_,_,_%29.md)
  Returns a reference to a localized name for the given font.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretext/ctfontcopyname(_:_:))*
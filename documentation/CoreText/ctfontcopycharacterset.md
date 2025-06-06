# CTFontCopyCharacterSet(_:)

**Framework**: Core Text  
**Kind**: func

Returns the Unicode character set of the font.

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
func CTFontCopyCharacterSet(_ font: CTFont) -> CFCharacterSet
```

#### Return Value

A retained reference to the font’s character set.

#### Discussion

The returned character set covers the nominal referenced by the font’s Unicode `'cmap’` table.

## Parameters

- `font`: The font reference.

## See Also

- [func CTFontGetStringEncoding(CTFont) -> CFStringEncoding](ctfontgetstringencoding(_:).md)
  Returns the best string encoding for legacy format support.
- [func CTFontCopySupportedLanguages(CTFont) -> CFArray](ctfontcopysupportedlanguages(_:).md)
  Returns an array of languages supported by the font.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretext/ctfontcopycharacterset(_:))*
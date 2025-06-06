# CTFontGetStringEncoding(_:)

**Framework**: Core Text  
**Kind**: func

Returns the best string encoding for legacy format support.

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
func CTFontGetStringEncoding(_ font: CTFont) -> CFStringEncoding
```

#### Return Value

The best string encoding for the font.

## Parameters

- `font`: The font reference.

## See Also

- [func CTFontCopyCharacterSet(CTFont) -> CFCharacterSet](ctfontcopycharacterset(_:).md)
  Returns the Unicode character set of the font.
- [func CTFontCopySupportedLanguages(CTFont) -> CFArray](ctfontcopysupportedlanguages(_:).md)
  Returns an array of languages supported by the font.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretext/ctfontgetstringencoding(_:))*
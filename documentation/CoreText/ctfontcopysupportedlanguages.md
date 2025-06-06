# CTFontCopySupportedLanguages(_:)

**Framework**: Core Text  
**Kind**: func

Returns an array of languages supported by the font.

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
func CTFontCopySupportedLanguages(_ font: CTFont) -> CFArray
```

#### Return Value

A retained reference to an array of languages supported by the font. The array contains language identifier strings as `CFStringRef` objects. The format of the language identifier conforms to the RFC 3066bis standard.

## Parameters

- `font`: The font reference.

## See Also

- [func CTFontCopyCharacterSet(CTFont) -> CFCharacterSet](ctfontcopycharacterset(_:).md)
  Returns the Unicode character set of the font.
- [func CTFontGetStringEncoding(CTFont) -> CFStringEncoding](ctfontgetstringencoding(_:).md)
  Returns the best string encoding for legacy format support.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretext/ctfontcopysupportedlanguages(_:))*
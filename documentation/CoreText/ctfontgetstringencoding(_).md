# CTFontGetStringEncoding(_:)

**Framework**: Core Text  
**Kind**: func  
**Role**: Function

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

```c
extern CFStringEncoding CTFontGetStringEncoding(CTFontRef font);
```

## Return Value

The best string encoding for the font.

## Parameters

- `font`: The font reference.

## See Also

### Working With Encoding
- [func CTFontCopyCharacterSet(CTFont) -> CFCharacterSet](./ctfontcopycharacterset%28_%29.md)
  Returns the Unicode character set of the font.
- [func CTFontCopySupportedLanguages(CTFont) -> CFArray](./ctfontcopysupportedlanguages%28_%29.md)
  Returns an array of languages supported by the font.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretext/ctfontgetstringencoding(_:))*
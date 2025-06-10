# CFStringBuiltInEncodings

**Framework**: Core Foundation  
**Kind**: enum

Encodings that are built-in on all platforms on which macOS runs.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
enum CFStringBuiltInEncodings
```

## Topics

### Constants
- [CFStringBuiltInEncodings.macRoman](cfstringbuiltinencodings/macroman.md)
  An encoding constant that identifies the Mac Roman encoding.
- [CFStringBuiltInEncodings.windowsLatin1](cfstringbuiltinencodings/windowslatin1.md)
  An encoding constant that identifies the Windows Latin 1 encoding (ANSI codepage 1252).
- [CFStringBuiltInEncodings.isoLatin1](cfstringbuiltinencodings/isolatin1.md)
  An encoding constant that identifies the ISO Latin 1 encoding (ISO 8859-1)
- [CFStringBuiltInEncodings.nextStepLatin](cfstringbuiltinencodings/nextsteplatin.md)
  An encoding constant that identifies the NextStep/OpenStep encoding.
- [CFStringBuiltInEncodings.ASCII](cfstringbuiltinencodings/ascii.md)
  An encoding constant that identifies the ASCII encoding (decimal values 0 through 127).
- [CFStringBuiltInEncodings.unicode](cfstringbuiltinencodings/unicode.md)
  An encoding constant that identifies the Unicode encoding.
- [CFStringBuiltInEncodings.UTF8](cfstringbuiltinencodings/utf8.md)
  An encoding constant that identifies the UTF 8 encoding.
- [CFStringBuiltInEncodings.nonLossyASCII](cfstringbuiltinencodings/nonlossyascii.md)
  An encoding constant that identifies non-lossy ASCII encoding.
- [static var UTF16: CFStringBuiltInEncodings](cfstringbuiltinencodings/utf16.md)
  An encoding constant that identifies kTextEncodingUnicodeDefault + kUnicodeUTF16Format encoding (alias of kCFStringEncodingUnicode).
- [CFStringBuiltInEncodings.UTF16BE](cfstringbuiltinencodings/utf16be.md)
  An encoding constant that identifies kTextEncodingUnicodeDefault + kUnicodeUTF16BEFormat encoding. This constant specifies big-endian byte order.
- [CFStringBuiltInEncodings.UTF16LE](cfstringbuiltinencodings/utf16le.md)
  An encoding constant that identifies kTextEncodingUnicodeDefault + kUnicodeUTF16LEFormat encoding. This constant specifies little-endian byte order.
- [CFStringBuiltInEncodings.UTF32](cfstringbuiltinencodings/utf32.md)
  An encoding constant that identifies kTextEncodingUnicodeDefault + kUnicodeUTF32Format encoding.
- [CFStringBuiltInEncodings.UTF32BE](cfstringbuiltinencodings/utf32be.md)
  An encoding constant that identifies kTextEncodingUnicodeDefault + kUnicodeUTF32BEFormat encoding. This constant specifies big-endian byte order.
- [CFStringBuiltInEncodings.UTF32LE](cfstringbuiltinencodings/utf32le.md)
  An encoding constant that identifies kTextEncodingUnicodeDefault + kUnicodeUTF32LEFormat encoding. This constant specifies little-endian byte order.
### Initializers
- [init?(rawValue: CFStringEncoding)](cfstringbuiltinencodings/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [String Comparison Flags](string-comparison-flags.md)
  Flags that specify how string comparisons are performed.
- [Invalid String Encoding Flag](invalid-string-encoding-flag.md)
  Special value returned from functions to indicate a string encoding that is not supported or recognized by CFString.
- [External String Encodings](external-string-encodings.md)
  `CFStringEncoding` constants for encodings that may be supported by CFString.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfstringbuiltinencodings)*
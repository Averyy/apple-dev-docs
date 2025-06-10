# Unicode.ParseResult

**Framework**: Swift  
**Kind**: enum

The result of attempting to parse a `T` from some input.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.0+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
@frozen
enum ParseResult<T>
```

## Topics

### Enumeration Cases
- [Unicode.ParseResult.emptyInput](unicode/parseresult/emptyinput.md)
  The input was entirely consumed.
- [Unicode.ParseResult.error(length:)](unicode/parseresult/error(length:).md)
  An encoding error was detected.
- [Unicode.ParseResult.valid(_:)](unicode/parseresult/valid(_:).md)
  A `T` was parsed successfully

## Relationships

### Conforms To
- [Sendable](sendable.md)
- [SendableMetatype](sendablemetatype.md)

## See Also

- [protocol UnicodeCodec](unicodecodec.md)
  A Unicode encoding form that translates between Unicode scalar values and form-specific code units.
- [Unicode.ASCII](unicode/ascii.md)
- [Unicode.UTF8](unicode/utf8.md)
- [Unicode.UTF16](unicode/utf16.md)
- [Unicode.UTF32](unicode/utf32.md)
- [enum UnicodeDecodingResult](unicodedecodingresult.md)
  The result of one Unicode decoding step.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/unicode/parseresult)*
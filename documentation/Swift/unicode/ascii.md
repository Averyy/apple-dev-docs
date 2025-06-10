# Unicode.ASCII

**Framework**: Swift  
**Kind**: enum

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
enum ASCII
```

## Topics

### Structures
- [Unicode.ASCII.Parser](unicode/ascii/parser.md)
### Type Aliases
- [Unicode.ASCII.CodeUnit](unicode/ascii/codeunit.md)
  The basic unit of encoding
- [Unicode.ASCII.EncodedScalar](unicode/ascii/encodedscalar.md)
  A valid scalar value as represented in this encoding
- [Unicode.ASCII.ForwardParser](unicode/ascii/forwardparser.md)
  A type that can be used to parse `CodeUnits` into `EncodedScalar`s.
- [Unicode.ASCII.ReverseParser](unicode/ascii/reverseparser.md)
  A type that can be used to parse a reversed sequence of `CodeUnits` into `EncodedScalar`s.
### Type Properties
- [static var encodedReplacementCharacter: Unicode.ASCII.EncodedScalar](unicode/ascii/encodedreplacementcharacter.md)
  A unicode scalar value to be used when repairing encoding/decoding errors, as represented in this encoding.
### Type Methods
- [static func decode(Unicode.ASCII.EncodedScalar) -> Unicode.Scalar](unicode/ascii/decode(_:).md)
  Converts from encoded to encoding-independent representation
- [static func encode(Unicode.Scalar) -> Unicode.ASCII.EncodedScalar?](unicode/ascii/encode(_:).md)
  Converts from encoding-independent to encoded representation, returning `nil` if the scalar can’t be represented in this encoding.
- [static func isASCII(Unicode.ASCII.CodeUnit) -> Bool](unicode/ascii/isascii(_:).md)
  Returns whether the given code unit represents an ASCII scalar
- [static func transcode<FromEncoding>(FromEncoding.EncodedScalar, from: FromEncoding.Type) -> Unicode.ASCII.EncodedScalar?](unicode/ascii/transcode(_:from:).md)
  Converts a scalar from another encoding’s representation, returning `nil` if the scalar can’t be represented in this encoding.

## Relationships

### Conforms To
- [BitwiseCopyable](bitwisecopyable.md)
- [Copyable](copyable.md)
- [Sendable](sendable.md)
- [SendableMetatype](sendablemetatype.md)

## See Also

- [protocol UnicodeCodec](unicodecodec.md)
  A Unicode encoding form that translates between Unicode scalar values and form-specific code units.
- [Unicode.UTF8](unicode/utf8.md)
- [Unicode.UTF16](unicode/utf16.md)
- [Unicode.UTF32](unicode/utf32.md)
- [enum UnicodeDecodingResult](unicodedecodingresult.md)
  The result of one Unicode decoding step.
- [Unicode.ParseResult](unicode/parseresult.md)
  The result of attempting to parse a `T` from some input.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/unicode/ascii)*
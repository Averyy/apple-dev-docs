# Unicode.ASCII

**Framework**: Swift  
**Kind**: enum  
**Role**: Enumeration

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
- [Unicode.ASCII.Parser](./ascii/parser.md)
### Type Aliases
- [Unicode.ASCII.CodeUnit](./ascii/codeunit.md)
  The basic unit of encoding
- [Unicode.ASCII.EncodedScalar](./ascii/encodedscalar.md)
  A valid scalar value as represented in this encoding
- [Unicode.ASCII.ForwardParser](./ascii/forwardparser.md)
  A type that can be used to parse `CodeUnits` into `EncodedScalar`s.
- [Unicode.ASCII.ReverseParser](./ascii/reverseparser.md)
  A type that can be used to parse a reversed sequence of `CodeUnits` into `EncodedScalar`s.
### Type Properties
- [static var encodedReplacementCharacter: Unicode.ASCII.EncodedScalar](./ascii/encodedreplacementcharacter.md)
  A unicode scalar value to be used when repairing encoding/decoding errors, as represented in this encoding.
### Type Methods
- [static func decode(Unicode.ASCII.EncodedScalar) -> Unicode.Scalar](./ascii/decode%28_%29.md)
  Converts from encoded to encoding-independent representation
- [static func encode(Unicode.Scalar) -> Unicode.ASCII.EncodedScalar?](./ascii/encode%28_%29.md)
  Converts from encoding-independent to encoded representation, returning `nil` if the scalar can’t be represented in this encoding.
- [static func isASCII(Unicode.ASCII.CodeUnit) -> Bool](./ascii/isascii%28_%29.md)
  Returns whether the given code unit represents an ASCII scalar
- [static func transcode<FromEncoding>(FromEncoding.EncodedScalar, from: FromEncoding.Type) -> Unicode.ASCII.EncodedScalar?](./ascii/transcode%28_,from%29.md)
  Converts a scalar from another encoding’s representation, returning `nil` if the scalar can’t be represented in this encoding.

## Relationships

### Conforms To
- [BitwiseCopyable](../bitwisecopyable.md)
- [Copyable](../copyable.md)
- [Escapable](../escapable.md)
- [Sendable](../sendable.md)
- [SendableMetatype](../sendablemetatype.md)

## See Also

### Unicode Codecs
- [protocol UnicodeCodec](../unicodecodec.md)
  A Unicode encoding form that translates between Unicode scalar values and form-specific code units.
- [Unicode.UTF8](./utf8.md)
- [Unicode.UTF16](./utf16.md)
- [Unicode.UTF32](./utf32.md)
- [enum UnicodeDecodingResult](../unicodedecodingresult.md)
  The result of one Unicode decoding step.
- [Unicode.ParseResult](./parseresult.md)
  The result of attempting to parse a `T` from some input.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/unicode/ascii)*
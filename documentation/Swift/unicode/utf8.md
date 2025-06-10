# Unicode.UTF8

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
enum UTF8
```

## Topics

### Structures
- [Unicode.UTF8.ForwardParser](unicode/utf8/forwardparser.md)
  A type that can be used to parse `CodeUnits` into `EncodedScalar`s.
- [Unicode.UTF8.ReverseParser](unicode/utf8/reverseparser.md)
  A type that can be used to parse a reversed sequence of `CodeUnits` into `EncodedScalar`s.
- [Unicode.UTF8.ValidationError](unicode/utf8/validationerror.md)
  The kind and location of a UTF-8 encoding error.
### Type Aliases
- [Unicode.UTF8.CodeUnit](unicode/utf8/codeunit.md)
  The basic unit of encoding
- [Unicode.UTF8.EncodedScalar](unicode/utf8/encodedscalar.md)
  A valid scalar value as represented in this encoding
### Type Properties
- [static var encodedReplacementCharacter: Unicode.UTF8.EncodedScalar](unicode/utf8/encodedreplacementcharacter.md)
  A unicode scalar value to be used when repairing encoding/decoding errors, as represented in this encoding.
### Type Methods
- [static func decode(Unicode.UTF8.EncodedScalar) -> Unicode.Scalar](unicode/utf8/decode(_:)-swift.type.method.md)
  Converts from encoded to encoding-independent representation
- [static func encode(Unicode.Scalar) -> Unicode.UTF8.EncodedScalar?](unicode/utf8/encode(_:).md)
  Converts from encoding-independent to encoded representation, returning `nil` if the scalar can’t be represented in this encoding.
- [static func isASCII(Unicode.UTF8.CodeUnit) -> Bool](unicode/utf8/isascii(_:).md)
  Returns whether the given code unit represents an ASCII scalar
- [static func isContinuation(Unicode.UTF8.CodeUnit) -> Bool](unicode/utf8/iscontinuation(_:).md)
  Returns a Boolean value indicating whether the specified code unit is a UTF-8 continuation byte.
- [static func transcode<FromEncoding>(FromEncoding.EncodedScalar, from: FromEncoding.Type) -> Unicode.UTF8.EncodedScalar?](unicode/utf8/transcode(_:from:).md)
  Converts a scalar from another encoding’s representation, returning `nil` if the scalar can’t be represented in this encoding.
- [static func width(Unicode.Scalar) -> Int](unicode/utf8/width(_:).md)
  Returns the number of code units required to encode the given Unicode scalar.
### Default Implementations
- [UnicodeCodec Implementations](unicode/utf8/unicodecodec-implementations.md)

## Relationships

### Conforms To
- [BitwiseCopyable](bitwisecopyable.md)
- [Copyable](copyable.md)
- [Sendable](sendable.md)
- [SendableMetatype](sendablemetatype.md)
- [UnicodeCodec](unicodecodec.md)

## See Also

- [protocol UnicodeCodec](unicodecodec.md)
  A Unicode encoding form that translates between Unicode scalar values and form-specific code units.
- [Unicode.ASCII](unicode/ascii.md)
- [Unicode.UTF16](unicode/utf16.md)
- [Unicode.UTF32](unicode/utf32.md)
- [enum UnicodeDecodingResult](unicodedecodingresult.md)
  The result of one Unicode decoding step.
- [Unicode.ParseResult](unicode/parseresult.md)
  The result of attempting to parse a `T` from some input.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/unicode/utf8)*
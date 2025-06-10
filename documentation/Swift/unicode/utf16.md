# Unicode.UTF16

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
enum UTF16
```

## Topics

### Structures
- [Unicode.UTF16.ForwardParser](unicode/utf16/forwardparser.md)
  A type that can be used to parse `CodeUnits` into `EncodedScalar`s.
- [Unicode.UTF16.ReverseParser](unicode/utf16/reverseparser.md)
  A type that can be used to parse a reversed sequence of `CodeUnits` into `EncodedScalar`s.
### Type Aliases
- [Unicode.UTF16.CodeUnit](unicode/utf16/codeunit.md)
  The basic unit of encoding
- [Unicode.UTF16.EncodedScalar](unicode/utf16/encodedscalar.md)
  A valid scalar value as represented in this encoding
### Type Properties
- [static var encodedReplacementCharacter: Unicode.UTF16.EncodedScalar](unicode/utf16/encodedreplacementcharacter.md)
  A unicode scalar value to be used when repairing encoding/decoding errors, as represented in this encoding.
### Type Methods
- [static func decode(Unicode.UTF16.EncodedScalar) -> Unicode.Scalar](unicode/utf16/decode(_:)-swift.type.method.md)
  Converts from encoded to encoding-independent representation
- [static func encode(Unicode.Scalar) -> Unicode.UTF16.EncodedScalar?](unicode/utf16/encode(_:).md)
  Converts from encoding-independent to encoded representation, returning `nil` if the scalar can’t be represented in this encoding.
- [static func isASCII(Unicode.UTF16.CodeUnit) -> Bool](unicode/utf16/isascii(_:).md)
  Returns whether the given code unit represents an ASCII scalar
- [static func isLeadSurrogate(Unicode.UTF16.CodeUnit) -> Bool](unicode/utf16/isleadsurrogate(_:).md)
  Returns a Boolean value indicating whether the specified code unit is a high-surrogate code unit.
- [static func isSurrogate(Unicode.UTF16.CodeUnit) -> Bool](unicode/utf16/issurrogate(_:).md)
  Returns a Boolean value indicating whether the specified code unit is a high or low surrogate code unit.
- [static func isTrailSurrogate(Unicode.UTF16.CodeUnit) -> Bool](unicode/utf16/istrailsurrogate(_:).md)
  Returns a Boolean value indicating whether the specified code unit is a low-surrogate code unit.
- [static func leadSurrogate(Unicode.Scalar) -> UTF16.CodeUnit](unicode/utf16/leadsurrogate(_:).md)
  Returns the high-surrogate code unit of the surrogate pair representing the specified Unicode scalar.
- [static func trailSurrogate(Unicode.Scalar) -> UTF16.CodeUnit](unicode/utf16/trailsurrogate(_:).md)
  Returns the low-surrogate code unit of the surrogate pair representing the specified Unicode scalar.
- [static func transcode<FromEncoding>(FromEncoding.EncodedScalar, from: FromEncoding.Type) -> Unicode.UTF16.EncodedScalar?](unicode/utf16/transcode(_:from:).md)
  Converts a scalar from another encoding’s representation, returning `nil` if the scalar can’t be represented in this encoding.
- [static func transcodedLength<Input, Encoding>(of: Input, decodedAs: Encoding.Type, repairingIllFormedSequences: Bool) -> (count: Int, isASCII: Bool)?](unicode/utf16/transcodedlength(of:decodedas:repairingillformedsequences:).md)
  Returns the number of UTF-16 code units required for the given code unit sequence when transcoded to UTF-16, and a Boolean value indicating whether the sequence was found to contain only ASCII characters.
- [static func width(Unicode.Scalar) -> Int](unicode/utf16/width(_:).md)
  Returns the number of code units required to encode the given Unicode scalar.
### Default Implementations
- [UnicodeCodec Implementations](unicode/utf16/unicodecodec-implementations.md)

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
- [Unicode.UTF8](unicode/utf8.md)
- [Unicode.UTF32](unicode/utf32.md)
- [enum UnicodeDecodingResult](unicodedecodingresult.md)
  The result of one Unicode decoding step.
- [Unicode.ParseResult](unicode/parseresult.md)
  The result of attempting to parse a `T` from some input.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/unicode/utf16)*
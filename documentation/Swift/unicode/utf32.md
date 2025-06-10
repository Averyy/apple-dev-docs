# Unicode.UTF32

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
enum UTF32
```

## Topics

### Structures
- [Unicode.UTF32.Parser](unicode/utf32/parser.md)
### Operators
- [static func == (Unicode.UTF32, Unicode.UTF32) -> Bool](unicode/utf32/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Instance Properties
- [var hashValue: Int](unicode/utf32/hashvalue.md)
  The hash value.
### Instance Methods
- [func hash(into: inout Hasher)](unicode/utf32/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Type Aliases
- [Unicode.UTF32.CodeUnit](unicode/utf32/codeunit.md)
  The basic unit of encoding
- [Unicode.UTF32.EncodedScalar](unicode/utf32/encodedscalar.md)
  A valid scalar value as represented in this encoding
- [Unicode.UTF32.ForwardParser](unicode/utf32/forwardparser.md)
  A type that can be used to parse `CodeUnits` into `EncodedScalar`s.
- [Unicode.UTF32.ReverseParser](unicode/utf32/reverseparser.md)
  A type that can be used to parse a reversed sequence of `CodeUnits` into `EncodedScalar`s.
### Type Properties
- [static var encodedReplacementCharacter: Unicode.UTF32.EncodedScalar](unicode/utf32/encodedreplacementcharacter.md)
  A unicode scalar value to be used when repairing encoding/decoding errors, as represented in this encoding.
### Type Methods
- [static func decode(Unicode.UTF32.EncodedScalar) -> Unicode.Scalar](unicode/utf32/decode(_:)-swift.type.method.md)
  Converts from encoded to encoding-independent representation
- [static func encode(Unicode.Scalar) -> Unicode.UTF32.EncodedScalar?](unicode/utf32/encode(_:).md)
  Converts from encoding-independent to encoded representation, returning `nil` if the scalar can’t be represented in this encoding.
- [static func isASCII(Unicode.UTF32.CodeUnit) -> Bool](unicode/utf32/isascii(_:).md)
  Returns whether the given code unit represents an ASCII scalar
### Default Implementations
- [Equatable Implementations](unicode/utf32/equatable-implementations.md)
- [UnicodeCodec Implementations](unicode/utf32/unicodecodec-implementations.md)

## Relationships

### Conforms To
- [BitwiseCopyable](bitwisecopyable.md)
- [Copyable](copyable.md)
- [Equatable](equatable.md)
- [Hashable](hashable.md)
- [Sendable](sendable.md)
- [SendableMetatype](sendablemetatype.md)
- [UnicodeCodec](unicodecodec.md)

## See Also

- [protocol UnicodeCodec](unicodecodec.md)
  A Unicode encoding form that translates between Unicode scalar values and form-specific code units.
- [Unicode.ASCII](unicode/ascii.md)
- [Unicode.UTF8](unicode/utf8.md)
- [Unicode.UTF16](unicode/utf16.md)
- [enum UnicodeDecodingResult](unicodedecodingresult.md)
  The result of one Unicode decoding step.
- [Unicode.ParseResult](unicode/parseresult.md)
  The result of attempting to parse a `T` from some input.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/unicode/utf32)*
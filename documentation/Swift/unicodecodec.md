# UnicodeCodec

**Framework**: Swift  
**Kind**: protocol

A Unicode encoding form that translates between Unicode scalar values and form-specific code units.

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
protocol UnicodeCodec : _UnicodeEncoding
```

#### Overview

The `UnicodeCodec` protocol declares methods that decode code unit sequences into Unicode scalar values and encode Unicode scalar values into code unit sequences. The standard library implements codecs for the UTF-8, UTF-16, and UTF-32 encoding schemes as the `UTF8`, `UTF16`, and `UTF32` types, respectively. Use the `Unicode.Scalar` type to work with decoded Unicode scalar values.

## Topics

### Initializers
- [init()](unicodecodec/init.md)
  Creates an instance of the codec.
### Instance Methods
- [func decode<I>(inout I) -> UnicodeDecodingResult](unicodecodec/decode(_:).md)
  Starts or continues decoding a code unit sequence into Unicode scalar values.
### Type Methods
- [static func encode(Unicode.Scalar, into: (Self.CodeUnit) -> Void)](unicodecodec/encode(_:into:).md)
  Encodes a Unicode scalar as a series of code units by calling the given closure on each code unit.

## Relationships

### Conforming Types
- [Unicode.UTF16](unicode/utf16.md)
- [Unicode.UTF32](unicode/utf32.md)
- [Unicode.UTF8](unicode/utf8.md)

## See Also

- [Unicode.ASCII](unicode/ascii.md)
- [Unicode.UTF8](unicode/utf8.md)
- [Unicode.UTF16](unicode/utf16.md)
- [Unicode.UTF32](unicode/utf32.md)
- [enum UnicodeDecodingResult](unicodedecodingresult.md)
  The result of one Unicode decoding step.
- [Unicode.ParseResult](unicode/parseresult.md)
  The result of attempting to parse a `T` from some input.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/unicodecodec)*
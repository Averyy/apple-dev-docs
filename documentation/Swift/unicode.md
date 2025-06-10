# Unicode

**Framework**: Swift  
**Kind**: enum

A namespace for Unicode utilities.

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
enum Unicode
```

## Topics

### Individual Unicode Scalar Values
- [Unicode.Scalar](unicode/scalar.md)
  A Unicode scalar value.
### Unicode Scalar Classifications
- [Unicode.GeneralCategory](unicode/generalcategory.md)
  The most general classification of a Unicode scalar.
- [Unicode.CanonicalCombiningClass](unicode/canonicalcombiningclass.md)
  The classification of a scalar used in the Canonical Ordering Algorithm defined by the Unicode Standard.
- [Unicode.NumericType](unicode/numerictype.md)
  The numeric type of a scalar.
### Unicode Codecs
- [protocol UnicodeCodec](unicodecodec.md)
  A Unicode encoding form that translates between Unicode scalar values and form-specific code units.
- [Unicode.ASCII](unicode/ascii.md)
- [Unicode.UTF8](unicode/utf8.md)
- [Unicode.UTF16](unicode/utf16.md)
- [Unicode.UTF32](unicode/utf32.md)
- [enum UnicodeDecodingResult](unicodedecodingresult.md)
  The result of one Unicode decoding step.
- [Unicode.ParseResult](unicode/parseresult.md)
  The result of attempting to parse a `T` from some input.
### Translation Between Unicode Encodings
- [func transcode<Input, InputEncoding, OutputEncoding>(Input, from: InputEncoding.Type, to: OutputEncoding.Type, stoppingOnError: Bool, into: (OutputEncoding.CodeUnit) -> Void) -> Bool](transcode(_:from:to:stoppingonerror:into:).md)
  Translates the given input from one Unicode encoding to another by calling the given closure.
### Deprecated
- [typealias UnicodeScalar](unicodescalar.md)
- [typealias UTF8](utf8.md)
- [typealias UTF16](utf16.md)
- [typealias UTF32](utf32.md)
### Type Aliases
- [typealias Encoding](unicode/encoding.md)
- [typealias Parser](unicode/parser.md)
- [typealias Version](unicode/version.md)
  A version of the Unicode Standard represented by its major and minor components.

## Relationships

### Conforms To
- [Sendable](sendable.md)
- [SendableMetatype](sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/unicode)*
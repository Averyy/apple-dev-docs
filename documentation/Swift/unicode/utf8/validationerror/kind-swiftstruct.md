# Unicode.UTF8.ValidationError.Kind

**Framework**: Swift  
**Kind**: struct

The kind of encoding error encountered during validation

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)
- watchOS 26.0+ (Beta)

## Declaration

```swift
@frozen
struct Kind
```

## Topics

### Initializers
- [init?(rawValue: UInt8)](unicode/utf8/validationerror/kind-swift.struct/init(rawvalue:).md)
  Creates a new instance with the specified raw value.
### Instance Properties
- [var rawValue: UInt8](unicode/utf8/validationerror/kind-swift.struct/rawvalue-swift.property.md)
  The corresponding value of the raw type.
### Type Aliases
- [Unicode.UTF8.ValidationError.Kind.RawValue](unicode/utf8/validationerror/kind-swift.struct/rawvalue-swift.typealias.md)
  The raw type that can be used to represent all values of the conforming type.
### Type Properties
- [static var invalidNonSurrogateCodePointByte: Unicode.UTF8.ValidationError.Kind](unicode/utf8/validationerror/kind-swift.struct/invalidnonsurrogatecodepointbyte.md)
  A byte in an invalid, non-surrogate code point (`>U+10FFFF`) sequence
- [static var overlongEncodingByte: Unicode.UTF8.ValidationError.Kind](unicode/utf8/validationerror/kind-swift.struct/overlongencodingbyte.md)
  A byte in an overlong encoding sequence
- [static var surrogateCodePointByte: Unicode.UTF8.ValidationError.Kind](unicode/utf8/validationerror/kind-swift.struct/surrogatecodepointbyte.md)
  A byte in a surrogate code point (`U+D800..U+DFFF`) sequence
- [static var truncatedScalar: Unicode.UTF8.ValidationError.Kind](unicode/utf8/validationerror/kind-swift.struct/truncatedscalar.md)
  A multi-byte sequence that is the start of a valid multi-byte scalar but is cut off before ending correctly
- [static var unexpectedContinuationByte: Unicode.UTF8.ValidationError.Kind](unicode/utf8/validationerror/kind-swift.struct/unexpectedcontinuationbyte.md)
  A continuation byte (`10xxxxxx`) outside of a multi-byte sequence
### Default Implementations
- [CustomStringConvertible Implementations](unicode/utf8/validationerror/kind-swift.struct/customstringconvertible-implementations.md)
- [Equatable Implementations](unicode/utf8/validationerror/kind-swift.struct/equatable-implementations.md)
- [RawRepresentable Implementations](unicode/utf8/validationerror/kind-swift.struct/rawrepresentable-implementations.md)

## Relationships

### Conforms To
- [BitwiseCopyable](bitwisecopyable.md)
- [Copyable](copyable.md)
- [CustomStringConvertible](customstringconvertible.md)
- [Equatable](equatable.md)
- [Error](error.md)
- [Hashable](hashable.md)
- [RawRepresentable](rawrepresentable.md)
- [Sendable](sendable.md)
- [SendableMetatype](sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/unicode/utf8/validationerror/kind-swift.struct)*
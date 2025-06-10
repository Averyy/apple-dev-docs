# Unicode.UTF8.ValidationError

**Framework**: Swift  
**Kind**: struct

The kind and location of a UTF-8 encoding error.

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
struct ValidationError
```

#### Overview

Valid UTF-8 is represented by this table:

```swift
╔════════════════════╦════════╦════════╦════════╦════════╗
║    Scalar value    ║ Byte 0 ║ Byte 1 ║ Byte 2 ║ Byte 3 ║
╠════════════════════╬════════╬════════╬════════╬════════╣
║ U+0000..U+007F     ║ 00..7F ║        ║        ║        ║
║ U+0080..U+07FF     ║ C2..DF ║ 80..BF ║        ║        ║
║ U+0800..U+0FFF     ║ E0     ║ A0..BF ║ 80..BF ║        ║
║ U+1000..U+CFFF     ║ E1..EC ║ 80..BF ║ 80..BF ║        ║
║ U+D000..U+D7FF     ║ ED     ║ 80..9F ║ 80..BF ║        ║
║ U+E000..U+FFFF     ║ EE..EF ║ 80..BF ║ 80..BF ║        ║
║ U+10000..U+3FFFF   ║ F0     ║ 90..BF ║ 80..BF ║ 80..BF ║
║ U+40000..U+FFFFF   ║ F1..F3 ║ 80..BF ║ 80..BF ║ 80..BF ║
║ U+100000..U+10FFFF ║ F4     ║ 80..8F ║ 80..BF ║ 80..BF ║
╚════════════════════╩════════╩════════╩════════╩════════╝
```

##### Classifying Errors

An  is when a continuation byte (`10xxxxxx`) occurs in a position that should be the start of a new scalar value. Unexpected continuations can often occur when the input contains arbitrary data instead of textual content. An unexpected continuation at the start of input might mean that the input was not correctly sliced along scalar boundaries or that it does not contain UTF-8.

A  is a multi-byte sequence that is the start of a valid multi-byte scalar but is cut off before ending correctly. A truncated scalar at the end of the input might mean that only part of the entire input was received.

A  (`U+D800..U+DFFF`) is invalid UTF-8. Surrogate code points are used by UTF-16 to encode scalars in the supplementary planes. Their presence may mean the input was encoded in a different 8-bit encoding, such as CESU-8, WTF-8, or Java’s Modified UTF-8.

An  is any code point higher than `U+10FFFF`. This can often occur when the input is arbitrary data instead of textual content.

An  occurs when a scalar value that could have been encoded using fewer bytes is encoded in a longer byte sequence. Overlong encodings are invalid UTF-8 and can lead to security issues if not correctly detected:

- https://nvd.nist.gov/vuln/detail/CVE-2008-2938
- https://nvd.nist.gov/vuln/detail/CVE-2000-0884

An overlong encoding of `NUL`, `0xC0 0x80`, is used in Java’s Modified UTF-8 but is invalid UTF-8. Overlong encoding errors often catch attempts to bypass security measures.

##### Reporting the Range of the Error

The range of the error reported follows the  algorithm in which each error is either one byte long or ends before the first byte that is disallowed. See “U+FFFD Substitution of Maximal Subparts” in the Unicode Standard. Unicode started recommending this algorithm in version 6 and is adopted by the W3C.

The maximal subpart algorithm will produce a single multi-byte range for a truncated scalar (a multi-byte sequence that is the start of a valid multi-byte scalar but is cut off before ending correctly). For all other errors (including overlong encodings, surrogates, and invalid code points), it will produce an error per byte.

// FIXME: without a checkAllErrors, we don’t have these classification distinctions, should we drop it, ensure we will do it, or what?

Since overlong encodings, surrogates, and invalid code points are erroneous by the second byte (at the latest), the above definition produces the same ranges as defining such a sequence as a truncated scalar error followed by unexpected continuation byte errors. The more semantically-rich classification is reported.

For example, a surrogate count point sequence `ED A0 80` will be reported as three `.surrogateCodePointByte` errors rather than a `.truncatedScalar` followed by two `.unexpectedContinuationByte` errors.

Other commonly reported error ranges can be constructed from this result. For example, PEP 383’s error-per-byte can be constructed by mapping over the reported range. Similarly, constructing a single error for the longest invalid byte range can be constructed by joining adjacent error ranges.

```swift
╔═════════════════╦══════╦═════╦═════╦═════╦═════╦═════╦═════╦══════╗
║                 ║  61  ║ F1  ║ 80  ║ 80  ║ E1  ║ 80  ║ C2  ║  62  ║
╠═════════════════╬══════╬═════╬═════╬═════╬═════╬═════╬═════╬══════╣
║ Longest range   ║ U+61 ║ err ║     ║     ║     ║     ║     ║ U+62 ║
║ Maximal subpart ║ U+61 ║ err ║     ║     ║ err ║     ║ err ║ U+62 ║
║ Error per byte  ║ U+61 ║ err ║ err ║ err ║ err ║ err ║ err ║ U+62 ║
╚═════════════════╩══════╩═════╩═════╩═════╩═════╩═════╩═════╩══════╝
```

## Topics

### Structures
- [Unicode.UTF8.ValidationError.Kind](unicode/utf8/validationerror/kind-swift.struct.md)
  The kind of encoding error encountered during validation
### Operators
- [static func == (Unicode.UTF8.ValidationError, Unicode.UTF8.ValidationError) -> Bool](unicode/utf8/validationerror/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Initializers
- [init(Unicode.UTF8.ValidationError.Kind, Range<Int>)](unicode/utf8/validationerror/init(_:_:).md)
- [init(Unicode.UTF8.ValidationError.Kind, at: Int)](unicode/utf8/validationerror/init(_:at:).md)
### Instance Properties
- [var byteOffsets: Range<Int>](unicode/utf8/validationerror/byteoffsets.md)
  The range of offsets into our input containing the error
- [var hashValue: Int](unicode/utf8/validationerror/hashvalue.md)
  The hash value.
- [var kind: Unicode.UTF8.ValidationError.Kind](unicode/utf8/validationerror/kind-swift.property.md)
  The kind of encoding error
### Instance Methods
- [func hash(into: inout Hasher)](unicode/utf8/validationerror/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Default Implementations
- [CustomStringConvertible Implementations](unicode/utf8/validationerror/customstringconvertible-implementations.md)
- [Equatable Implementations](unicode/utf8/validationerror/equatable-implementations.md)

## Relationships

### Conforms To
- [Copyable](copyable.md)
- [CustomStringConvertible](customstringconvertible.md)
- [Equatable](equatable.md)
- [Error](error.md)
- [Hashable](hashable.md)
- [Sendable](sendable.md)
- [SendableMetatype](sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/unicode/utf8/validationerror)*
# UTF8Span

**Framework**: Swift  
**Kind**: struct

A borrowed view into contiguous memory that contains validly-encoded UTF-8 code units.

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
struct UTF8Span
```

## Topics

### Structures
- [UTF8Span.CharacterIterator](utf8span/characteriterator.md)
  Iterate the `Character` contents of a `UTF8Span`.
- [UTF8Span.UnicodeScalarIterator](utf8span/unicodescalariterator.md)
  Iterate the `Unicode.Scalar`s  contents of a `UTF8Span`.
### Initializers
- [init(unchecked: Span<UInt8>, isKnownASCII: Bool)](utf8span/init(unchecked:isknownascii:).md)
  Creates a UTF8Span, bypassing safety and security checks. The caller must guarantee that `codeUnits` contains validly-encoded UTF-8, or else undefined behavior may result upon use. If `isKnownASCII: true is passed`, the contents must be ASCII, or else undefined behavior may result upon use.
- [init(validating: consuming Span<UInt8>) throws(UTF8.ValidationError)](utf8span/init(validating:).md)
  Creates a UTF8Span containing `codeUnits`. Validates that the input is valid UTF-8, otherwise throws an error.
### Instance Properties
- [var count: Int](utf8span/count.md)
- [var isEmpty: Bool](utf8span/isempty.md)
- [var isKnownASCII: Bool](utf8span/isknownascii.md)
  Returns whether contents are known to be all-ASCII. A return value of `true` means that all code units are ASCII. A return value of `false` means there  be non-ASCII content.
- [var isKnownNFC: Bool](utf8span/isknownnfc.md)
  Returns whether the contents are known to be NFC. This is not always checked at initialization time and is set by `checkForNFC`.
- [var span: Span<UInt8>](utf8span/span.md)
### Instance Methods
- [func bytesEqual(to: some Sequence<UInt8>) -> Bool](utf8span/bytesequal(to:).md)
  Whether this span has the same bytes as `other`.
- [func charactersEqual(to: some Sequence<Character>) -> Bool](utf8span/charactersequal(to:).md)
  Whether this span has the same `Character`s as `other`.
- [func checkForASCII() -> Bool](utf8span/checkforascii.md)
  Do a scan checking for whether the contents are all-ASCII.
- [func checkForNFC(quickCheck: Bool) -> Bool](utf8span/checkfornfc(quickcheck:).md)
  Do a scan checking for whether the contents are in Normal Form C. When the contents are in NFC, canonical equivalence checks are much faster.
- [func isCanonicallyEquivalent(to: UTF8Span) -> Bool](utf8span/iscanonicallyequivalent(to:).md)
  Whether `self` is equivalent to `other` under Unicode Canonical Equivalence.
- [func isCanonicallyLessThan(UTF8Span) -> Bool](utf8span/iscanonicallylessthan(_:).md)
  Whether `self` orders less than `other` under Unicode Canonical Equivalence using normalized code-unit order (in NFC).
- [func makeCharacterIterator() -> UTF8Span.CharacterIterator](utf8span/makecharacteriterator.md)
  Returns an iterator that will construct `Character`s from the underlying UTF-8 content.
- [func makeUnicodeScalarIterator() -> UTF8Span.UnicodeScalarIterator](utf8span/makeunicodescalariterator.md)
  Returns an iterator that will decode the code units into `Unicode.Scalar`s.
- [func unicodeScalarsEqual(to: some Sequence<Unicode.Scalar>) -> Bool](utf8span/unicodescalarsequal(to:).md)
  Whether this span has the same `Unicode.Scalar`s as `other`.

## Relationships

### Conforms To
- [BitwiseCopyable](bitwisecopyable.md)

## See Also

- [struct Span](span.md)
  `Span<Element>` represents a contiguous region of memory which contains initialized instances of `Element`.
- [struct RawSpan](rawspan.md)
  `RawSpan` represents a contiguous region of memory which contains initialized bytes.
- [struct OutputSpan](outputspan.md)
- [struct MutableSpan](mutablespan.md)
- [struct MutableRawSpan](mutablerawspan.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/utf8span)*
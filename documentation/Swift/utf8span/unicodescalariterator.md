# UTF8Span.UnicodeScalarIterator

**Framework**: Swift  
**Kind**: struct

Iterate the `Unicode.Scalar`s  contents of a `UTF8Span`.

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
struct UnicodeScalarIterator
```

#### Overview

: Examples

## Topics

### Initializers
- [init(UTF8Span)](utf8span/unicodescalariterator/init(_:).md)
### Instance Properties
- [let codeUnits: UTF8Span](utf8span/unicodescalariterator/codeunits.md)
- [var currentCodeUnitOffset: Int](utf8span/unicodescalariterator/currentcodeunitoffset.md)
  The byte offset of the start of the next scalar. This is always scalar-aligned.
### Instance Methods
- [func next() -> Unicode.Scalar?](utf8span/unicodescalariterator/next.md)
  Decode and return the scalar starting at `currentCodeUnitOffset`. After the function returns, `currentCodeUnitOffset` holds the position at the end of the returned scalar, which is also the start of the next scalar.
- [func prefix() -> UTF8Span](utf8span/unicodescalariterator/prefix.md)
  Returns the UTF8Span containing all the content up to the iterator’s current position.
- [func previous() -> Unicode.Scalar?](utf8span/unicodescalariterator/previous.md)
  Decode and return the scalar ending at `currentCodeUnitOffset`. After the function returns, `currentCodeUnitOffset` holds the position at the start of the returned scalar, which is also the end of the previous scalar.
- [func reset(roundingBackwardsFrom: Int)](utf8span/unicodescalariterator/reset(roundingbackwardsfrom:).md)
  Reset to the nearest scalar-aligned code unit offset `<= i`.
- [func reset(roundingForwardsFrom: Int)](utf8span/unicodescalariterator/reset(roundingforwardsfrom:).md)
  Reset to the nearest scalar-aligned code unit offset `>= i`.
- [func reset(toUnchecked: Int)](utf8span/unicodescalariterator/reset(tounchecked:).md)
  Reset this iterator to `codeUnitOffset`, skipping  safety checks (including bounds checks).
- [func skipBack() -> Int](utf8span/unicodescalariterator/skipback.md)
  Move `codeUnitOffset` to the start of the previous scalar, without decoding it.
- [func skipBack(by: Int) -> Int](utf8span/unicodescalariterator/skipback(by:).md)
  Move `codeUnitOffset` to the start of the previous `n` scalars, without decoding them.
- [func skipForward() -> Int](utf8span/unicodescalariterator/skipforward.md)
  Advance `codeUnitOffset` to the end of the current scalar, without decoding it.
- [func skipForward(by: Int) -> Int](utf8span/unicodescalariterator/skipforward(by:).md)
  Advance `codeUnitOffset` to the end of `n` scalars, without decoding them.
- [func suffix() -> UTF8Span](utf8span/unicodescalariterator/suffix.md)
  Returns the UTF8Span containing all the content after the iterator’s current position.

## Relationships

### Conforms To
- [BitwiseCopyable](bitwisecopyable.md)
- [Copyable](copyable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/utf8span/unicodescalariterator)*
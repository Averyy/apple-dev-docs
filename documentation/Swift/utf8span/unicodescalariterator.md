# UTF8Span.UnicodeScalarIterator

**Framework**: Swift  
**Kind**: struct  
**Role**: Structure

Iterate the `Unicode.Scalar`s contents of a `UTF8Span`.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
@frozen
struct UnicodeScalarIterator
```

## Overview

```swift
func printScalarValues(_ string: borrowing String) {
    var iterator = string.utf8Span.makeUnicodeScalarIterator()
    while let scalar = iterator.next() {
        print(scalar.escaped(asASCII: true))
    }
}

let string = "A🎉"
printScalarValues(string)
// Prints "A"
// Prints "\u{0001F389}"
```

## Topics

### Initializers
- [init(UTF8Span)](./unicodescalariterator/init%28_%29.md)
### Instance Properties
- [let codeUnits: UTF8Span](./unicodescalariterator/codeunits.md)
- [var currentCodeUnitOffset: Int](./unicodescalariterator/currentcodeunitoffset.md)
  The byte offset of the start of the next scalar. This is always scalar-aligned.
### Instance Methods
- [func next() -> Unicode.Scalar?](./unicodescalariterator/next%28%29.md)
  Decode and return the scalar starting at `currentCodeUnitOffset`. After the function returns, `currentCodeUnitOffset` holds the position at the end of the returned scalar, which is also the start of the next scalar.
- [func prefix() -> UTF8Span](./unicodescalariterator/prefix%28%29.md)
  Returns the UTF8Span containing all the content up to the iterator’s current position.
- [func previous() -> Unicode.Scalar?](./unicodescalariterator/previous%28%29.md)
  Decode and return the scalar ending at `currentCodeUnitOffset`. After the function returns, `currentCodeUnitOffset` holds the position at the start of the returned scalar, which is also the end of the previous scalar.
- [func reset(roundingBackwardsFrom: Int)](./unicodescalariterator/reset%28roundingbackwardsfrom%29.md)
  Reset to the nearest scalar-aligned code unit offset `<= i`.
- [func reset(roundingForwardsFrom: Int)](./unicodescalariterator/reset%28roundingforwardsfrom%29.md)
  Reset to the nearest scalar-aligned code unit offset `>= i`.
- [func reset(toUnchecked: Int)](./unicodescalariterator/reset%28tounchecked%29.md)
  Reset this iterator to `codeUnitOffset`, skipping *all* safety checks (including bounds checks).
- [func skipBack() -> Int](./unicodescalariterator/skipback%28%29.md)
  Move `currentCodeUnitOffset` to the start of the previous scalar, without decoding it.
- [func skipBack(by: Int) -> Int](./unicodescalariterator/skipback%28by%29.md)
  Move `currentCodeUnitOffset` to the start of the previous `n` scalars, without decoding them.
- [func skipForward() -> Int](./unicodescalariterator/skipforward%28%29.md)
  Advance `currentCodeUnitOffset` to the end of the current scalar, without decoding it.
- [func skipForward(by: Int) -> Int](./unicodescalariterator/skipforward%28by%29.md)
  Advance `currentCodeUnitOffset` to the end of `n` scalars, without decoding them.
- [func suffix() -> UTF8Span](./unicodescalariterator/suffix%28%29.md)
  Returns the UTF8Span containing all the content after the iterator’s current position.

## Relationships

### Conforms To
- [BitwiseCopyable](../bitwisecopyable.md)
- [Copyable](../copyable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/utf8span/unicodescalariterator)*
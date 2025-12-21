# UTF8Span.CharacterIterator

**Framework**: Swift  
**Kind**: struct

Iterate the `Character` contents of a `UTF8Span`.

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
struct CharacterIterator
```

## Topics

### Initializers
- [init(UTF8Span)](utf8span/characteriterator/init(_:).md)
### Instance Properties
- [let codeUnits: UTF8Span](utf8span/characteriterator/codeunits.md)
- [var currentCodeUnitOffset: Int](utf8span/characteriterator/currentcodeunitoffset.md)
  The byte offset of the start of the next `Character`. This is always scalar-aligned. It is always `Character`-aligned relative to the last call to `reset` (or the start of the span if not called).
### Instance Methods
- [func next() -> Character?](utf8span/characteriterator/next.md)
  Return the `Character` starting at `currentCodeUnitOffset`. After the function returns, `currentCodeUnitOffset` holds the position at the end of the `Character`, which is also the start of the next `Character`.
- [func prefix() -> UTF8Span](utf8span/characteriterator/prefix.md)
  Returns the UTF8Span containing all the content up to the iterator’s current position.
- [func previous() -> Character?](utf8span/characteriterator/previous.md)
  Return the `Character` ending at `currentCodeUnitOffset`. After the function returns, `currentCodeUnitOffset` holds the position at the start of the returned `Character`, which is also the end of the previous `Character`.
- [func reset(roundingBackwardsFrom: Int)](utf8span/characteriterator/reset(roundingbackwardsfrom:).md)
  Reset to the nearest character-aligned position `<= i`.
- [func reset(roundingForwardsFrom: Int)](utf8span/characteriterator/reset(roundingforwardsfrom:).md)
  Reset to the nearest character-aligned position `>= i`.
- [func reset(toUnchecked: Int)](utf8span/characteriterator/reset(tounchecked:).md)
  Reset this iterator to `codeUnitOffset`, skipping  safety checks.
- [func skipBack() -> Int](utf8span/characteriterator/skipback.md)
  Move `codeUnitOffset` to the start of the previous `Character`, without constructing it.
- [func skipBack(by: Int) -> Int](utf8span/characteriterator/skipback(by:).md)
  Move `codeUnitOffset` to the start of the previous `n` `Character`s, without constructing them.
- [func skipForward() -> Int](utf8span/characteriterator/skipforward.md)
  Advance `codeUnitOffset` to the end of the current `Character`, without constructing it.
- [func skipForward(by: Int) -> Int](utf8span/characteriterator/skipforward(by:).md)
  Advance `codeUnitOffset` to the end of `n` `Characters`, without constructing them.
- [func suffix() -> UTF8Span](utf8span/characteriterator/suffix.md)
  Returns the UTF8Span containing all the content after the iterator’s current position.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/utf8span/characteriterator)*
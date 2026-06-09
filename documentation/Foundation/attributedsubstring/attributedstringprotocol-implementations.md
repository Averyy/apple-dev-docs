# AttributedStringProtocol Implementations

**Framework**: Foundation

## Topics

### Instance Properties
- [var characters: AttributedString.CharacterView](attributedsubstring/characters.md)
  The characters of the attributed string, as a view into the underlying string.
- [var endIndex: AttributedString.Index](attributedsubstring/endindex.md)
  A substring’s past-the-end position — the position one greater than the last valid subscript argument.
- [var runs: AttributedString.Runs](attributedsubstring/runs.md)
  The attributed runs of the attributed string, as a view into the underlying string.
- [var startIndex: AttributedString.Index](attributedsubstring/startindex.md)
  The position of the first character in a nonempty attributed substring.
- [var unicodeScalars: AttributedString.UnicodeScalarView](attributedsubstring/unicodescalars.md)
  The Unicode scalars of the attributed string, as a view into the underlying string.
- [var utf16: AttributedString.UTF16View](attributedsubstring/utf16.md)
  A view of the attributed substring’s contents as a collection of UTF-16 code units.
- [var utf8: AttributedString.UTF8View](attributedsubstring/utf8.md)
  A view of the attributed substring’s contents as a collection of UTF-8 code units.
### Subscripts
- [subscript<K>(K.Type) -> K.Value?](attributedsubstring/subscript(_:)-2hp64.md)
  Returns an attribute value that corresponds to an attributed string key.
- [subscript(some RangeExpression<AttributedString.Index>) -> AttributedSubstring](attributedsubstring/subscript(_:)-96fey.md)
  Returns a substring of the attributed substring that a range indicates.
- [subscript<K>(dynamicMember _: KeyPath<AttributeDynamicLookup, K>) -> K.Value?](attributedsubstring/subscript(dynamicmember:)-3o8o1.md)
  Returns an attribute value that a key path indicates.
- [subscript<S>(dynamicMember _: KeyPath<AttributeScopes, S.Type>) -> ScopedAttributeContainer<S>](attributedsubstring/subscript(dynamicmember:)-548k0.md)
  Returns a scoped attribute container that a key path indicates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/attributedsubstring/attributedstringprotocol-implementations)*
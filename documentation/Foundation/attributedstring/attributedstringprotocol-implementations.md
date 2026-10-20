# AttributedStringProtocol Implementations

**Framework**: Foundation  
**Role**: API Collection

## Topics

### Instance Properties
- [var characters: AttributedString.CharacterView](./characters.md)
  The characters of the attributed string, as a view into the underlying string.
- [var endIndex: AttributedString.Index](./endindex.md)
  The string’s past-the-end position — the position one greater than the last valid subscript argument.
- [var runs: AttributedString.Runs](./runs-swift.property.md)
  The attributed runs of the attributed string, as a view into the underlying string.
- [var startIndex: AttributedString.Index](./startindex.md)
  The position of the first character in a nonempty attributed string.
- [var unicodeScalars: AttributedString.UnicodeScalarView](./unicodescalars.md)
  The Unicode scalars of the attributed string, as a view into the underlying string.
- [var utf16: AttributedString.UTF16View](./utf16.md)
  A view of the attributed string’s contents as a collection of UTF-16 code units.
- [var utf8: AttributedString.UTF8View](./utf8.md)
  A view of the attributed string’s contents as a collection of UTF-8 code units.
### Subscripts
- [subscript(some RangeExpression<AttributedString.Index>) -> AttributedSubstring](./subscript%28_%29-2vqsz.md)
  Returns a substring of the attributed string using a range to indicate the substring bounds.
- [subscript<K>(dynamicMember _: KeyPath<AttributeDynamicLookup, K>) -> K.Value?](./subscript%28dynamicmember%29-34zdf.md)
  Returns an attribute value that a key path indicates.
- [subscript<S>(dynamicMember _: KeyPath<AttributeScopes, S.Type>) -> ScopedAttributeContainer<S>](./subscript%28dynamicmember%29-9modq.md)
  Returns a scoped attribute container that a key path indicates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/attributedstring/attributedstringprotocol-implementations)*
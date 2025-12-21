# DiscontiguousAttributedSubstring

**Framework**: Foundation  
**Kind**: struct

A discontiguous portion of an attributed string.

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
@dynamicMemberLookup
struct DiscontiguousAttributedSubstring
```

## Topics

### Instance Properties
- [var base: AttributedString](discontiguousattributedsubstring/base.md)
  The underlying attributed string that the discontiguous attributed substring derives from.
- [var characters: DiscontiguousSlice<AttributedString.CharacterView>](discontiguousattributedsubstring/characters.md)
  The characters of the discontiguous attributed string, as a view into the underlying string.
- [var runs: AttributedString.Runs](discontiguousattributedsubstring/runs.md)
  The attributed runs of the discontiguous attributed string, as a view into the underlying string.
- [var unicodeScalars: DiscontiguousSlice<AttributedString.UnicodeScalarView>](discontiguousattributedsubstring/unicodescalars.md)
  The Unicode scalars of the discontiguous attributed string, as a view into the underlying string.
### Subscripts
- [subscript<K>(K.Type) -> K.Value?](discontiguousattributedsubstring/subscript(_:)-1bcls.md)
  Returns an attribute value that corresponds to an attributed string key.
- [subscript(some RangeExpression<AttributedString.Index>) -> DiscontiguousAttributedSubstring](discontiguousattributedsubstring/subscript(_:)-6j670.md)
  Returns a discontiguous substring of this discontiguous attributed string using a range to indicate the discontiguous substring bounds.
- [subscript(RangeSet<AttributedString.Index>) -> DiscontiguousAttributedSubstring](discontiguousattributedsubstring/subscript(_:)-6p2b.md)
  Returns a discontiguous substring of this discontiguous attributed string using a set of ranges to indicate the discontiguous substring bounds.
- [subscript<K>(dynamicMember _: KeyPath<AttributeDynamicLookup, K>) -> K.Value?](discontiguousattributedsubstring/subscript(dynamicmember:)-5i1c9.md)
  Returns an attribute value that a key path indicates.
- [subscript<S>(dynamicMember _: KeyPath<AttributeScopes, S.Type>) -> ScopedAttributeContainer<S>](discontiguousattributedsubstring/subscript(dynamicmember:)-89pug.md)
  Returns a scoped attribute container that a key path indicates.

## Relationships

### Conforms To
- [AttributedStringAttributeMutation](attributedstringattributemutation.md)
- [Copyable](../Swift/Copyable.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/discontiguousattributedsubstring)*
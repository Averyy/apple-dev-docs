# DiscontiguousAttributedSubstring

**Framework**: Foundation  
**Kind**: struct

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 1.0+
- watchOS 26.0+ (Beta)

## Declaration

```swift
@dynamicMemberLookup
struct DiscontiguousAttributedSubstring
```

## Topics

### Instance Properties
- [var base: AttributedString](discontiguousattributedsubstring/base.md)
- [var characters: DiscontiguousSlice<AttributedString.CharacterView>](discontiguousattributedsubstring/characters.md)
- [var runs: AttributedString.Runs](discontiguousattributedsubstring/runs.md)
- [var unicodeScalars: DiscontiguousSlice<AttributedString.UnicodeScalarView>](discontiguousattributedsubstring/unicodescalars.md)
### Subscripts
- [subscript<K>(K.Type) -> K.Value?](discontiguousattributedsubstring/subscript(_:)-1bcls.md)
- [subscript(some RangeExpression<AttributedString.Index>) -> DiscontiguousAttributedSubstring](discontiguousattributedsubstring/subscript(_:)-6j670.md)
- [subscript(RangeSet<AttributedString.Index>) -> DiscontiguousAttributedSubstring](discontiguousattributedsubstring/subscript(_:)-6p2b.md)
- [subscript<K>(dynamicMember _: KeyPath<AttributeDynamicLookup, K>) -> K.Value?](discontiguousattributedsubstring/subscript(dynamicmember:)-5i1c9.md)
- [subscript<S>(dynamicMember _: KeyPath<AttributeScopes, S.Type>) -> ScopedAttributeContainer<S>](discontiguousattributedsubstring/subscript(dynamicmember:)-89pug.md)

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
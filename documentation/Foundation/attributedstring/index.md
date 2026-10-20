# AttributedString.Index

**Framework**: Foundation  
**Kind**: struct  
**Role**: Structure

A type that represents the position of a character or code unit within an attributed string.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
struct Index
```

## Topics

### Initializers
- [init?<S>(String.Index, within: S)](./index/init%28_,within%29.md)
### Instance Methods
- [func isValid(within: DiscontiguousAttributedSubstring) -> Bool](./index/isvalid%28within%29-6wjr6.md)
  Indicates whether the index is valid for use with the provided discontiguous attributed string.
- [func isValid(within: some AttributedStringProtocol) -> Bool](./index/isvalid%28within%29-8fw50.md)
  Indicates whether the index is valid for use with the provided attributed string.

## Relationships

### Conforms To
- [Comparable](../../Swift/comparable.md)
- [Equatable](../../Swift/equatable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Modifying an Attributed String
- [func insert(some AttributedStringProtocol, at: AttributedString.Index)](./insert%28_,at%29.md)
  Inserts the specified string at a specific index in the attributed string.
- [func removeSubrange(some RangeExpression<AttributedString.Index>)](./removesubrange%28_%29.md)
  Removes a range of characters from the attributed string.
- [func replaceSubrange(some RangeExpression<AttributedString.Index>, with: some AttributedStringProtocol)](./replacesubrange%28_,with%29.md)
  Replaces the contents in a range of the attributed string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/attributedstring/index)*
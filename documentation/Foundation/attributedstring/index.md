# AttributedString.Index

**Framework**: Foundation  
**Kind**: struct

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
- [init?<S>(String.Index, within: S)](attributedstring/index/init(_:within:).md)
### Instance Methods
- [func isValid(within: DiscontiguousAttributedSubstring) -> Bool](attributedstring/index/isvalid(within:)-6wjr6.md)
  Indicates whether the index is valid for use with the provided discontiguous attributed string.
- [func isValid(within: some AttributedStringProtocol) -> Bool](attributedstring/index/isvalid(within:)-8fw50.md)
  Indicates whether the index is valid for use with the provided attributed string.

## Relationships

### Conforms To
- [Comparable](../Swift/Comparable.md)
- [Equatable](../Swift/Equatable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [func insert(some AttributedStringProtocol, at: AttributedString.Index)](attributedstring/insert(_:at:).md)
  Inserts the specified string at a specific index in the attributed string.
- [func removeSubrange(some RangeExpression<AttributedString.Index>)](attributedstring/removesubrange(_:).md)
  Removes a range of characters from the attributed string.
- [func replaceSubrange(some RangeExpression<AttributedString.Index>, with: some AttributedStringProtocol)](attributedstring/replacesubrange(_:with:).md)
  Replaces the contents in a range of the attributed string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/attributedstring/index)*
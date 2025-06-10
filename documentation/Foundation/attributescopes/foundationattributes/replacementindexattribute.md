# AttributeScopes.FoundationAttributes.ReplacementIndexAttribute

**Framework**: Foundation  
**Kind**: enum

A type for using a replacement index as an attribute.

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
@frozen
enum ReplacementIndexAttribute
```

#### Overview

When you use the [`applyReplacementIndexAttribute`](attributedstring/formattingoptions/applyreplacementindexattribute.md) formatting option, the resulting formatted string uses this attribute to mark the location of replacement strings. This allows you to relate ranges to replacements even if localizers change the word order in format strings.

## Relationships

### Conforms To
- [AttributedStringKey](attributedstringkey.md)
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Copyable](../Swift/Copyable.md)
- [DecodableAttributedStringKey](decodableattributedstringkey.md)
- [EncodableAttributedStringKey](encodableattributedstringkey.md)

## See Also

- [let replacementIndex: AttributeScopes.FoundationAttributes.ReplacementIndexAttribute](attributescopes/foundationattributes/replacementindex.md)
  A property for accessing a replacement index attribute.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/attributescopes/foundationattributes/replacementindexattribute)*
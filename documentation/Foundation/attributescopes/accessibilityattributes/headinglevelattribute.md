# AttributeScopes.AccessibilityAttributes.HeadingLevelAttribute

**Framework**: Foundation  
**Kind**: enum

An attribute for the level of this heading.

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
enum HeadingLevelAttribute
```

#### Overview

Assistive technologies can use this property to improve navigation and describe the level number of levels [`AttributeScopes.AccessibilityAttributes.HeadingLevelAttribute.HeadingLevel.h1`](attributescopes/accessibilityattributes/headinglevelattribute/headinglevel/h1.md) through [`AttributeScopes.AccessibilityAttributes.HeadingLevelAttribute.HeadingLevel.h6`](attributescopes/accessibilityattributes/headinglevelattribute/headinglevel/h6.md) alongside the text.

For example, you can rank sections within UI using a heading level. The most important section is marked with[`AttributeScopes.AccessibilityAttributes.HeadingLevelAttribute.HeadingLevel.h1`](attributescopes/accessibilityattributes/headinglevelattribute/headinglevel/h1.md). Nested sections can use subsequent heading levels. For unranked headings, use [`AttributeScopes.AccessibilityAttributes.HeadingLevelAttribute.HeadingLevel.unspecified`](attributescopes/accessibilityattributes/headinglevelattribute/headinglevel/unspecified.md).

## Topics

### Enumerations
- [AttributeScopes.AccessibilityAttributes.HeadingLevelAttribute.HeadingLevel](attributescopes/accessibilityattributes/headinglevelattribute/headinglevel.md)
  The hierarchy of a heading in relation other headings.

## Relationships

### Conforms To
- [AttributedStringKey](attributedstringkey.md)
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Copyable](../Swift/Copyable.md)
- [DecodableAttributedStringKey](decodableattributedstringkey.md)
- [EncodableAttributedStringKey](encodableattributedstringkey.md)
- [MarkdownDecodableAttributedStringKey](markdowndecodableattributedstringkey.md)
- [ObjectiveCConvertibleAttributedStringKey](objectivecconvertibleattributedstringkey.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/attributescopes/accessibilityattributes/headinglevelattribute)*
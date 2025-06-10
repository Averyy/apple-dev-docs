# AttributeScopes.AccessibilityAttributes.TextualContextAttribute

**Framework**: Foundation  
**Kind**: enum

An attribute for the textual context.

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
enum TextualContextAttribute
```

#### Overview

Assistive technologies can use this property to choose an appropriate way to output the text. For example, when encountering a source coding context, VoiceOver could choose to speak all punctuation.

> **Note**: This attribute is not used on macOS

## Topics

### Enumerations
- [AttributeScopes.AccessibilityAttributes.TextualContextAttribute.TextualContext](attributescopes/accessibilityattributes/textualcontextattribute/textualcontext.md)
  Textual context that assistive technologies can use to improve the presentation of spoken text.

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

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/attributescopes/accessibilityattributes/textualcontextattribute)*
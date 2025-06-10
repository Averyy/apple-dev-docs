# AttributeScopes.AccessibilityAttributes.AdjustedPitchAttribute

**Framework**: Foundation  
**Kind**: enum

An attribute to adjust the pitch the spoken speech.

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
enum AdjustedPitchAttribute
```

#### Overview

Values between `-1` and `0` result in a lower pitch while values between `0` and `1` result in a higher pitch.

For example, you may want to lower the pitch when an object is deleted, or raise the pitch if an object is inserted.

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

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/attributescopes/accessibilityattributes/adjustedpitchattribute)*
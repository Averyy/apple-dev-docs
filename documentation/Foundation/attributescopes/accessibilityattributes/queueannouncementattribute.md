# AttributeScopes.AccessibilityAttributes.QueueAnnouncementAttribute

**Framework**: Foundation  
**Kind**: enum

An attribute to define if speech announcements spoken by VoiceOver should be queued behind existing speech rather than interrupting speech in progress.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+
- Unknown ?+ - Deprecated

## Declaration

```swift
@frozen
enum QueueAnnouncementAttribute
```

#### Overview

When `true`, the announcement will be queued behind existing speech. When `false`, it will interrupt existing speech. By default, announcements interrupt existing speech.

> **Note**: This attribute is not used on macOS

## Relationships

### Conforms To
- [AttributedStringKey](attributedstringkey.md)
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Copyable](../Swift/Copyable.md)
- [DecodableAttributedStringKey](decodableattributedstringkey.md)
- [EncodableAttributedStringKey](encodableattributedstringkey.md)
- [MarkdownDecodableAttributedStringKey](markdowndecodableattributedstringkey.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/attributescopes/accessibilityattributes/queueannouncementattribute)*
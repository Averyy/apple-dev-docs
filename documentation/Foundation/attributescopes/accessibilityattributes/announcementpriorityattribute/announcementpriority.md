# AttributeScopes.AccessibilityAttributes.AnnouncementPriorityAttribute.AnnouncementPriority

**Framework**: Foundation  
**Kind**: enum  
**Role**: Enumeration

A priority level used by accessibility clients, such as VoiceOver, to control how announcements are queued and presented.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
enum AnnouncementPriority
```

## Topics

### Enumeration Cases
- [AttributeScopes.AccessibilityAttributes.AnnouncementPriorityAttribute.AnnouncementPriority.default](./announcementpriority/default.md)
  Announcements will interrupt existing speech, but are interruptible if a new speech utterance is started.
- [AttributeScopes.AccessibilityAttributes.AnnouncementPriorityAttribute.AnnouncementPriority.high](./announcementpriority/high.md)
  Announcements will interrupt other speech and cannot be interrupted once started.
- [AttributeScopes.AccessibilityAttributes.AnnouncementPriorityAttribute.AnnouncementPriority.low](./announcementpriority/low.md)
  Announcements are queued and spoken when other speech utterances have completed.

## Relationships

### Conforms To
- [Copyable](../../../../Swift/copyable.md)
- [Decodable](../../../../Swift/decodable.md)
- [Encodable](../../../../Swift/encodable.md)
- [Equatable](../../../../Swift/equatable.md)
- [Escapable](../../../../Swift/escapable.md)
- [Hashable](../../../../Swift/hashable.md)
- [RawRepresentable](../../../../Swift/rawrepresentable.md)
- [Sendable](../../../../Swift/sendable.md)
- [SendableMetatype](../../../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/attributescopes/accessibilityattributes/announcementpriorityattribute/announcementpriority)*
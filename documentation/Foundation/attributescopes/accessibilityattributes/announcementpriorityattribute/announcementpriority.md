# AttributeScopes.AccessibilityAttributes.AnnouncementPriorityAttribute.AnnouncementPriority

**Framework**: Foundation  
**Kind**: enum

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
- [AttributeScopes.AccessibilityAttributes.AnnouncementPriorityAttribute.AnnouncementPriority.default](attributescopes/accessibilityattributes/announcementpriorityattribute/announcementpriority/default.md)
  Announcements will interrupt existing speech, but are interruptible if a new speech utterance is started.
- [AttributeScopes.AccessibilityAttributes.AnnouncementPriorityAttribute.AnnouncementPriority.high](attributescopes/accessibilityattributes/announcementpriorityattribute/announcementpriority/high.md)
  Announcements will interrupt other speech and cannot be interrupted once started.
- [AttributeScopes.AccessibilityAttributes.AnnouncementPriorityAttribute.AnnouncementPriority.low](attributescopes/accessibilityattributes/announcementpriorityattribute/announcementpriority/low.md)
  Announcements are queued and spoken when other speech utterances have completed.

## Relationships

### Conforms To
- [Copyable](../swift/copyable.md)
- [Decodable](../swift/decodable.md)
- [Encodable](../swift/encodable.md)
- [Equatable](../swift/equatable.md)
- [Escapable](../swift/escapable.md)
- [Hashable](../swift/hashable.md)
- [RawRepresentable](../swift/rawrepresentable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/attributescopes/accessibilityattributes/announcementpriorityattribute/announcementpriority)*
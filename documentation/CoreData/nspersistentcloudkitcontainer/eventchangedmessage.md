# NSPersistentCloudKitContainer.EventChangedMessage

**Framework**: Core Data  
**Kind**: struct

Posted when a CloudKit event occurs on the CloudKit private serial queue.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst ?+
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
struct EventChangedMessage
```

## Topics

### Instance Properties
- [let event: NSPersistentCloudKitContainer.Event](nspersistentcloudkitcontainer/eventchangedmessage/event.md)
  The CloudKit event that triggered this notification.

## Relationships

### Conforms To
- [NotificationCenter.AsyncMessage](../Foundation/NotificationCenter/AsyncMessage.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nspersistentcloudkitcontainer/eventchangedmessage)*